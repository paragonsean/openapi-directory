

# GoogleAppsCardV1ImageCropStyle

Represents the crop style applied to an image. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend): For example, here's how to apply a 16:9 aspect ratio: ``` cropStyle { \"type\": \"RECTANGLE_CUSTOM\", \"aspectRatio\": 16/9 } ```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aspectRatio** | **Double** | The aspect ratio to use if the crop type is &#x60;RECTANGLE_CUSTOM&#x60;. For example, here&#39;s how to apply a 16:9 aspect ratio: &#x60;&#x60;&#x60; cropStyle { \&quot;type\&quot;: \&quot;RECTANGLE_CUSTOM\&quot;, \&quot;aspectRatio\&quot;: 16/9 } &#x60;&#x60;&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The crop type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE_CROP_TYPE_UNSPECIFIED | &quot;IMAGE_CROP_TYPE_UNSPECIFIED&quot; |
| SQUARE | &quot;SQUARE&quot; |
| CIRCLE | &quot;CIRCLE&quot; |
| RECTANGLE_CUSTOM | &quot;RECTANGLE_CUSTOM&quot; |
| RECTANGLE_4_3 | &quot;RECTANGLE_4_3&quot; |



