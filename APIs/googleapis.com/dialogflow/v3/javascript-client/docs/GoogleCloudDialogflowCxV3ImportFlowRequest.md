# DialogflowApi.GoogleCloudDialogflowCxV3ImportFlowRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flowContent** | **Blob** | Uncompressed raw byte content for flow. | [optional] 
**flowImportStrategy** | [**GoogleCloudDialogflowCxV3FlowImportStrategy**](GoogleCloudDialogflowCxV3FlowImportStrategy.md) |  | [optional] 
**flowUri** | **String** | The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import flow from. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a read operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). | [optional] 
**importOption** | **String** | Flow import mode. If not specified, &#x60;KEEP&#x60; is assumed. | [optional] 



## Enum: ImportOptionEnum


* `IMPORT_OPTION_UNSPECIFIED` (value: `"IMPORT_OPTION_UNSPECIFIED"`)

* `KEEP` (value: `"KEEP"`)

* `FALLBACK` (value: `"FALLBACK"`)




