# GoogleSlidesApi.ReplaceImageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imageObjectId** | **String** | The ID of the existing image that will be replaced. The ID can be retrieved from the response of a get request. | [optional] 
**imageReplaceMethod** | **String** | The replacement method. | [optional] 
**url** | **String** | The image URL. The image is fetched once at insertion time and a copy is stored for display inside the presentation. Images must be less than 50MB, cannot exceed 25 megapixels, and must be in PNG, JPEG, or GIF format. The provided URL can&#39;t surpass 2 KB in length. The URL is saved with the image, and exposed through the Image.source_url field. | [optional] 



## Enum: ImageReplaceMethodEnum


* `IMAGE_REPLACE_METHOD_UNSPECIFIED` (value: `"IMAGE_REPLACE_METHOD_UNSPECIFIED"`)

* `CENTER_INSIDE` (value: `"CENTER_INSIDE"`)

* `CENTER_CROP` (value: `"CENTER_CROP"`)




