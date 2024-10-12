# DisplayVideo360Api.DayAndTimeAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dayOfWeek** | **String** | Required. The day of the week for this day and time targeting setting. | [optional] 
**endHour** | **Number** | Required. The end hour for day and time targeting. Must be between 1 (1 hour after start of day) and 24 (end of day). | [optional] 
**startHour** | **Number** | Required. The start hour for day and time targeting. Must be between 0 (start of day) and 23 (1 hour before end of day). | [optional] 
**timeZoneResolution** | **String** | Required. The mechanism used to determine which timezone to use for this day and time targeting setting. | [optional] 



## Enum: DayOfWeekEnum


* `DAY_OF_WEEK_UNSPECIFIED` (value: `"DAY_OF_WEEK_UNSPECIFIED"`)

* `MONDAY` (value: `"MONDAY"`)

* `TUESDAY` (value: `"TUESDAY"`)

* `WEDNESDAY` (value: `"WEDNESDAY"`)

* `THURSDAY` (value: `"THURSDAY"`)

* `FRIDAY` (value: `"FRIDAY"`)

* `SATURDAY` (value: `"SATURDAY"`)

* `SUNDAY` (value: `"SUNDAY"`)





## Enum: TimeZoneResolutionEnum


* `UNSPECIFIED` (value: `"TIME_ZONE_RESOLUTION_UNSPECIFIED"`)

* `END_USER` (value: `"TIME_ZONE_RESOLUTION_END_USER"`)

* `ADVERTISER` (value: `"TIME_ZONE_RESOLUTION_ADVERTISER"`)




