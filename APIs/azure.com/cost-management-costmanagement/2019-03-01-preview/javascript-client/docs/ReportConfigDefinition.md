# CostManagementClient.ReportConfigDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | [**ReportConfigDataset**](ReportConfigDataset.md) |  | [optional] 
**timePeriod** | [**ReportConfigTimePeriod**](ReportConfigTimePeriod.md) |  | [optional] 
**timeframe** | **String** | The time frame for pulling data for the report. If custom, then a specific time period must be provided. | 
**type** | **String** | The type of the report. Usage represents actual usage, forecast represents forecasted data and UsageAndForecast represents both usage and forecasted data. Actual usage and forecasted data can be differentiated based on dates. | 



## Enum: TimeframeEnum


* `WeekToDate` (value: `"WeekToDate"`)

* `MonthToDate` (value: `"MonthToDate"`)

* `YearToDate` (value: `"YearToDate"`)

* `Custom` (value: `"Custom"`)





## Enum: TypeEnum


* `Usage` (value: `"Usage"`)




