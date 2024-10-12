# DataflowApi.WorkItemServiceState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completeWorkStatus** | [**Status**](Status.md) |  | [optional] 
**harnessData** | **{String: Object}** | Other data returned by the service, specific to the particular worker harness. | [optional] 
**hotKeyDetection** | [**HotKeyDetection**](HotKeyDetection.md) |  | [optional] 
**leaseExpireTime** | **String** | Time at which the current lease will expire. | [optional] 
**metricShortId** | [**[MetricShortId]**](MetricShortId.md) | The short ids that workers should use in subsequent metric updates. Workers should strive to use short ids whenever possible, but it is ok to request the short_id again if a worker lost track of it (e.g. if the worker is recovering from a crash). NOTE: it is possible that the response may have short ids for a subset of the metrics. | [optional] 
**nextReportIndex** | **String** | The index value to use for the next report sent by the worker. Note: If the report call fails for whatever reason, the worker should reuse this index for subsequent report attempts. | [optional] 
**reportStatusInterval** | **String** | New recommended reporting interval. | [optional] 
**splitRequest** | [**ApproximateSplitRequest**](ApproximateSplitRequest.md) |  | [optional] 
**suggestedStopPoint** | [**ApproximateProgress**](ApproximateProgress.md) |  | [optional] 
**suggestedStopPosition** | [**Position**](Position.md) |  | [optional] 


