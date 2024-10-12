

# GoogleCloudDialogflowCxV3RestoreAgentRequest

The request message for Agents.RestoreAgent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentContent** | **byte[]** | Uncompressed raw byte content for agent. |  [optional] |
|**agentUri** | **String** | The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to restore agent from. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a read operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). |  [optional] |
|**gitSource** | [**GoogleCloudDialogflowCxV3RestoreAgentRequestGitSource**](GoogleCloudDialogflowCxV3RestoreAgentRequestGitSource.md) |  |  [optional] |
|**restoreOption** | [**RestoreOptionEnum**](#RestoreOptionEnum) | Agent restore mode. If not specified, &#x60;KEEP&#x60; is assumed. |  [optional] |



## Enum: RestoreOptionEnum

| Name | Value |
|---- | -----|
| RESTORE_OPTION_UNSPECIFIED | &quot;RESTORE_OPTION_UNSPECIFIED&quot; |
| KEEP | &quot;KEEP&quot; |
| FALLBACK | &quot;FALLBACK&quot; |



