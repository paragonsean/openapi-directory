

# GoogleCloudDialogflowCxV3beta1ImportIntentsRequest

The request message for Intents.ImportIntents.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intentsContent** | [**GoogleCloudDialogflowCxV3beta1InlineSource**](GoogleCloudDialogflowCxV3beta1InlineSource.md) |  |  [optional] |
|**intentsUri** | **String** | The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import intents from. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a read operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). |  [optional] |
|**mergeOption** | [**MergeOptionEnum**](#MergeOptionEnum) | Merge option for importing intents. If not specified, &#x60;REJECT&#x60; is assumed. |  [optional] |



## Enum: MergeOptionEnum

| Name | Value |
|---- | -----|
| MERGE_OPTION_UNSPECIFIED | &quot;MERGE_OPTION_UNSPECIFIED&quot; |
| REJECT | &quot;REJECT&quot; |
| REPLACE | &quot;REPLACE&quot; |
| MERGE | &quot;MERGE&quot; |
| RENAME | &quot;RENAME&quot; |
| REPORT_CONFLICT | &quot;REPORT_CONFLICT&quot; |
| KEEP | &quot;KEEP&quot; |



