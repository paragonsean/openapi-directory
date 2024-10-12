

# WorkItem

WorkItem represents basic information about a WorkItem to be executed in the cloud.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_configuration** | **String** | Work item-specific configuration as an opaque blob. |  [optional] |
|**id** | **String** | Identifies this WorkItem. |  [optional] |
|**initialReportIndex** | **String** | The initial index to use when reporting the status of the WorkItem. |  [optional] |
|**jobId** | **String** | Identifies the workflow job this WorkItem belongs to. |  [optional] |
|**leaseExpireTime** | **String** | Time when the lease on this Work will expire. |  [optional] |
|**mapTask** | [**MapTask**](MapTask.md) |  |  [optional] |
|**packages** | [**List&lt;ModelPackage&gt;**](ModelPackage.md) | Any required packages that need to be fetched in order to execute this WorkItem. |  [optional] |
|**projectId** | **String** | Identifies the cloud project this WorkItem belongs to. |  [optional] |
|**reportStatusInterval** | **String** | Recommended reporting interval. |  [optional] |
|**seqMapTask** | [**SeqMapTask**](SeqMapTask.md) |  |  [optional] |
|**shellTask** | [**ShellTask**](ShellTask.md) |  |  [optional] |
|**sourceOperationTask** | [**SourceOperationRequest**](SourceOperationRequest.md) |  |  [optional] |
|**streamingComputationTask** | [**StreamingComputationTask**](StreamingComputationTask.md) |  |  [optional] |
|**streamingConfigTask** | [**StreamingConfigTask**](StreamingConfigTask.md) |  |  [optional] |
|**streamingSetupTask** | [**StreamingSetupTask**](StreamingSetupTask.md) |  |  [optional] |



