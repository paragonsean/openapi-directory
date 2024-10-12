# DataflowApi.ReportWorkItemStatusRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentWorkerTime** | **String** | The current timestamp at the worker. | [optional] 
**location** | **String** | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the WorkItem&#39;s job. | [optional] 
**unifiedWorkerRequest** | **{String: Object}** | Untranslated bag-of-bytes WorkProgressUpdateRequest from UnifiedWorker. | [optional] 
**workItemStatuses** | [**[WorkItemStatus]**](WorkItemStatus.md) | The order is unimportant, except that the order of the WorkItemServiceState messages in the ReportWorkItemStatusResponse corresponds to the order of WorkItemStatus messages here. | [optional] 
**workerId** | **String** | The ID of the worker reporting the WorkItem status. If this does not match the ID of the worker which the Dataflow service believes currently has the lease on the WorkItem, the report will be dropped (with an error response). | [optional] 


