# DialogflowApi.GoogleCloudDialogflowCxV3Fulfillment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedSettings** | [**GoogleCloudDialogflowCxV3AdvancedSettings**](GoogleCloudDialogflowCxV3AdvancedSettings.md) |  | [optional] 
**conditionalCases** | [**[GoogleCloudDialogflowCxV3FulfillmentConditionalCases]**](GoogleCloudDialogflowCxV3FulfillmentConditionalCases.md) | Conditional cases for this fulfillment. | [optional] 
**enableGenerativeFallback** | **Boolean** | If the flag is true, the agent will utilize LLM to generate a text response. If LLM generation fails, the defined responses in the fulfillment will be respected. This flag is only useful for fulfillments associated with no-match event handlers. | [optional] 
**messages** | [**[GoogleCloudDialogflowCxV3ResponseMessage]**](GoogleCloudDialogflowCxV3ResponseMessage.md) | The list of rich message responses to present to the user. | [optional] 
**returnPartialResponses** | **Boolean** | Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. | [optional] 
**setParameterActions** | [**[GoogleCloudDialogflowCxV3FulfillmentSetParameterAction]**](GoogleCloudDialogflowCxV3FulfillmentSetParameterAction.md) | Set parameter values before executing the webhook. | [optional] 
**tag** | **String** | The value of this field will be populated in the WebhookRequest &#x60;fulfillmentInfo.tag&#x60; field by Dialogflow when the associated webhook is called. The tag is typically used by the webhook service to identify which fulfillment is being called, but it could be used for other purposes. This field is required if &#x60;webhook&#x60; is specified. | [optional] 
**webhook** | **String** | The webhook to call. Format: &#x60;projects//locations//agents//webhooks/&#x60;. | [optional] 


