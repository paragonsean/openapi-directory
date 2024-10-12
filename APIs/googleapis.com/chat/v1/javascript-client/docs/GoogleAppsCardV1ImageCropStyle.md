# GoogleChatApi.GoogleAppsCardV1ImageCropStyle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspectRatio** | **Number** | The aspect ratio to use if the crop type is &#x60;RECTANGLE_CUSTOM&#x60;. For example, here&#39;s how to apply a 16:9 aspect ratio: &#x60;&#x60;&#x60; cropStyle { \&quot;type\&quot;: \&quot;RECTANGLE_CUSTOM\&quot;, \&quot;aspectRatio\&quot;: 16/9 } &#x60;&#x60;&#x60; | [optional] 
**type** | **String** | The crop type. | [optional] 



## Enum: TypeEnum


* `IMAGE_CROP_TYPE_UNSPECIFIED` (value: `"IMAGE_CROP_TYPE_UNSPECIFIED"`)

* `SQUARE` (value: `"SQUARE"`)

* `CIRCLE` (value: `"CIRCLE"`)

* `RECTANGLE_CUSTOM` (value: `"RECTANGLE_CUSTOM"`)

* `RECTANGLE_4_3` (value: `"RECTANGLE_4_3"`)




