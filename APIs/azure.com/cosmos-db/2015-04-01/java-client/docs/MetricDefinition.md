

# MetricDefinition

The definition of a metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricAvailabilities** | [**List&lt;MetricAvailability&gt;**](MetricAvailability.md) | The list of metric availabilities for the account. |  [optional] [readonly] |
|**name** | [**MetricName**](MetricName.md) |  |  [optional] |
|**primaryAggregationType** | [**PrimaryAggregationTypeEnum**](#PrimaryAggregationTypeEnum) | The primary aggregation type of the metric. |  [optional] [readonly] |
|**resourceUri** | **String** | The resource uri of the database. |  [optional] [readonly] |
|**unit** | **UnitType** |  |  [optional] |



## Enum: PrimaryAggregationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AVERAGE | &quot;Average&quot; |
| TOTAL | &quot;Total&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| LAST | &quot;Last&quot; |



