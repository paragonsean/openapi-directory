

# ReplaceImageRequest

Replaces an existing image with a new image. Replacing an image removes some image effects from the existing image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageObjectId** | **String** | The ID of the existing image that will be replaced. The ID can be retrieved from the response of a get request. |  [optional] |
|**imageReplaceMethod** | [**ImageReplaceMethodEnum**](#ImageReplaceMethodEnum) | The replacement method. |  [optional] |
|**url** | **String** | The image URL. The image is fetched once at insertion time and a copy is stored for display inside the presentation. Images must be less than 50MB, cannot exceed 25 megapixels, and must be in PNG, JPEG, or GIF format. The provided URL can&#39;t surpass 2 KB in length. The URL is saved with the image, and exposed through the Image.source_url field. |  [optional] |



## Enum: ImageReplaceMethodEnum

| Name | Value |
|---- | -----|
| IMAGE_REPLACE_METHOD_UNSPECIFIED | &quot;IMAGE_REPLACE_METHOD_UNSPECIFIED&quot; |
| CENTER_INSIDE | &quot;CENTER_INSIDE&quot; |
| CENTER_CROP | &quot;CENTER_CROP&quot; |



