# AzureSqlDatabase.Metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The end time for the metric (ISO-8601 format). | [optional] [readonly] 
**metricValues** | [**[MetricValue]**](MetricValue.md) | The metric values for the specified time window and timestep. | [optional] [readonly] 
**name** | [**MetricName**](MetricName.md) |  | [optional] 
**startTime** | **Date** | The start time for the metric (ISO-8601 format). | [optional] [readonly] 
**timeGrain** | **String** | The time step to be used to summarize the metric values. | [optional] [readonly] 
**unit** | **String** | The unit of the metric. | [optional] [readonly] 



## Enum: UnitEnum


* `count` (value: `"count"`)

* `bytes` (value: `"bytes"`)

* `seconds` (value: `"seconds"`)

* `percent` (value: `"percent"`)

* `countPerSecond` (value: `"countPerSecond"`)

* `bytesPerSecond` (value: `"bytesPerSecond"`)




