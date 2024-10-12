

# DateRange

Represents a date range.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endDate** | **LocalDate** |  |  [optional] |
|**kind** | **String** | The kind of resource this is, in this case dfareporting#dateRange. |  [optional] |
|**relativeDateRange** | [**RelativeDateRangeEnum**](#RelativeDateRangeEnum) | The date range relative to the date of when the report is run. |  [optional] |
|**startDate** | **LocalDate** |  |  [optional] |



## Enum: RelativeDateRangeEnum

| Name | Value |
|---- | -----|
| TODAY | &quot;TODAY&quot; |
| YESTERDAY | &quot;YESTERDAY&quot; |
| WEEK_TO_DATE | &quot;WEEK_TO_DATE&quot; |
| MONTH_TO_DATE | &quot;MONTH_TO_DATE&quot; |
| QUARTER_TO_DATE | &quot;QUARTER_TO_DATE&quot; |
| YEAR_TO_DATE | &quot;YEAR_TO_DATE&quot; |
| PREVIOUS_WEEK | &quot;PREVIOUS_WEEK&quot; |
| PREVIOUS_MONTH | &quot;PREVIOUS_MONTH&quot; |
| PREVIOUS_QUARTER | &quot;PREVIOUS_QUARTER&quot; |
| PREVIOUS_YEAR | &quot;PREVIOUS_YEAR&quot; |
| LAST_7_DAYS | &quot;LAST_7_DAYS&quot; |
| LAST_30_DAYS | &quot;LAST_30_DAYS&quot; |
| LAST_90_DAYS | &quot;LAST_90_DAYS&quot; |
| LAST_365_DAYS | &quot;LAST_365_DAYS&quot; |
| LAST_24_MONTHS | &quot;LAST_24_MONTHS&quot; |
| LAST_14_DAYS | &quot;LAST_14_DAYS&quot; |
| LAST_60_DAYS | &quot;LAST_60_DAYS&quot; |



