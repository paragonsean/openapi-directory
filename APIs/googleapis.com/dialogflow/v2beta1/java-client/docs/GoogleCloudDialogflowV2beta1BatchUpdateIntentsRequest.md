

# GoogleCloudDialogflowV2beta1BatchUpdateIntentsRequest

The request message for Intents.BatchUpdateIntents.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intentBatchInline** | [**GoogleCloudDialogflowV2beta1IntentBatch**](GoogleCloudDialogflowV2beta1IntentBatch.md) |  |  [optional] |
|**intentBatchUri** | **String** | The URI to a Google Cloud Storage file containing intents to update or create. The file format can either be a serialized proto (of IntentBatch type) or JSON object. Note: The URI must start with \&quot;gs://\&quot;. |  [optional] |
|**intentView** | [**IntentViewEnum**](#IntentViewEnum) | Optional. The resource view to apply to the returned intent. |  [optional] |
|**languageCode** | **String** | Optional. The language used to access language-specific data. If not specified, the agent&#39;s default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity). |  [optional] |
|**updateMask** | **String** | Optional. The mask to control which fields get updated. |  [optional] |



## Enum: IntentViewEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INTENT_VIEW_UNSPECIFIED&quot; |
| FULL | &quot;INTENT_VIEW_FULL&quot; |



