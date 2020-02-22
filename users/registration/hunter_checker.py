import requests

class HunterEmail:

    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = " https://api.hunter.io/v2/email-verifier"
    
    def email_verifier(self, email):
        params = {'email': email, 'api_key': self.api_key}
        response = requests.get(self.endpoint, params)
        
        result = response.json()["data"]["result"]
        return result