

# QueryDefinition

The definition of a query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataset** | [**QueryDataset**](QueryDataset.md) |  |  [optional] |
|**timePeriod** | [**QueryTimePeriod**](QueryTimePeriod.md) |  |  [optional] |
|**timeframe** | [**TimeframeEnum**](#TimeframeEnum) | The time frame for pulling data for the query. If custom, then a specific time period must be provided. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the query. |  |



## Enum: TimeframeEnum

| Name | Value |
|---- | -----|
| MONTH_TO_DATE | &quot;MonthToDate&quot; |
| BILLING_MONTH_TO_DATE | &quot;BillingMonthToDate&quot; |
| THE_LAST_MONTH | &quot;TheLastMonth&quot; |
| THE_LAST_BILLING_MONTH | &quot;TheLastBillingMonth&quot; |
| WEEK_TO_DATE | &quot;WeekToDate&quot; |
| CUSTOM | &quot;Custom&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USAGE | &quot;Usage&quot; |
| ACTUAL_COST | &quot;ActualCost&quot; |
| AMORTIZED_COST | &quot;AmortizedCost&quot; |



