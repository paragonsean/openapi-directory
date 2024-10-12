

# TimePeriod

Represents a span of time that the business is open, starting on the specified open day/time and closing on the specified close day/time. The closing time must occur after the opening time, for example later in the same day, or on a subsequent day.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closeDay** | [**CloseDayEnum**](#CloseDayEnum) | Indicates the day of the week this period ends on. |  [optional] |
|**closeTime** | **String** | Time in 24hr ISO 8601 extended format (hh:mm). Valid values are 00:00-24:00, where 24:00 represents midnight at the end of the specified day field. |  [optional] |
|**openDay** | [**OpenDayEnum**](#OpenDayEnum) | Indicates the day of the week this period starts on. |  [optional] |
|**openTime** | **String** | Time in 24hr ISO 8601 extended format (hh:mm). Valid values are 00:00-24:00, where 24:00 represents midnight at the end of the specified day field. |  [optional] |



## Enum: CloseDayEnum

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



## Enum: OpenDayEnum

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



