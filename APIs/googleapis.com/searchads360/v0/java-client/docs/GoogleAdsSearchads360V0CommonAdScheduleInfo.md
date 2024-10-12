

# GoogleAdsSearchads360V0CommonAdScheduleInfo

Represents an AdSchedule criterion. AdSchedule is specified as the day of the week and a time interval within which ads will be shown. No more than six AdSchedules can be added for the same day.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | Day of the week the schedule applies to. This field is required for CREATE operations and is prohibited on UPDATE operations. |  [optional] |
|**endHour** | **Integer** | Ending hour in 24 hour time; 24 signifies end of the day. This field must be between 0 and 24, inclusive. This field is required for CREATE operations and is prohibited on UPDATE operations. |  [optional] |
|**endMinute** | [**EndMinuteEnum**](#EndMinuteEnum) | Minutes after the end hour at which this schedule ends. The schedule is exclusive of the end minute. This field is required for CREATE operations and is prohibited on UPDATE operations. |  [optional] |
|**startHour** | **Integer** | Starting hour in 24 hour time. This field must be between 0 and 23, inclusive. This field is required for CREATE operations and is prohibited on UPDATE operations. |  [optional] |
|**startMinute** | [**StartMinuteEnum**](#StartMinuteEnum) | Minutes after the start hour at which this schedule starts. This field is required for CREATE operations and is prohibited on UPDATE operations. |  [optional] |



## Enum: DayOfWeekEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| MONDAY | &quot;MONDAY&quot; |
| TUESDAY | &quot;TUESDAY&quot; |
| WEDNESDAY | &quot;WEDNESDAY&quot; |
| THURSDAY | &quot;THURSDAY&quot; |
| FRIDAY | &quot;FRIDAY&quot; |
| SATURDAY | &quot;SATURDAY&quot; |
| SUNDAY | &quot;SUNDAY&quot; |



## Enum: EndMinuteEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ZERO | &quot;ZERO&quot; |
| FIFTEEN | &quot;FIFTEEN&quot; |
| THIRTY | &quot;THIRTY&quot; |
| FORTY_FIVE | &quot;FORTY_FIVE&quot; |



## Enum: StartMinuteEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ZERO | &quot;ZERO&quot; |
| FIFTEEN | &quot;FIFTEEN&quot; |
| THIRTY | &quot;THIRTY&quot; |
| FORTY_FIVE | &quot;FORTY_FIVE&quot; |



