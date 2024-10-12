

# AudioConfig

Description of audio data to be synthesized.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioEncoding** | [**AudioEncodingEnum**](#AudioEncodingEnum) | Required. The format of the audio byte stream. |  [optional] |
|**effectsProfileId** | **List&lt;String&gt;** | Optional. Input only. An identifier which selects &#39;audio effects&#39; profiles that are applied on (post synthesized) text to speech. Effects are applied on top of each other in the order they are given. See [audio profiles](https://cloud.google.com/text-to-speech/docs/audio-profiles) for current supported profile ids. |  [optional] |
|**pitch** | **Double** | Optional. Input only. Speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the original pitch. -20 means decrease 20 semitones from the original pitch. |  [optional] |
|**sampleRateHertz** | **Integer** | Optional. The synthesis sample rate (in hertz) for this audio. When this is specified in SynthesizeSpeechRequest, if this is different from the voice&#39;s natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality), unless the specified sample rate is not supported for the encoding chosen, in which case it will fail the request and return google.rpc.Code.INVALID_ARGUMENT. |  [optional] |
|**speakingRate** | **Double** | Optional. Input only. Speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values &lt; 0.25 or &gt; 4.0 will return an error. |  [optional] |
|**volumeGainDb** | **Double** | Optional. Input only. Volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. Strongly recommend not to exceed +10 (dB) as there&#39;s usually no effective increase in loudness for any value greater than that. |  [optional] |



## Enum: AudioEncodingEnum

| Name | Value |
|---- | -----|
| AUDIO_ENCODING_UNSPECIFIED | &quot;AUDIO_ENCODING_UNSPECIFIED&quot; |
| LINEAR16 | &quot;LINEAR16&quot; |
| MP3 | &quot;MP3&quot; |
| MP3_64_KBPS | &quot;MP3_64_KBPS&quot; |
| OGG_OPUS | &quot;OGG_OPUS&quot; |
| MULAW | &quot;MULAW&quot; |
| ALAW | &quot;ALAW&quot; |



