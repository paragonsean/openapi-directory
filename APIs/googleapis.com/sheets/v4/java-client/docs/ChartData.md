

# ChartData

The data included in a domain or series.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregateType** | [**AggregateTypeEnum**](#AggregateTypeEnum) | The aggregation type for the series of a data source chart. Only supported for data source charts. |  [optional] |
|**columnReference** | [**DataSourceColumnReference**](DataSourceColumnReference.md) |  |  [optional] |
|**groupRule** | [**ChartGroupRule**](ChartGroupRule.md) |  |  [optional] |
|**sourceRange** | [**ChartSourceRange**](ChartSourceRange.md) |  |  [optional] |



## Enum: AggregateTypeEnum

| Name | Value |
|---- | -----|
| CHART_AGGREGATE_TYPE_UNSPECIFIED | &quot;CHART_AGGREGATE_TYPE_UNSPECIFIED&quot; |
| AVERAGE | &quot;AVERAGE&quot; |
| COUNT | &quot;COUNT&quot; |
| MAX | &quot;MAX&quot; |
| MEDIAN | &quot;MEDIAN&quot; |
| MIN | &quot;MIN&quot; |
| SUM | &quot;SUM&quot; |



