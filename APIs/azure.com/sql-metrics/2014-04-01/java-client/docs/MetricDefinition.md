

# MetricDefinition

A database metric definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricAvailabilities** | [**List&lt;MetricAvailability&gt;**](MetricAvailability.md) | The list of database metric availabilities for the metric. |  [optional] [readonly] |
|**name** | [**MetricName**](MetricName.md) |  |  [optional] |
|**primaryAggregationType** | [**PrimaryAggregationTypeEnum**](#PrimaryAggregationTypeEnum) | The primary aggregation type defining how metric values are displayed. |  [optional] [readonly] |
|**resourceUri** | **String** | The resource uri of the database. |  [optional] [readonly] |
|**unit** | [**UnitEnum**](#UnitEnum) | The unit of the metric. |  [optional] [readonly] |



## Enum: PrimaryAggregationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AVERAGE | &quot;Average&quot; |
| COUNT | &quot;Count&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| TOTAL | &quot;Total&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| PERCENT | &quot;Percent&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



