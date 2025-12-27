from customopenai import CustomOpenAI
from extracttextfromimage import ExtractTextFromImage

# SET subscription_key to the 32-character Private Key, which is required to call Azure Rest API endpoint. 
#This key can be found in your Azure console.
vision_subscription_key = 'aabbccddeeffgghhiijjkkllmmnnooppqq'

# SET Azure Computer Vision Cognitive Service API Endpoint
# This endpoint can be found in your Azure console.
vision_cognitive_service_url = 'https://aabbccddee.cognitiveservices.azure.com/'

# SET URL to image file 
# For demo, this image is a photo of a clothing tag which displays the fiber types and their percentage composition
read_image_url = "https://chiuvention.com/wp-content/uploads/2024/01/fabric-composition-1.jpg"

extracttextobj = ExtractTextFromImage()
tagtext = extracttextobj.do_extract_text(
  read_image_url=read_image_url, 
  subscription_key=vision_subscription_key, 
  cognitive_service_url=vision_cognitive_service_url
)

#SET input variable to extracted text from image. The image is a photo of a clothing tag.
input = tagtext

# SET subscription_key to the 32-character Private Key, which is required to call Azure Rest API endpoint. 
#This key can be found in your Azure console.
openai_subscription_key = 'aabbccddeeffgghhiijjkkllmmnnooppqq'

# SET Azure Computer Vision Cognitive Service API Endpoint
# This endpoint can be found in your Azure console.
openai_cognitive_service_url = 'https://aabbcc-azure-openai.openai.azure.com/'


aiobject = CustomOpenAI(
           api_url = openai_cognitive_service_url,
           api_key = openai_subscription_key,  
           api_version = "2025-04-14", # This is available in Microsoft Foundry Chat Playground's available deployment models
           deployment_name = 'gpt-4' # This is available in Microsoft Foundry Chat Playground's available deployment models
        )

prompt = 'Find the fiber type names and fiber type percentages, and display them in a bulleted list from this text: ' + input

#The fiber_type variable contains chat response from Open AI GPT-4 model, which expects to be fiber type names and their percentage composition in the clothing.
fiber_type = aiobject.get_open_ai_output(prompt)
if fiber_type is not None:
   print (fiber_type)
