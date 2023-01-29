def generate_soap_notes(n:int, anonymize_patient:bool=True, use_full_section_headers:bool=False) -> list:
    '''
    Generates synthetic SOAP notes.

            Parameters:
                    n (int): The number of SOAP notes to generate
                    anonymize_patient (bool): Should the patient name be anonymous (default True)
                    use_full_section_headers (bool): Produce SOAP notes with a full text section header (default False)

            Returns:
                    soap_notes (list): A list of strings
    '''
    # Validate user input

    ## Assure that n is an integer
    if not isinstance(n, int):
        raise TypeError("n must be an int. Received a " + type(n).__name__)
    ## Assure that anonymize_patient is a bool
    if not isinstance(anonymize_patient, bool):
        raise TypeError("anonymize_patient must be a bool. Received a " + type(anonymize_patient).__name__)
    ## Assure that use_full_section_headers is a bool
    if not isinstance(use_full_section_headers, bool):
        raise TypeError("use_full_section_headers must be a bool. Received a " + type(use_full_section_headers).__name__)
    
    ## Assure the user requests a reasonable number of SOAP notes
    if n >= 1000000:
        raise ValueError("Too many SOAP notes requested!")
    if n < 1:
        raise ValueError("Too few SOAP notes requested!")
    
    # Get a template to fill in
    if use_full_section_headers:
        soap_template = "Subjective\n[subjective]\nObjective\n[objective]\nAssessment\n[assessment]\nPlan\n[plan]"
    else:
        soap_template = "S: [subjective]\nO: [objective]\nA: [assessment]\nP: [plan]"

    # Read in data from the SNOMED CT problems list

    # Create the SOAP notes
    soap_notes = []
    for i in range(n):
        subjective = "s"
        objective = "o"
        assessment = "a"
        plan = "p"
        soap_note = soap_template.replace("[subjective]", subjective).replace("[objective]", objective).replace("[assessment]", assessment).replace("[plan]", plan)
        soap_notes.append(soap_note)
    
    return soap_notes