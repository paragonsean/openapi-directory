

# H264Layer

Describes the settings to be used when encoding the input video into a desired output bitrate layer with the H.264 video codec.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bufferWindow** | **String** | The VBV buffer window length. The value should be in ISO 8601 format. The value should be in the range [0.1-100] seconds. The default is 5 seconds (for example, PT5S). |  [optional] |
|**entropyMode** | [**EntropyModeEnum**](#EntropyModeEnum) | The entropy mode to be used for this layer. If not specified, the encoder chooses the mode that is appropriate for the profile and level. |  [optional] |
|**level** | **String** | We currently support Level up to 6.2. The value can be Auto, or a number that matches the H.264 profile. If not specified, the default is Auto, which lets the encoder choose the Level that is appropriate for this layer. |  [optional] |
|**profile** | [**ProfileEnum**](#ProfileEnum) | We currently support Baseline, Main, High, High422, High444. Default is Auto. |  [optional] |
|**referenceFrames** | **Integer** | The number of reference frames to be used when encoding this layer. If not specified, the encoder determines an appropriate number based on the encoder complexity setting. |  [optional] |



## Enum: EntropyModeEnum

| Name | Value |
|---- | -----|
| CABAC | &quot;Cabac&quot; |
| CAVLC | &quot;Cavlc&quot; |



## Enum: ProfileEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;Auto&quot; |
| BASELINE | &quot;Baseline&quot; |
| MAIN | &quot;Main&quot; |
| HIGH | &quot;High&quot; |
| HIGH422 | &quot;High422&quot; |
| HIGH444 | &quot;High444&quot; |



