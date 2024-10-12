# CostManagementClient.QueryDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | [**QueryDataset**](QueryDataset.md) |  | [optional] 
**timePeriod** | [**QueryTimePeriod**](QueryTimePeriod.md) |  | [optional] 
**timeframe** | **String** | The time frame for pulling data for the query. If custom, then a specific time period must be provided. | 
**type** | **String** | The type of the query. | 



## Enum: TimeframeEnum


* `WeekToDate` (value: `"WeekToDate"`)

* `MonthToDate` (value: `"MonthToDate"`)

* `YearToDate` (value: `"YearToDate"`)

* `TheLastWeek` (value: `"TheLastWeek"`)

* `TheLastMonth` (value: `"TheLastMonth"`)

* `TheLastYear` (value: `"TheLastYear"`)

* `Custom` (value: `"Custom"`)





## Enum: TypeEnum


* `Usage` (value: `"Usage"`)




