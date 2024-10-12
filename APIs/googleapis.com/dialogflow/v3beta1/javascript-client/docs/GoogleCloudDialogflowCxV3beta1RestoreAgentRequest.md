# DialogflowApi.GoogleCloudDialogflowCxV3beta1RestoreAgentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentContent** | **Blob** | Uncompressed raw byte content for agent. | [optional] 
**agentUri** | **String** | The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to restore agent from. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a read operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). | [optional] 
**gitSource** | [**GoogleCloudDialogflowCxV3beta1RestoreAgentRequestGitSource**](GoogleCloudDialogflowCxV3beta1RestoreAgentRequestGitSource.md) |  | [optional] 
**restoreOption** | **String** | Agent restore mode. If not specified, &#x60;KEEP&#x60; is assumed. | [optional] 



## Enum: RestoreOptionEnum


* `RESTORE_OPTION_UNSPECIFIED` (value: `"RESTORE_OPTION_UNSPECIFIED"`)

* `KEEP` (value: `"KEEP"`)

* `FALLBACK` (value: `"FALLBACK"`)




