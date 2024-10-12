

# ReportWorkItemStatusResponse

Response from a request to report the status of WorkItems.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**unifiedWorkerResponse** | **Map&lt;String, Object&gt;** | Untranslated bag-of-bytes WorkProgressUpdateResponse for UnifiedWorker. |  [optional] |
|**workItemServiceStates** | [**List&lt;WorkItemServiceState&gt;**](WorkItemServiceState.md) | A set of messages indicating the service-side state for each WorkItem whose status was reported, in the same order as the WorkItemStatus messages in the ReportWorkItemStatusRequest which resulting in this response. |  [optional] |



