# ThePlaidApi.PhysicalDocumentImages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**croppedBack** | **String** | Temporary URL that expires after 60 seconds for downloading a cropped image containing just the back of the document. Might be null if the back of the document was not collected. | 
**croppedFront** | **String** | Temporary URL that expires after 60 seconds for downloading a cropped image containing just the front of the document. | 
**face** | **String** | Temporary URL that expires after 60 seconds for downloading a crop of just the user&#39;s face from the document image. Might be null if the document does not contain a face photo. | 
**originalBack** | **String** | Temporary URL that expires after 60 seconds for downloading the original image of the back of the document. Might be null if the back of the document was not collected. | 
**originalFront** | **String** | Temporary URL that expires after 60 seconds for downloading the uncropped original image of the front of the document. | 


