# CloudMonitoringApi.TimeSeries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**MonitoredResourceMetadata**](MonitoredResourceMetadata.md) |  | [optional] 
**metric** | [**Metric**](Metric.md) |  | [optional] 
**metricKind** | **String** | The metric kind of the time series. When listing time series, this metric kind might be different from the metric kind of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the metric kind of the associated metric. If the associated metric&#39;s descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either GAUGE (the default) or CUMULATIVE. | [optional] 
**points** | [**[Point]**](Point.md) | The data points of this time series. When listing time series, points are returned in reverse time order.When creating a time series, this field must contain exactly one point and the point&#39;s type must be the same as the value type of the associated metric. If the associated metric&#39;s descriptor must be auto-created, then the value type of the descriptor is determined by the point&#39;s type, which must be BOOL, INT64, DOUBLE, or DISTRIBUTION. | [optional] 
**resource** | [**MonitoredResource**](MonitoredResource.md) |  | [optional] 
**unit** | **String** | The units in which the metric value is reported. It is only applicable if the value_type is INT64, DOUBLE, or DISTRIBUTION. The unit defines the representation of the stored metric values. | [optional] 
**valueType** | **String** | The value type of the time series. When listing time series, this value type might be different from the value type of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the type of the data in the points field. | [optional] 



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




