# DialogflowApi.GoogleCloudDialogflowCxV3QueryResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedSettings** | [**GoogleCloudDialogflowCxV3AdvancedSettings**](GoogleCloudDialogflowCxV3AdvancedSettings.md) |  | [optional] 
**allowAnswerFeedback** | **Boolean** | Indicates whether the Thumbs up/Thumbs down rating controls are need to be shown for the response in the Dialogflow Messenger widget. | [optional] 
**currentPage** | [**GoogleCloudDialogflowCxV3Page**](GoogleCloudDialogflowCxV3Page.md) |  | [optional] 
**diagnosticInfo** | **{String: Object}** | The free-form diagnostic info. For example, this field could contain webhook call latency. The fields of this data can change without notice, so you should not write code that depends on its structure. One of the fields is called \&quot;Alternative Matched Intents\&quot;, which may aid with debugging. The following describes these intent results: - The list is empty if no intent was matched to end-user input. - Only intents that are referenced in the currently active flow are included. - The matched intent is included. - Other intents that could have matched end-user input, but did not match because they are referenced by intent routes that are out of [scope](https://cloud.google.com/dialogflow/cx/docs/concept/handler#scope), are included. - Other intents referenced by intent routes in scope that matched end-user input, but had a lower confidence score. | [optional] 
**dtmf** | [**GoogleCloudDialogflowCxV3DtmfInput**](GoogleCloudDialogflowCxV3DtmfInput.md) |  | [optional] 
**intent** | [**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md) |  | [optional] 
**intentDetectionConfidence** | **Number** | The intent detection confidence. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. This field is deprecated, please use QueryResult.match instead. | [optional] 
**languageCode** | **String** | The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. | [optional] 
**match** | [**GoogleCloudDialogflowCxV3Match**](GoogleCloudDialogflowCxV3Match.md) |  | [optional] 
**parameters** | **{String: Object}** | The collected session parameters. Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs: * MapKey type: string * MapKey value: parameter name * MapValue type: If parameter&#39;s entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map. * MapValue value: If parameter&#39;s entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value. | [optional] 
**responseMessages** | [**[GoogleCloudDialogflowCxV3ResponseMessage]**](GoogleCloudDialogflowCxV3ResponseMessage.md) | The list of rich messages returned to the client. Responses vary from simple text messages to more sophisticated, structured payloads used to drive complex logic. | [optional] 
**sentimentAnalysisResult** | [**GoogleCloudDialogflowCxV3SentimentAnalysisResult**](GoogleCloudDialogflowCxV3SentimentAnalysisResult.md) |  | [optional] 
**text** | **String** | If natural language text was provided as input, this field will contain a copy of the text. | [optional] 
**transcript** | **String** | If natural language speech audio was provided as input, this field will contain the transcript for the audio. | [optional] 
**triggerEvent** | **String** | If an event was provided as input, this field will contain the name of the event. | [optional] 
**triggerIntent** | **String** | If an intent was provided as input, this field will contain a copy of the intent identifier. Format: &#x60;projects//locations//agents//intents/&#x60;. | [optional] 
**webhookPayloads** | **[{String: Object}]** | The list of webhook payload in WebhookResponse.payload, in the order of call sequence. If some webhook call fails or doesn&#39;t return any payload, an empty &#x60;Struct&#x60; would be used instead. | [optional] 
**webhookStatuses** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | The list of webhook call status in the order of call sequence. | [optional] 


