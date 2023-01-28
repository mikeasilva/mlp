def generate_soap_notes(n:int) -> list:
    '''
    Generates synthetic SOAP notes.

            Parameters:
                    n (int): The number of SOAP notes to generate

            Returns:
                    soap_notes (list): A list of strings
    '''
    # Validate user input

    ## Assure that n is an integer
    if not isinstance(n, int):
        raise TypeError("Expected int. Received " + type(n).__name__)
    
    ## Assure the user requests a reasonable number of SOAP notes
    if n >= 1000000:
        raise ValueError("Too many SOAP notes requested!")
    if n < 1:
        raise ValueError("Too few SOAP notes requested!")
    
    # Get a template to fill in
    soap_template = r"Subjective\n[subjective}]nObjective\n[objective]\Assessment\n[assessment}]nPlan\n[plan]"

    # Read in data from the SNOMED CT problems list

    # Create the SOAP notes
    soap_notes = []
    for i in range(0, n):
        subjective = "s"
        objective = "o"
        assessment = "a"
        plan = "p"
        soap_note = soap_template.replace("[subjective]", subjective).replace("[objective]", objective).replace("[assessment]", assessment).replace("[plan]", plan)
        soap_notes.append(soap_note)
    
    return soap_notes