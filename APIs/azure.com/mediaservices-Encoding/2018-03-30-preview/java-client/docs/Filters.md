

# Filters

Describes all the filtering operations, such as de-interlacing, rotation etc. that are to be applied to the input media before encoding.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crop** | [**Rectangle**](Rectangle.md) |  |  [optional] |
|**deinterlace** | [**Deinterlace**](Deinterlace.md) |  |  [optional] |
|**overlays** | [**List&lt;Overlay&gt;**](Overlay.md) | The properties of overlays to be applied to the input video. These could be audio, image or video overlays. |  [optional] |
|**rotation** | [**RotationEnum**](#RotationEnum) | The rotation, if any, to be applied to the input video, before it is encoded. Default is Auto |  [optional] |



## Enum: RotationEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;Auto&quot; |
| NONE | &quot;None&quot; |
| ROTATE0 | &quot;Rotate0&quot; |
| ROTATE90 | &quot;Rotate90&quot; |
| ROTATE180 | &quot;Rotate180&quot; |
| ROTATE270 | &quot;Rotate270&quot; |



