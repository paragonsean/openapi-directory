

# GoogleCloudDialogflowV2WebhookResponse

The response message for a webhook call. This response is validated by the Dialogflow server. If validation fails, an error will be returned in the QueryResult.diagnostic_info field. Setting JSON fields to an empty value with the wrong type is a common error. To avoid this error: - Use `\"\"` for empty strings - Use `{}` or `null` for empty objects - Use `[]` or `null` for empty arrays For more information, see the [Protocol Buffers Language Guide](https://developers.google.com/protocol-buffers/docs/proto3#json).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**followupEventInput** | [**GoogleCloudDialogflowV2EventInput**](GoogleCloudDialogflowV2EventInput.md) |  |  [optional] |
|**fulfillmentMessages** | [**List&lt;GoogleCloudDialogflowV2IntentMessage&gt;**](GoogleCloudDialogflowV2IntentMessage.md) | Optional. The rich response messages intended for the end-user. When provided, Dialogflow uses this field to populate QueryResult.fulfillment_messages sent to the integration or API caller. |  [optional] |
|**fulfillmentText** | **String** | Optional. The text response message intended for the end-user. It is recommended to use &#x60;fulfillment_messages.text.text[0]&#x60; instead. When provided, Dialogflow uses this field to populate QueryResult.fulfillment_text sent to the integration or API caller. |  [optional] |
|**outputContexts** | [**List&lt;GoogleCloudDialogflowV2Context&gt;**](GoogleCloudDialogflowV2Context.md) | Optional. The collection of output contexts that will overwrite currently active contexts for the session and reset their lifespans. When provided, Dialogflow uses this field to populate QueryResult.output_contexts sent to the integration or API caller. |  [optional] |
|**payload** | **Map&lt;String, Object&gt;** | Optional. This field can be used to pass custom data from your webhook to the integration or API caller. Arbitrary JSON objects are supported. When provided, Dialogflow uses this field to populate QueryResult.webhook_payload sent to the integration or API caller. This field is also used by the [Google Assistant integration](https://cloud.google.com/dialogflow/docs/integrations/aog) for rich response messages. See the format definition at [Google Assistant Dialogflow webhook format](https://developers.google.com/assistant/actions/build/json/dialogflow-webhook-json) |  [optional] |
|**sessionEntityTypes** | [**List&lt;GoogleCloudDialogflowV2SessionEntityType&gt;**](GoogleCloudDialogflowV2SessionEntityType.md) | Optional. Additional session entity types to replace or extend developer entity types with. The entity synonyms apply to all languages and persist for the session. Setting this data from a webhook overwrites the session entity types that have been set using &#x60;detectIntent&#x60;, &#x60;streamingDetectIntent&#x60; or SessionEntityType management methods. |  [optional] |
|**source** | **String** | Optional. A custom field used to identify the webhook source. Arbitrary strings are supported. When provided, Dialogflow uses this field to populate QueryResult.webhook_source sent to the integration or API caller. |  [optional] |



