# DialogflowApi.GoogleCloudDialogflowV2beta1SpeechToTextConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **String** | Which Speech model to select. Select the model best suited to your domain to get best results. If a model is not explicitly specified, then Dialogflow auto-selects a model based on other parameters in the SpeechToTextConfig and Agent settings. If enhanced speech model is enabled for the agent and an enhanced version of the specified model for the language does not exist, then the speech is recognized using the standard version of the specified model. Refer to [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics#select-model) for more details. If you specify a model, the following models typically have the best performance: - phone_call (best for Agent Assist and telephony) - latest_short (best for Dialogflow non-telephony) - command_and_search Leave this field unspecified to use [Agent Speech settings](https://cloud.google.com/dialogflow/cx/docs/concept/agent#settings-speech) for model selection. | [optional] 
**speechModelVariant** | **String** | The speech model used in speech to text. &#x60;SPEECH_MODEL_VARIANT_UNSPECIFIED&#x60;, &#x60;USE_BEST_AVAILABLE&#x60; will be treated as &#x60;USE_ENHANCED&#x60;. It can be overridden in AnalyzeContentRequest and StreamingAnalyzeContentRequest request. If enhanced model variant is specified and an enhanced version of the specified model for the language does not exist, then it would emit an error. | [optional] 
**useTimeoutBasedEndpointing** | **Boolean** | Use timeout based endpointing, interpreting endpointer sensitivy as seconds of timeout value. | [optional] 



## Enum: SpeechModelVariantEnum


* `SPEECH_MODEL_VARIANT_UNSPECIFIED` (value: `"SPEECH_MODEL_VARIANT_UNSPECIFIED"`)

* `USE_BEST_AVAILABLE` (value: `"USE_BEST_AVAILABLE"`)

* `USE_STANDARD` (value: `"USE_STANDARD"`)

* `USE_ENHANCED` (value: `"USE_ENHANCED"`)




