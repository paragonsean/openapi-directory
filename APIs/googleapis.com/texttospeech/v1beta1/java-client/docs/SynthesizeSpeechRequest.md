

# SynthesizeSpeechRequest

The top-level message sent by the client for the `SynthesizeSpeech` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioConfig** | [**AudioConfig**](AudioConfig.md) |  |  [optional] |
|**enableTimePointing** | [**List&lt;EnableTimePointingEnum&gt;**](#List&lt;EnableTimePointingEnum&gt;) | Whether and what timepoints are returned in the response. |  [optional] |
|**input** | [**SynthesisInput**](SynthesisInput.md) |  |  [optional] |
|**voice** | [**VoiceSelectionParams**](VoiceSelectionParams.md) |  |  [optional] |



## Enum: List&lt;EnableTimePointingEnum&gt;

| Name | Value |
|---- | -----|
| TIMEPOINT_TYPE_UNSPECIFIED | &quot;TIMEPOINT_TYPE_UNSPECIFIED&quot; |
| SSML_MARK | &quot;SSML_MARK&quot; |



