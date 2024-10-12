# GoogleDocsApi.InsertInlineImageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endOfSegmentLocation** | [**EndOfSegmentLocation**](EndOfSegmentLocation.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**objectSize** | [**Size**](Size.md) |  | [optional] 
**uri** | **String** | The image URI. The image is fetched once at insertion time and a copy is stored for display inside the document. Images must be less than 50MB in size, cannot exceed 25 megapixels, and must be in one of PNG, JPEG, or GIF format. The provided URI must be publicly accessible and at most 2 kB in length. The URI itself is saved with the image, and exposed via the ImageProperties.content_uri field. | [optional] 


