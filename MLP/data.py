def generate_soap_notes(n:int) -> list:
    '''
    Generates synthetic SOAP notes.

            Parameters:
                    n (int): The number of SOAP notes to generate

            Returns:
                    soap_notes (list): A list of strings
    '''
    soap_notes = []

    # Assure that n is an integer
    if not isinstance(n, int):
        raise TypeError("Expected int. Received " + type(n).__name__)
    
    # Assure the user requests a reasonable number of SOAP notes
    if n >= 1000000:
        raise ValueError("Too many SOAP notes requested!")
    if n < 1:
        raise ValueError("Too few SOAP notes requested!")
    
    # Read in data from the SNOMED CT problems list
    return soap_notes