This repo contains python scripts that extract text from images using Azure Computer Vision and analyzes the extracted text using Azure Open AI service. 

I wrote these scripts to streamline text extraction and analysis using Open AI SDK for a quantitative research on waste policies.

**CustomComputerVision.py**

This python script contains a custom client class that uses Azure Computer Vision SDK to extract text from an image.

**ExtractTextFromImage.py**

This python script contains a custom function that utilizes CustomComputerVision class to extract text from an image.

**CustomOpenAI.py**

This python script contains a custom client class that uses Azure Open AI and feeds it with prompts for data analysis.

**askopenai.py**

This python script contains calls to functions in ExtractTextFromImage.py and CustomOpenAI.py.
It extracts text from a clothing tag image and prompts Open AI to find the fiber type names and percentages in the clothing tag.

