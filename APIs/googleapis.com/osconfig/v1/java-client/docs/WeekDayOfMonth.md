

# WeekDayOfMonth

Represents one week day in a month. An example is \"the 4th Sunday\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | Required. A day of the week. |  [optional] |
|**dayOffset** | **Integer** | Optional. Represents the number of days before or after the given week day of month that the patch deployment is scheduled for. For example if &#x60;week_ordinal&#x60; and &#x60;day_of_week&#x60; values point to the second Tuesday of the month and the &#x60;day_offset&#x60; value is set to &#x60;3&#x60;, patch deployment takes place three days after the second Tuesday of the month. If this value is negative, for example -5, patches are deployed five days before the second Tuesday of the month. Allowed values are in range [-30, 30]. |  [optional] |
|**weekOrdinal** | **Integer** | Required. Week number in a month. 1-4 indicates the 1st to 4th week of the month. -1 indicates the last week of the month. |  [optional] |



## Enum: DayOfWeekEnum

| Name | Value |
|---- | -----|
| DAY_OF_WEEK_UNSPECIFIED | &quot;DAY_OF_WEEK_UNSPECIFIED&quot; |
| MONDAY | &quot;MONDAY&quot; |
| TUESDAY | &quot;TUESDAY&quot; |
| WEDNESDAY | &quot;WEDNESDAY&quot; |
| THURSDAY | &quot;THURSDAY&quot; |
| FRIDAY | &quot;FRIDAY&quot; |
| SATURDAY | &quot;SATURDAY&quot; |
| SUNDAY | &quot;SUNDAY&quot; |



