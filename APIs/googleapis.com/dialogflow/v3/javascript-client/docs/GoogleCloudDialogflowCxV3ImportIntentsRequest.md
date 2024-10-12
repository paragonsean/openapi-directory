# DialogflowApi.GoogleCloudDialogflowCxV3ImportIntentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intentsContent** | [**GoogleCloudDialogflowCxV3InlineSource**](GoogleCloudDialogflowCxV3InlineSource.md) |  | [optional] 
**intentsUri** | **String** | The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import intents from. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a read operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). | [optional] 
**mergeOption** | **String** | Merge option for importing intents. If not specified, &#x60;REJECT&#x60; is assumed. | [optional] 



## Enum: MergeOptionEnum


* `MERGE_OPTION_UNSPECIFIED` (value: `"MERGE_OPTION_UNSPECIFIED"`)

* `REJECT` (value: `"REJECT"`)

* `REPLACE` (value: `"REPLACE"`)

* `MERGE` (value: `"MERGE"`)

* `RENAME` (value: `"RENAME"`)

* `REPORT_CONFLICT` (value: `"REPORT_CONFLICT"`)

* `KEEP` (value: `"KEEP"`)




