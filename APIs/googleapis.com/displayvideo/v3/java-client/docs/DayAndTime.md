

# DayAndTime

Representation of time defined by day of the week and hour of the day.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | Required. Day of the week. |  [optional] |
|**hourOfDay** | **Integer** | Required. Hour of the day. |  [optional] |
|**timeZoneResolution** | [**TimeZoneResolutionEnum**](#TimeZoneResolutionEnum) | Required. The mechanism used to determine the relevant timezone. |  [optional] |



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



