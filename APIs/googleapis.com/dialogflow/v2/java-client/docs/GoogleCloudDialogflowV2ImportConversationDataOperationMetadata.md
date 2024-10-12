

# GoogleCloudDialogflowV2ImportConversationDataOperationMetadata

Metadata for a ConversationDatasets.ImportConversationData operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationDataset** | **String** | The resource name of the imported conversation dataset. Format: &#x60;projects//locations//conversationDatasets/&#x60; |  [optional] |
|**createTime** | **String** | Timestamp when import conversation data request was created. The time is measured on server side. |  [optional] |
|**partialFailures** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | Partial failures are failures that don&#39;t fail the whole long running operation, e.g. single files that couldn&#39;t be read. |  [optional] |



