

# GoogleCloudDialogflowV2beta1SynthesizeSpeechConfig

Configuration of how speech should be synthesized.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**effectsProfileId** | **List&lt;String&gt;** | Optional. An identifier which selects &#39;audio effects&#39; profiles that are applied on (post synthesized) text to speech. Effects are applied on top of each other in the order they are given. |  [optional] |
|**pitch** | **Double** | Optional. Speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the original pitch. -20 means decrease 20 semitones from the original pitch. |  [optional] |
|**speakingRate** | **Double** | Optional. Speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values &lt; 0.25 or &gt; 4.0 will return an error. |  [optional] |
|**voice** | [**GoogleCloudDialogflowV2beta1VoiceSelectionParams**](GoogleCloudDialogflowV2beta1VoiceSelectionParams.md) |  |  [optional] |
|**volumeGainDb** | **Double** | Optional. Volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. We strongly recommend not to exceed +10 (dB) as there&#39;s usually no effective increase in loudness for any value greater than that. |  [optional] |



