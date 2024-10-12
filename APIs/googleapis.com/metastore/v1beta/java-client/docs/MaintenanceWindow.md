

# MaintenanceWindow

Maintenance window. This specifies when Dataproc Metastore may perform system maintenance operation to the service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | The day of week, when the window starts. |  [optional] |
|**hourOfDay** | **Integer** | The hour of day (0-23) when the window starts. |  [optional] |



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



