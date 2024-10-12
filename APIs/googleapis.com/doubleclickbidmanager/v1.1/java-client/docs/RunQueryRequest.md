

# RunQueryRequest

Request to run a stored query to generate a report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataRange** | [**DataRangeEnum**](#DataRangeEnum) | Report data range used to generate the report. |  [optional] |
|**reportDataEndTimeMs** | **String** | The ending time for the data that is shown in the report. Note, reportDataEndTimeMs is required if dataRange is CUSTOM_DATES and ignored otherwise. |  [optional] |
|**reportDataStartTimeMs** | **String** | The starting time for the data that is shown in the report. Note, reportDataStartTimeMs is required if dataRange is CUSTOM_DATES and ignored otherwise. |  [optional] |
|**timezoneCode** | **String** | Canonical timezone code for report data time. Defaults to America/New_York. |  [optional] |



## Enum: DataRangeEnum

| Name | Value |
|---- | -----|
| CUSTOM_DATES | &quot;CUSTOM_DATES&quot; |
| CURRENT_DAY | &quot;CURRENT_DAY&quot; |
| PREVIOUS_DAY | &quot;PREVIOUS_DAY&quot; |
| WEEK_TO_DATE | &quot;WEEK_TO_DATE&quot; |
| MONTH_TO_DATE | &quot;MONTH_TO_DATE&quot; |
| QUARTER_TO_DATE | &quot;QUARTER_TO_DATE&quot; |
| YEAR_TO_DATE | &quot;YEAR_TO_DATE&quot; |
| PREVIOUS_WEEK | &quot;PREVIOUS_WEEK&quot; |
| PREVIOUS_HALF_MONTH | &quot;PREVIOUS_HALF_MONTH&quot; |
| PREVIOUS_MONTH | &quot;PREVIOUS_MONTH&quot; |
| PREVIOUS_QUARTER | &quot;PREVIOUS_QUARTER&quot; |
| PREVIOUS_YEAR | &quot;PREVIOUS_YEAR&quot; |
| LAST_7_DAYS | &quot;LAST_7_DAYS&quot; |
| LAST_30_DAYS | &quot;LAST_30_DAYS&quot; |
| LAST_90_DAYS | &quot;LAST_90_DAYS&quot; |
| LAST_365_DAYS | &quot;LAST_365_DAYS&quot; |
| ALL_TIME | &quot;ALL_TIME&quot; |
| LAST_14_DAYS | &quot;LAST_14_DAYS&quot; |
| TYPE_NOT_SUPPORTED | &quot;TYPE_NOT_SUPPORTED&quot; |
| LAST_60_DAYS | &quot;LAST_60_DAYS&quot; |



