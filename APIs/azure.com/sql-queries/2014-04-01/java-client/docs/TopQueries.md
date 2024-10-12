

# TopQueries

A database query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationFunction** | [**AggregationFunctionEnum**](#AggregationFunctionEnum) | The function that is used to aggregate each query&#39;s metrics. |  [optional] [readonly] |
|**executionType** | [**ExecutionTypeEnum**](#ExecutionTypeEnum) | The execution type that is used to filter the query instances that are returned. |  [optional] [readonly] |
|**intervalType** | **String** | The duration of the interval (ISO8601 duration format). |  [optional] [readonly] |
|**numberOfTopQueries** | **BigDecimal** | The number of requested queries. |  [optional] [readonly] |
|**observationEndTime** | **OffsetDateTime** | The end time for queries that are returned (ISO8601 format) |  [optional] [readonly] |
|**observationStartTime** | **OffsetDateTime** | The start time for queries that are returned (ISO8601 format) |  [optional] [readonly] |
|**observedMetric** | [**ObservedMetricEnum**](#ObservedMetricEnum) | The type of metric to use for ordering the top metrics. |  [optional] [readonly] |
|**queries** | [**List&lt;QueryStatistic&gt;**](QueryStatistic.md) | The list of queries. |  [optional] [readonly] |



## Enum: AggregationFunctionEnum

| Name | Value |
|---- | -----|
| MIN | &quot;min&quot; |
| MAX | &quot;max&quot; |
| AVG | &quot;avg&quot; |
| SUM | &quot;sum&quot; |



## Enum: ExecutionTypeEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| REGULAR | &quot;regular&quot; |
| IRREGULAR | &quot;irregular&quot; |
| ABORTED | &quot;aborted&quot; |
| EXCEPTION | &quot;exception&quot; |



## Enum: ObservedMetricEnum

| Name | Value |
|---- | -----|
| CPU | &quot;cpu&quot; |
| IO | &quot;io&quot; |
| LOGIO | &quot;logio&quot; |
| DURATION | &quot;duration&quot; |
| EXECUTION_COUNT | &quot;executionCount&quot; |



