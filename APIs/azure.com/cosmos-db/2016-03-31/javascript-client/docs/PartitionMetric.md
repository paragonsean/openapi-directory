# CosmosDb.PartitionMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitionId** | **String** | The partition id (GUID identifier) of the metric values. | [optional] [readonly] 
**partitionKeyRangeId** | **String** | The partition key range id (integer identifier) of the metric values. | [optional] [readonly] 
**endTime** | **Date** | The end time for the metric (ISO-8601 format). | [optional] [readonly] 
**metricValues** | [**[MetricValue]**](MetricValue.md) | The metric values for the specified time window and timestep. | [optional] [readonly] 
**name** | [**MetricName**](MetricName.md) |  | [optional] 
**startTime** | **Date** | The start time for the metric (ISO-8601 format). | [optional] [readonly] 
**timeGrain** | **String** | The time grain to be used to summarize the metric values. | [optional] [readonly] 
**unit** | [**UnitType**](UnitType.md) |  | [optional] 


