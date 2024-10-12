# AnchoreEngineApiServer.PaginatedVulnerableImageList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPage** | **String** | True if additional pages exist (page + 1) or False if this is the last page | [optional] 
**page** | **String** | The page number returned (should match the requested page query string param) | [optional] 
**returnedCount** | **Number** | The number of items sent in this response | [optional] 
**images** | [**[VulnerableImage]**](VulnerableImage.md) |  | [optional] 


