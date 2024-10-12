# CostManagementClient.QueryDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | [**QueryDataset**](QueryDataset.md) |  | [optional] 
**timePeriod** | [**QueryTimePeriod**](QueryTimePeriod.md) |  | [optional] 
**timeframe** | **String** | The time frame for pulling data for the query. If custom, then a specific time period must be provided. | 
**type** | **String** | The type of the query. | 



## Enum: TimeframeEnum


* `MonthToDate` (value: `"MonthToDate"`)

* `BillingMonthToDate` (value: `"BillingMonthToDate"`)

* `TheLastMonth` (value: `"TheLastMonth"`)

* `TheLastBillingMonth` (value: `"TheLastBillingMonth"`)

* `WeekToDate` (value: `"WeekToDate"`)

* `Custom` (value: `"Custom"`)





## Enum: TypeEnum


* `Usage` (value: `"Usage"`)

* `ActualCost` (value: `"ActualCost"`)

* `AmortizedCost` (value: `"AmortizedCost"`)




