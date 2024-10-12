

# PlansListMetricDefinitions200ResponseValueInner

Metric Definition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricAvailabilities** | [**List&lt;PlansListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner&gt;**](PlansListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner.md) | List of metric definitions. |  [optional] |
|**name** | **String** | Metric definition name. |  [optional] |
|**primaryAggregationType** | [**PrimaryAggregationTypeEnum**](#PrimaryAggregationTypeEnum) | The primary aggregation type for resource metric. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | The resource metric unit. |  [optional] |



## Enum: PrimaryAggregationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AVERAGE | &quot;Average&quot; |
| TOTAL | &quot;Total&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| LAST | &quot;Last&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



