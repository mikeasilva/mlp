import random
import typing


def generate_soap_notes(
    n: int,
    patient_gender: typing.Optional[str] = None,
    anonymize_patient: bool = True,
    use_full_section_headers: bool = False,
) -> list:
    """
    Generates synthetic SOAP notes.

            Parameters:
                    n (int): The number of SOAP notes to generate
                    patient_gender (str, optional): The desired gender of the patient (supports male or female).  If none is specified one will be chosen at random.
                    anonymize_patient (bool, optional): Should the patient name be anonymous (default True)
                    use_full_section_headers (bool, optional): Produce SOAP notes with a full text section header (default False)

            Returns:
                    soap_notes (list): A list of strings
    """
    # Validate user input

    ## Assure that n is an integer
    if not isinstance(n, int):
        raise TypeError("n must be an int. Received a " + type(n).__name__)
    ## Assure that patient_gender is a str or None
    if not (isinstance(patient_gender, str) or patient_gender is None):
        raise TypeError(
            "patient_gender must be a str or None. Received a "
            + type(patient_gender).__name__
        )
    elif isinstance(patient_gender, str):
        ## Check to see the patient gender is valid (supported)
        if not patient_gender.lower() in ["male", "female"]:
            raise ValueError(
                "patient_gender not male or female. Received " + patient_gender
            )
        ## make sure it's lower case
        patient_gender = patient_gender.lower()

    ## Assure that anonymize_patient is a bool
    if not isinstance(anonymize_patient, bool):
        raise TypeError(
            "anonymize_patient must be a bool. Received a "
            + type(anonymize_patient).__name__
        )
    ## Assure that use_full_section_headers is a bool
    if not isinstance(use_full_section_headers, bool):
        raise TypeError(
            "use_full_section_headers must be a bool. Received a "
            + type(use_full_section_headers).__name__
        )

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
        # Determine the patient gender if not specified
        if patient_gender is None:
            if random.randint(0, 1) == 1:
                patient_gender == "male"
            else:
                patient_gender == "female"
        
        # Determine how to refer to the patient as 
        if anonymize_patient:
            refer_to_patient_as ="the patient"
        else:
            if patient_gender == "male":
                max_lines = 2943 # Number of lines in ./data/male.txt
            else:
                max_lines = 5001 # Number of lines in ./data/female.txt
        
            line_number = random.randint(0, max_lines)

            with open(f"data/{patient_gender}.txt", 'r') as fp:
                refer_to_patient_as = fp.readlines()[line_number:line_number]
                
        subjective = "s"
        objective = "o"
        assessment = "a"
        plan = "p"
        soap_note = (
            soap_template.replace("[subjective]", subjective)
            .replace("[objective]", objective)
            .replace("[assessment]", assessment)
            .replace("[plan]", plan)
        )
        soap_notes.append(soap_note)

    return soap_notes
