# CloudMonitoringApi.ValueDescriptor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | The value key. | [optional] 
**metricKind** | **String** | The value stream kind. | [optional] 
**unit** | **String** | The unit in which time_series point values are reported. unit follows the UCUM format for units as seen in https://unitsofmeasure.org/ucum.html. unit is only valid if value_type is INTEGER, DOUBLE, DISTRIBUTION. | [optional] 
**valueType** | **String** | The value type. | [optional] 



## Enum: MetricKindEnum


* `METRIC_KIND_UNSPECIFIED` (value: `"METRIC_KIND_UNSPECIFIED"`)

* `GAUGE` (value: `"GAUGE"`)

* `DELTA` (value: `"DELTA"`)

* `CUMULATIVE` (value: `"CUMULATIVE"`)





## Enum: ValueTypeEnum


* `VALUE_TYPE_UNSPECIFIED` (value: `"VALUE_TYPE_UNSPECIFIED"`)

* `BOOL` (value: `"BOOL"`)

* `INT64` (value: `"INT64"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `STRING` (value: `"STRING"`)

* `DISTRIBUTION` (value: `"DISTRIBUTION"`)

* `MONEY` (value: `"MONEY"`)




