

# DayAndTimeAssignedTargetingOptionDetails

Representation of a segment of time defined on a specific day of the week and with a start and end time. The time represented by `start_hour` must be before the time represented by `end_hour`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | Required. The day of the week for this day and time targeting setting. |  [optional] |
|**endHour** | **Integer** | Required. The end hour for day and time targeting. Must be between 1 (1 hour after start of day) and 24 (end of day). |  [optional] |
|**startHour** | **Integer** | Required. The start hour for day and time targeting. Must be between 0 (start of day) and 23 (1 hour before end of day). |  [optional] |
|**timeZoneResolution** | [**TimeZoneResolutionEnum**](#TimeZoneResolutionEnum) | Required. The mechanism used to determine which timezone to use for this day and time targeting setting. |  [optional] |



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



## Enum: TimeZoneResolutionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TIME_ZONE_RESOLUTION_UNSPECIFIED&quot; |
| END_USER | &quot;TIME_ZONE_RESOLUTION_END_USER&quot; |
| ADVERTISER | &quot;TIME_ZONE_RESOLUTION_ADVERTISER&quot; |



