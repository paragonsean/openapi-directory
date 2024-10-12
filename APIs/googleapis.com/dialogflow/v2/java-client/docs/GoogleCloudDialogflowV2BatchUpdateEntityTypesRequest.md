

# GoogleCloudDialogflowV2BatchUpdateEntityTypesRequest

The request message for EntityTypes.BatchUpdateEntityTypes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityTypeBatchInline** | [**GoogleCloudDialogflowV2EntityTypeBatch**](GoogleCloudDialogflowV2EntityTypeBatch.md) |  |  [optional] |
|**entityTypeBatchUri** | **String** | The URI to a Google Cloud Storage file containing entity types to update or create. The file format can either be a serialized proto (of EntityBatch type) or a JSON object. Note: The URI must start with \&quot;gs://\&quot;. |  [optional] |
|**languageCode** | **String** | Optional. The language used to access language-specific data. If not specified, the agent&#39;s default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity). |  [optional] |
|**updateMask** | **String** | Optional. The mask to control which fields get updated. |  [optional] |



