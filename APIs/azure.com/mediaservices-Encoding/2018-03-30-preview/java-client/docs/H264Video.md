

# H264Video

Describes all the properties for encoding a video with the H.264 codec.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**complexity** | [**ComplexityEnum**](#ComplexityEnum) | Tells the encoder how to choose its encoding settings. The default value is Balanced. |  [optional] |
|**layers** | [**List&lt;H264Layer&gt;**](H264Layer.md) | The collection of output H.264 layers to be produced by the encoder. |  [optional] |
|**sceneChangeDetection** | **Boolean** | Whether or not the encoder should insert key frames at scene changes. If not specified, the default is false. This flag should be set to true only when the encoder is being configured to produce a single output video. |  [optional] |



## Enum: ComplexityEnum

| Name | Value |
|---- | -----|
| SPEED | &quot;Speed&quot; |
| BALANCED | &quot;Balanced&quot; |
| QUALITY | &quot;Quality&quot; |



