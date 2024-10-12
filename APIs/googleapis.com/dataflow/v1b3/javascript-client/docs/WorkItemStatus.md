# DataflowApi.WorkItemStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **Boolean** | True if the WorkItem was completed (successfully or unsuccessfully). | [optional] 
**counterUpdates** | [**[CounterUpdate]**](CounterUpdate.md) | Worker output counters for this WorkItem. | [optional] 
**dynamicSourceSplit** | [**DynamicSourceSplit**](DynamicSourceSplit.md) |  | [optional] 
**errors** | [**[Status]**](Status.md) | Specifies errors which occurred during processing. If errors are provided, and completed &#x3D; true, then the WorkItem is considered to have failed. | [optional] 
**metricUpdates** | [**[MetricUpdate]**](MetricUpdate.md) | DEPRECATED in favor of counter_updates. | [optional] 
**progress** | [**ApproximateProgress**](ApproximateProgress.md) |  | [optional] 
**reportIndex** | **String** | The report index. When a WorkItem is leased, the lease will contain an initial report index. When a WorkItem&#39;s status is reported to the system, the report should be sent with that report index, and the response will contain the index the worker should use for the next report. Reports received with unexpected index values will be rejected by the service. In order to preserve idempotency, the worker should not alter the contents of a report, even if the worker must submit the same report multiple times before getting back a response. The worker should not submit a subsequent report until the response for the previous report had been received from the service. | [optional] 
**reportedProgress** | [**ApproximateReportedProgress**](ApproximateReportedProgress.md) |  | [optional] 
**requestedLeaseDuration** | **String** | Amount of time the worker requests for its lease. | [optional] 
**sourceFork** | [**SourceFork**](SourceFork.md) |  | [optional] 
**sourceOperationResponse** | [**SourceOperationResponse**](SourceOperationResponse.md) |  | [optional] 
**stopPosition** | [**Position**](Position.md) |  | [optional] 
**totalThrottlerWaitTimeSeconds** | **Number** | Total time the worker spent being throttled by external systems. | [optional] 
**workItemId** | **String** | Identifies the WorkItem. | [optional] 


