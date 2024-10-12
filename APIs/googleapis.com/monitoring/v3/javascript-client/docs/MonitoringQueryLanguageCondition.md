# CloudMonitoringApi.MonitoringQueryLanguageCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **String** | The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. | [optional] 
**evaluationMissingData** | **String** | A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. | [optional] 
**query** | **String** | Monitoring Query Language (https://cloud.google.com/monitoring/mql) query that outputs a boolean stream. | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 



## Enum: EvaluationMissingDataEnum


* `UNSPECIFIED` (value: `"EVALUATION_MISSING_DATA_UNSPECIFIED"`)

* `INACTIVE` (value: `"EVALUATION_MISSING_DATA_INACTIVE"`)

* `ACTIVE` (value: `"EVALUATION_MISSING_DATA_ACTIVE"`)

* `NO_OP` (value: `"EVALUATION_MISSING_DATA_NO_OP"`)




