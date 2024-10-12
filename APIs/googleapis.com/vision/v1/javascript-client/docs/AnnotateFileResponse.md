# CloudVisionApi.AnnotateFileResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Status**](Status.md) |  | [optional] 
**inputConfig** | [**InputConfig**](InputConfig.md) |  | [optional] 
**responses** | [**[AnnotateImageResponse]**](AnnotateImageResponse.md) | Individual responses to images found within the file. This field will be empty if the &#x60;error&#x60; field is set. | [optional] 
**totalPages** | **Number** | This field gives the total number of pages in the file. | [optional] 


