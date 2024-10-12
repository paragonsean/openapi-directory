# DisplayVideo360Api.TargetFrequency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targetCount** | **String** | The target number of times, on average, the ads will be shown to the same person in the timespan dictated by time_unit and time_unit_count. | [optional] 
**timeUnit** | **String** | The unit of time in which the target frequency will be applied. The following time unit is applicable: * &#x60;TIME_UNIT_WEEKS&#x60; | [optional] 
**timeUnitCount** | **Number** | The number of time_unit the target frequency will last. The following restrictions apply based on the value of time_unit: * &#x60;TIME_UNIT_WEEKS&#x60; - must be 1 | [optional] 



## Enum: TimeUnitEnum


* `UNSPECIFIED` (value: `"TIME_UNIT_UNSPECIFIED"`)

* `LIFETIME` (value: `"TIME_UNIT_LIFETIME"`)

* `MONTHS` (value: `"TIME_UNIT_MONTHS"`)

* `WEEKS` (value: `"TIME_UNIT_WEEKS"`)

* `DAYS` (value: `"TIME_UNIT_DAYS"`)

* `HOURS` (value: `"TIME_UNIT_HOURS"`)

* `MINUTES` (value: `"TIME_UNIT_MINUTES"`)




