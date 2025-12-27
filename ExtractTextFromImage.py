from customcomputervision import CustomComputerVision


# SET subscription_key to the 32-character Private Key, which is required to call Azure Rest API endpoint. 
#This key can be found in your Azure console.
subscription_key = 'aabbccddeeffgghhiijjkkllmmnnooppqq'

# SET Azure Computer Vision Cognitive Service API Endpoint
# This endpoint can be found in your Azure console.
cognitive_service_url = 'https://aabbccddee.cognitiveservices.azure.com/'

obj = CustomComputerVision(subscription_key,cognitive_service_url)

# SET URL to image file 
read_image_url = "https://shsthetribe.com/wp-content/uploads/2023/10/02B4FF51-0B37-4778-B1C3-4BB3D5911FB0-e1697125385980-900x1200.jpeg"

tagText = obj.gettagtext(read_image_url=read_image_url)

#print text
print(tagText)

