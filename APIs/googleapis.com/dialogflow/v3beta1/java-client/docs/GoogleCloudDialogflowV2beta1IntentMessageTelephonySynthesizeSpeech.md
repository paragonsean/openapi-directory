

# GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech

Synthesizes speech and plays back the synthesized audio to the caller in Telephony Gateway. Telephony Gateway takes the synthesizer settings from `DetectIntentResponse.output_audio_config` which can either be set at request-level or can come from the agent-level synthesizer config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ssml** | **String** | The SSML to be synthesized. For more information, see [SSML](https://developers.google.com/actions/reference/ssml). |  [optional] |
|**text** | **String** | The raw text to be synthesized. |  [optional] |



