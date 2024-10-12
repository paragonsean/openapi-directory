

# GoogleCloudDialogflowCxV3beta1WebhookRequest

The request message for a webhook call. The request is sent as a JSON object and the field names will be presented in camel cases. You may see undocumented fields in an actual request. These fields are used internally by Dialogflow and should be ignored.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detectIntentResponseId** | **String** | Always present. The unique identifier of the DetectIntentResponse that will be returned to the API caller. |  [optional] |
|**dtmfDigits** | **String** | If DTMF was provided as input, this field will contain the DTMF digits. |  [optional] |
|**fulfillmentInfo** | [**GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo**](GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo.md) |  |  [optional] |
|**intentInfo** | [**GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo**](GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo.md) |  |  [optional] |
|**languageCode** | **String** | The language code specified in the original request. |  [optional] |
|**messages** | [**List&lt;GoogleCloudDialogflowCxV3beta1ResponseMessage&gt;**](GoogleCloudDialogflowCxV3beta1ResponseMessage.md) | The list of rich message responses to present to the user. Webhook can choose to append or replace this list in WebhookResponse.fulfillment_response; |  [optional] |
|**pageInfo** | [**GoogleCloudDialogflowCxV3beta1PageInfo**](GoogleCloudDialogflowCxV3beta1PageInfo.md) |  |  [optional] |
|**payload** | **Map&lt;String, Object&gt;** | Custom data set in QueryParameters.payload. |  [optional] |
|**sentimentAnalysisResult** | [**GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResult**](GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResult.md) |  |  [optional] |
|**sessionInfo** | [**GoogleCloudDialogflowCxV3beta1SessionInfo**](GoogleCloudDialogflowCxV3beta1SessionInfo.md) |  |  [optional] |
|**text** | **String** | If natural language text was provided as input, this field will contain a copy of the text. |  [optional] |
|**transcript** | **String** | If natural language speech audio was provided as input, this field will contain the transcript for the audio. |  [optional] |
|**triggerEvent** | **String** | If an event was provided as input, this field will contain the name of the event. |  [optional] |
|**triggerIntent** | **String** | If an intent was provided as input, this field will contain a copy of the intent identifier. Format: &#x60;projects//locations//agents//intents/&#x60;. |  [optional] |



