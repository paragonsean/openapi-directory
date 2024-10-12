

# GoogleCloudDialogflowCxV3ImportEntityTypesRequest

The request message for EntityTypes.ImportEntityTypes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityTypesContent** | [**GoogleCloudDialogflowCxV3InlineSource**](GoogleCloudDialogflowCxV3InlineSource.md) |  |  [optional] |
|**entityTypesUri** | **String** | The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import entity types from. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a read operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). |  [optional] |
|**mergeOption** | [**MergeOptionEnum**](#MergeOptionEnum) | Required. Merge option for importing entity types. |  [optional] |
|**targetEntityType** | **String** | Optional. The target entity type to import into. Format: &#x60;projects//locations//agents//entity_types/&#x60;. If set, there should be only one entity type included in entity_types, of which the type should match the type of the target entity type. All entities in the imported entity type will be added to the target entity type. |  [optional] |



## Enum: MergeOptionEnum

| Name | Value |
|---- | -----|
| MERGE_OPTION_UNSPECIFIED | &quot;MERGE_OPTION_UNSPECIFIED&quot; |
| REPLACE | &quot;REPLACE&quot; |
| MERGE | &quot;MERGE&quot; |
| RENAME | &quot;RENAME&quot; |
| REPORT_CONFLICT | &quot;REPORT_CONFLICT&quot; |
| KEEP | &quot;KEEP&quot; |



