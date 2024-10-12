# BigQueryApi.QueryTimelineSample

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeUnits** | **String** | Total number of active workers. This does not correspond directly to slot usage. This is the largest value observed since the last sample. | [optional] 
**completedUnits** | **String** | Total parallel units of work completed by this query. | [optional] 
**elapsedMs** | **String** | Milliseconds elapsed since the start of query execution. | [optional] 
**estimatedRunnableUnits** | **String** | Units of work that can be scheduled immediately. Providing additional slots for these units of work will accelerate the query, if no other query in the reservation needs additional slots. | [optional] 
**pendingUnits** | **String** | Total units of work remaining for the query. This number can be revised (increased or decreased) while the query is running. | [optional] 
**totalSlotMs** | **String** | Cumulative slot-ms consumed by the query. | [optional] 


