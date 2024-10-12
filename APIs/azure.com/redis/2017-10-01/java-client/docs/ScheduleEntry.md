

# ScheduleEntry

Patch schedule entry for a Premium Redis Cache.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | Day of the week when a cache can be patched. |  |
|**maintenanceWindow** | **String** | ISO8601 timespan specifying how much time cache patching can take.  |  [optional] |
|**startHourUtc** | **Integer** | Start hour after which cache patching can start. |  |



## Enum: DayOfWeekEnum

| Name | Value |
|---- | -----|
| MONDAY | &quot;Monday&quot; |
| TUESDAY | &quot;Tuesday&quot; |
| WEDNESDAY | &quot;Wednesday&quot; |
| THURSDAY | &quot;Thursday&quot; |
| FRIDAY | &quot;Friday&quot; |
| SATURDAY | &quot;Saturday&quot; |
| SUNDAY | &quot;Sunday&quot; |
| EVERYDAY | &quot;Everyday&quot; |
| WEEKEND | &quot;Weekend&quot; |



