

# ImageError

A message resulting from reading an image file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | The type of image error encountered. Optional for older image errors. |  [optional] |
|**filePath** | **String** | The file path in the import of the image that was rejected. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| INVALID_IMAGE | &quot;INVALID_IMAGE&quot; |
| IMAGE_TOO_BIG | &quot;IMAGE_TOO_BIG&quot; |
| WRONG_IMAGE_TYPE | &quot;WRONG_IMAGE_TYPE&quot; |



