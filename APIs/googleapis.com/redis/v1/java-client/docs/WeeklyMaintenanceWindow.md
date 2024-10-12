

# WeeklyMaintenanceWindow

Time window in which disruptive maintenance updates occur. Non-disruptive updates can occur inside or outside this window.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**day** | [**DayEnum**](#DayEnum) | Required. The day of week that maintenance updates occur. |  [optional] |
|**duration** | **String** | Output only. Duration of the maintenance window. The current window is fixed at 1 hour. |  [optional] [readonly] |
|**startTime** | [**TimeOfDay**](TimeOfDay.md) |  |  [optional] |



## Enum: DayEnum

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



