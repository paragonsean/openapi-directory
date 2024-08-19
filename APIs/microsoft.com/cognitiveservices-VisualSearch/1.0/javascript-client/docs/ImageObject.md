# VisualSearchClient.ImageObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accentColor** | **String** | A three-byte hexadecimal number that represents the color that dominates the image. Use the color as the temporary background in your client until the image is loaded. | [optional] [readonly] 
**imageId** | **String** | Unique Id for the image. | [optional] [readonly] 
**imageInsightsToken** | **String** | The token that you use in a subsequent call to Visual Search API to get additional information about the image. For information about using this token, see the imageInsightsToken field inside the knowledgeRequest request parameter. | [optional] [readonly] 
**insightsMetadata** | [**ImagesImageMetadata**](ImagesImageMetadata.md) |  | [optional] 
**thumbnail** | [**ImageObject**](ImageObject.md) |  | [optional] 
**visualWords** | **String** | For internal use only. | [optional] [readonly] 


