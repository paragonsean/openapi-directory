# DialogflowApi.GoogleCloudDialogflowV2beta1WebhookResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endInteraction** | **Boolean** | Optional. Indicates that this intent ends an interaction. Some integrations (e.g., Actions on Google or Dialogflow phone gateway) use this information to close interaction with an end user. Default is false. | [optional] 
**followupEventInput** | [**GoogleCloudDialogflowV2beta1EventInput**](GoogleCloudDialogflowV2beta1EventInput.md) |  | [optional] 
**fulfillmentMessages** | [**[GoogleCloudDialogflowV2beta1IntentMessage]**](GoogleCloudDialogflowV2beta1IntentMessage.md) | Optional. The rich response messages intended for the end-user. When provided, Dialogflow uses this field to populate QueryResult.fulfillment_messages sent to the integration or API caller. | [optional] 
**fulfillmentText** | **String** | Optional. The text response message intended for the end-user. It is recommended to use &#x60;fulfillment_messages.text.text[0]&#x60; instead. When provided, Dialogflow uses this field to populate QueryResult.fulfillment_text sent to the integration or API caller. | [optional] 
**liveAgentHandoff** | **Boolean** | Indicates that a live agent should be brought in to handle the interaction with the user. In most cases, when you set this flag to true, you would also want to set end_interaction to true as well. Default is false. | [optional] 
**outputContexts** | [**[GoogleCloudDialogflowV2beta1Context]**](GoogleCloudDialogflowV2beta1Context.md) | Optional. The collection of output contexts that will overwrite currently active contexts for the session and reset their lifespans. When provided, Dialogflow uses this field to populate QueryResult.output_contexts sent to the integration or API caller. | [optional] 
**payload** | **{String: Object}** | Optional. This field can be used to pass custom data from your webhook to the integration or API caller. Arbitrary JSON objects are supported. When provided, Dialogflow uses this field to populate QueryResult.webhook_payload sent to the integration or API caller. This field is also used by the [Google Assistant integration](https://cloud.google.com/dialogflow/docs/integrations/aog) for rich response messages. See the format definition at [Google Assistant Dialogflow webhook format](https://developers.google.com/assistant/actions/build/json/dialogflow-webhook-json) | [optional] 
**sessionEntityTypes** | [**[GoogleCloudDialogflowV2beta1SessionEntityType]**](GoogleCloudDialogflowV2beta1SessionEntityType.md) | Optional. Additional session entity types to replace or extend developer entity types with. The entity synonyms apply to all languages and persist for the session. Setting this data from a webhook overwrites the session entity types that have been set using &#x60;detectIntent&#x60;, &#x60;streamingDetectIntent&#x60; or SessionEntityType management methods. | [optional] 
**source** | **String** | Optional. A custom field used to identify the webhook source. Arbitrary strings are supported. When provided, Dialogflow uses this field to populate QueryResult.webhook_source sent to the integration or API caller. | [optional] 


