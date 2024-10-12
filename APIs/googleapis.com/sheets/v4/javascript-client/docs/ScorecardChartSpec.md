# GoogleSheetsApi.ScorecardChartSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregateType** | **String** | The aggregation type for key and baseline chart data in scorecard chart. This field is not supported for data source charts. Use the ChartData.aggregateType field of the key_value_data or baseline_value_data instead for data source charts. This field is optional. | [optional] 
**baselineValueData** | [**ChartData**](ChartData.md) |  | [optional] 
**baselineValueFormat** | [**BaselineValueFormat**](BaselineValueFormat.md) |  | [optional] 
**customFormatOptions** | [**ChartCustomNumberFormatOptions**](ChartCustomNumberFormatOptions.md) |  | [optional] 
**keyValueData** | [**ChartData**](ChartData.md) |  | [optional] 
**keyValueFormat** | [**KeyValueFormat**](KeyValueFormat.md) |  | [optional] 
**numberFormatSource** | **String** | The number format source used in the scorecard chart. This field is optional. | [optional] 
**scaleFactor** | **Number** | Value to scale scorecard key and baseline value. For example, a factor of 10 can be used to divide all values in the chart by 10. This field is optional. | [optional] 



## Enum: AggregateTypeEnum


* `CHART_AGGREGATE_TYPE_UNSPECIFIED` (value: `"CHART_AGGREGATE_TYPE_UNSPECIFIED"`)

* `AVERAGE` (value: `"AVERAGE"`)

* `COUNT` (value: `"COUNT"`)

* `MAX` (value: `"MAX"`)

* `MEDIAN` (value: `"MEDIAN"`)

* `MIN` (value: `"MIN"`)

* `SUM` (value: `"SUM"`)





## Enum: NumberFormatSourceEnum


* `CHART_NUMBER_FORMAT_SOURCE_UNDEFINED` (value: `"CHART_NUMBER_FORMAT_SOURCE_UNDEFINED"`)

* `FROM_DATA` (value: `"FROM_DATA"`)

* `CUSTOM` (value: `"CUSTOM"`)




