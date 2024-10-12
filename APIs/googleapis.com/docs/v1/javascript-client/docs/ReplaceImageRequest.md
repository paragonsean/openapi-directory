# GoogleDocsApi.ReplaceImageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imageObjectId** | **String** | The ID of the existing image that will be replaced. The ID can be retrieved from the response of a get request. | [optional] 
**imageReplaceMethod** | **String** | The replacement method. | [optional] 
**uri** | **String** | The URI of the new image. The image is fetched once at insertion time and a copy is stored for display inside the document. Images must be less than 50MB, cannot exceed 25 megapixels, and must be in PNG, JPEG, or GIF format. The provided URI can&#39;t surpass 2 KB in length. The URI is saved with the image, and exposed through the ImageProperties.source_uri field. | [optional] 



## Enum: ImageReplaceMethodEnum


* `IMAGE_REPLACE_METHOD_UNSPECIFIED` (value: `"IMAGE_REPLACE_METHOD_UNSPECIFIED"`)

* `CENTER_CROP` (value: `"CENTER_CROP"`)




