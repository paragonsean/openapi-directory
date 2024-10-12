

# ValueDescriptor

A descriptor for the value columns in a data point.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The value key. |  [optional] |
|**metricKind** | [**MetricKindEnum**](#MetricKindEnum) | The value stream kind. |  [optional] |
|**unit** | **String** | The unit in which time_series point values are reported. unit follows the UCUM format for units as seen in https://unitsofmeasure.org/ucum.html. unit is only valid if value_type is INTEGER, DOUBLE, DISTRIBUTION. |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | The value type. |  [optional] |



## Enum: MetricKindEnum

| Name | Value |
|---- | -----|
| METRIC_KIND_UNSPECIFIED | &quot;METRIC_KIND_UNSPECIFIED&quot; |
| GAUGE | &quot;GAUGE&quot; |
| DELTA | &quot;DELTA&quot; |
| CUMULATIVE | &quot;CUMULATIVE&quot; |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| VALUE_TYPE_UNSPECIFIED | &quot;VALUE_TYPE_UNSPECIFIED&quot; |
| BOOL | &quot;BOOL&quot; |
| INT64 | &quot;INT64&quot; |
| DOUBLE | &quot;DOUBLE&quot; |
| STRING | &quot;STRING&quot; |
| DISTRIBUTION | &quot;DISTRIBUTION&quot; |
| MONEY | &quot;MONEY&quot; |



