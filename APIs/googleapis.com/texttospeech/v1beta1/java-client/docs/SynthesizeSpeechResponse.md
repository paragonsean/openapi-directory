

# SynthesizeSpeechResponse

The message returned to the client by the `SynthesizeSpeech` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioConfig** | [**AudioConfig**](AudioConfig.md) |  |  [optional] |
|**audioContent** | **byte[]** | The audio data bytes encoded as specified in the request, including the header for encodings that are wrapped in containers (e.g. MP3, OGG_OPUS). For LINEAR16 audio, we include the WAV header. Note: as with all bytes fields, protobuffers use a pure binary representation, whereas JSON representations use base64. |  [optional] |
|**timepoints** | [**List&lt;Timepoint&gt;**](Timepoint.md) | A link between a position in the original request input and a corresponding time in the output audio. It&#39;s only supported via &#x60;&#x60; of SSML input. |  [optional] |



