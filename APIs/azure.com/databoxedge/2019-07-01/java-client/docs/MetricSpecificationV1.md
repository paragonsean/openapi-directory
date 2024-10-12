

# MetricSpecificationV1

Metric specification version 1.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationType** | [**AggregationTypeEnum**](#AggregationTypeEnum) | Metric aggregation type. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | Metric category. |  [optional] |
|**dimensions** | [**List&lt;MetricDimensionV1&gt;**](MetricDimensionV1.md) | Metric dimensions, other than default dimension which is resource. |  [optional] |
|**displayDescription** | **String** | Description of the metric to be displayed. |  [optional] |
|**displayName** | **String** | Display name of the metric. |  [optional] |
|**fillGapWithZero** | **Boolean** | Set true to fill the gaps with zero. |  [optional] |
|**name** | **String** | Name of the metric. |  [optional] |
|**resourceIdDimensionNameOverride** | **String** | Resource name override. |  [optional] |
|**supportedAggregationTypes** | [**List&lt;SupportedAggregationTypesEnum&gt;**](#List&lt;SupportedAggregationTypesEnum&gt;) | Support metric aggregation type. |  [optional] |
|**supportedTimeGrainTypes** | [**List&lt;SupportedTimeGrainTypesEnum&gt;**](#List&lt;SupportedTimeGrainTypesEnum&gt;) | Support granularity of metrics. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | Metric units. |  [optional] |



## Enum: AggregationTypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| NONE | &quot;None&quot; |
| AVERAGE | &quot;Average&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| TOTAL | &quot;Total&quot; |
| COUNT | &quot;Count&quot; |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| CAPACITY | &quot;Capacity&quot; |
| TRANSACTION | &quot;Transaction&quot; |



## Enum: List&lt;SupportedAggregationTypesEnum&gt;

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| NONE | &quot;None&quot; |
| AVERAGE | &quot;Average&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| TOTAL | &quot;Total&quot; |
| COUNT | &quot;Count&quot; |



## Enum: List&lt;SupportedTimeGrainTypesEnum&gt;

| Name | Value |
|---- | -----|
| PT1_M | &quot;PT1M&quot; |
| PT5_M | &quot;PT5M&quot; |
| PT15_M | &quot;PT15M&quot; |
| PT30_M | &quot;PT30M&quot; |
| PT1_H | &quot;PT1H&quot; |
| PT6_H | &quot;PT6H&quot; |
| PT12_H | &quot;PT12H&quot; |
| PT1_D | &quot;PT1D&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| PERCENT | &quot;Percent&quot; |
| COUNT | &quot;Count&quot; |
| SECONDS | &quot;Seconds&quot; |
| MILLISECONDS | &quot;Milliseconds&quot; |
| BYTES | &quot;Bytes&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |



