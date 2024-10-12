# SearchAds360ReportingApi.GoogleAdsSearchads360V0CommonAdScheduleInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dayOfWeek** | **String** | Day of the week the schedule applies to. This field is required for CREATE operations and is prohibited on UPDATE operations. | [optional] 
**endHour** | **Number** | Ending hour in 24 hour time; 24 signifies end of the day. This field must be between 0 and 24, inclusive. This field is required for CREATE operations and is prohibited on UPDATE operations. | [optional] 
**endMinute** | **String** | Minutes after the end hour at which this schedule ends. The schedule is exclusive of the end minute. This field is required for CREATE operations and is prohibited on UPDATE operations. | [optional] 
**startHour** | **Number** | Starting hour in 24 hour time. This field must be between 0 and 23, inclusive. This field is required for CREATE operations and is prohibited on UPDATE operations. | [optional] 
**startMinute** | **String** | Minutes after the start hour at which this schedule starts. This field is required for CREATE operations and is prohibited on UPDATE operations. | [optional] 



## Enum: DayOfWeekEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `MONDAY` (value: `"MONDAY"`)

* `TUESDAY` (value: `"TUESDAY"`)

* `WEDNESDAY` (value: `"WEDNESDAY"`)

* `THURSDAY` (value: `"THURSDAY"`)

* `FRIDAY` (value: `"FRIDAY"`)

* `SATURDAY` (value: `"SATURDAY"`)

* `SUNDAY` (value: `"SUNDAY"`)





## Enum: EndMinuteEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ZERO` (value: `"ZERO"`)

* `FIFTEEN` (value: `"FIFTEEN"`)

* `THIRTY` (value: `"THIRTY"`)

* `FORTY_FIVE` (value: `"FORTY_FIVE"`)





## Enum: StartMinuteEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ZERO` (value: `"ZERO"`)

* `FIFTEEN` (value: `"FIFTEEN"`)

* `THIRTY` (value: `"THIRTY"`)

* `FORTY_FIVE` (value: `"FORTY_FIVE"`)




