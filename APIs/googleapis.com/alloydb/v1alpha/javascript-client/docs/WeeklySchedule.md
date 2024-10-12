# AlloyDbApi.WeeklySchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daysOfWeek** | **[String]** | The days of the week to perform a backup. If this field is left empty, the default of every day of the week is used. | [optional] 
**startTimes** | [**[GoogleTypeTimeOfDay]**](GoogleTypeTimeOfDay.md) | The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00). If no start times are provided, a single fixed start time is chosen arbitrarily. | [optional] 



## Enum: [DaysOfWeekEnum]


* `DAY_OF_WEEK_UNSPECIFIED` (value: `"DAY_OF_WEEK_UNSPECIFIED"`)

* `MONDAY` (value: `"MONDAY"`)

* `TUESDAY` (value: `"TUESDAY"`)

* `WEDNESDAY` (value: `"WEDNESDAY"`)

* `THURSDAY` (value: `"THURSDAY"`)

* `FRIDAY` (value: `"FRIDAY"`)

* `SATURDAY` (value: `"SATURDAY"`)

* `SUNDAY` (value: `"SUNDAY"`)




