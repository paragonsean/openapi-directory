

# GoogleCloudDialogflowCxV3ExportAgentRequest

The request message for Agents.ExportAgent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentUri** | **String** | Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the agent to. The format of this URI must be &#x60;gs:///&#x60;. If left unspecified, the serialized agent is returned inline. Dialogflow performs a write operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). |  [optional] |
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | Optional. The data format of the exported agent. If not specified, &#x60;BLOB&#x60; is assumed. |  [optional] |
|**environment** | **String** | Optional. Environment name. If not set, draft environment is assumed. Format: &#x60;projects//locations//agents//environments/&#x60;. |  [optional] |
|**gitDestination** | [**GoogleCloudDialogflowCxV3ExportAgentRequestGitDestination**](GoogleCloudDialogflowCxV3ExportAgentRequestGitDestination.md) |  |  [optional] |
|**includeBigqueryExportSettings** | **Boolean** | Optional. Whether to include BigQuery Export setting. |  [optional] |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| DATA_FORMAT_UNSPECIFIED | &quot;DATA_FORMAT_UNSPECIFIED&quot; |
| BLOB | &quot;BLOB&quot; |
| JSON_PACKAGE | &quot;JSON_PACKAGE&quot; |



