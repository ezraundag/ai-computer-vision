from customcomputervision import CustomComputerVision

class ExtractTextFromImage: 
  def do_extract_text(self, read_image_url, subscription_key, cognitive_service_url ):
    obj = CustomComputerVision(subscription_key,cognitive_service_url)
    tagText = obj.gettagtext(read_image_url=read_image_url)
    return tagText

