

# ReportConfigDefinition

The definition of a report config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataset** | [**ReportConfigDataset**](ReportConfigDataset.md) |  |  [optional] |
|**timePeriod** | [**ReportConfigTimePeriod**](ReportConfigTimePeriod.md) |  |  [optional] |
|**timeframe** | [**TimeframeEnum**](#TimeframeEnum) | The time frame for pulling data for the report. If custom, then a specific time period must be provided. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the report. |  |



## Enum: TimeframeEnum

| Name | Value |
|---- | -----|
| WEEK_TO_DATE | &quot;WeekToDate&quot; |
| MONTH_TO_DATE | &quot;MonthToDate&quot; |
| YEAR_TO_DATE | &quot;YearToDate&quot; |
| CUSTOM | &quot;Custom&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USAGE | &quot;Usage&quot; |



