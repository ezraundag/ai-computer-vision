from openai import AzureOpenAI

class CustomOpenAI:
    def __init__(self, api_url, api_key, api_version,deployment_name):
        self.api_url = api_url
        self.api_key = api_key
        self.api_version=api_version
        self.deployment_name=deployment_name
    
    def get_open_ai_output(self,prompt):
        client = AzureOpenAI(
            api_key=self.api_key,  
            api_version=self.api_version,
            azure_endpoint=self.api_url
        )
        deployment_name = self.deployment_name
        output = ''

        try:
            response = client.chat.completions.create(
                        model=deployment_name,
                        messages=[
                                {"role": "system", "content": "You are a helpful data scientist."},
                                {"role": "user", "content":prompt }
                            ]
                        )
            output = response.choices[0].message.content
            

        except openai.AuthenticationError as e:
            # Handle Authentication error here, e.g. invalid API key
            print(f"OpenAI API returned an Authentication Error: {e}")
            output = 'ERROR'

        except openai.APIConnectionError as e:
            # Handle connection error here
            print(f"Failed to connect to OpenAI API: {e}")
            output = 'ERROR'

        except openai.BadRequestError as e:
            # Handle connection error here
            print(f"Invalid Request Error: {e}")
            output = 'ERROR'

        except openai.RateLimitError as e:
            # Handle rate limit error
            print(f"OpenAI API request exceeded rate limit: {e}")
            output = 'ERROR'

        except openai.InternalServerError as e:
            # Handle Service Unavailable error
            print(f"Service Unavailable: {e}")
            output = 'ERROR'

        except openai.APITimeoutError as e:
            # Handle request timeout
            print(f"Request timed out: {e}")
            output = 'ERROR'
            
        except openai.APIError as e:
            # Handle API error here, e.g. retry or log
            print(f"OpenAI API returned an API Error: {e}")
            output = 'ERROR'

        except:
            # Handles all other exceptions
            print("An exception has occured.")
            output = 'ERROR'

        return output
