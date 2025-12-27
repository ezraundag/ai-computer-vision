from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import time
import re

class CustomComputerVision:

    def __init__(self, subscription_key, endpoint):
        self.subscription_key = subscription_key
        self.endpoint = endpoint
    
    def gettagtext(self,read_image_url):
        tagText=''
        computervision_client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))

        '''
        OCR: Read File using the Read API, extract text - remote
        This  will extract text in an image.
        '''
        # Get an image with text
        try:
            # Call API with URL and raw response (allows you to get the operation location)
            read_response = computervision_client.read(read_image_url,  raw=True)

            # Get the operation location (URL with an ID at the end) from the response
            read_operation_location = read_response.headers["Operation-Location"]
            # Grab the ID from the URL
            operation_id = read_operation_location.split("/")[-1]

            # Call the "GET" API and wait for it to retrieve the results 
            while True:
                read_result = computervision_client.get_read_result(operation_id)
                if read_result.status not in ['notStarted', 'running']:
                    break
                time.sleep(1)

            # Print the detected text, line by line
            if read_result.status == OperationStatusCodes.succeeded:
            
                for text_result in read_result.analyze_result.read_results:
                    for line in text_result.lines:
                        tagText+=line.text
                        tagText+="\n"
            '''
            END - Read File - remote
            '''
        except:
            # Handles all other exceptions
            print("An exception has occured.")

        return tagText


