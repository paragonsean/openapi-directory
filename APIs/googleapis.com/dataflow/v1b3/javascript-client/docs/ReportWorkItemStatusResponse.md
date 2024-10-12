# DataflowApi.ReportWorkItemStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unifiedWorkerResponse** | **{String: Object}** | Untranslated bag-of-bytes WorkProgressUpdateResponse for UnifiedWorker. | [optional] 
**workItemServiceStates** | [**[WorkItemServiceState]**](WorkItemServiceState.md) | A set of messages indicating the service-side state for each WorkItem whose status was reported, in the same order as the WorkItemStatus messages in the ReportWorkItemStatusRequest which resulting in this response. | [optional] 


