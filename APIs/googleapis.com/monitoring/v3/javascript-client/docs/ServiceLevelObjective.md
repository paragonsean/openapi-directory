# CloudMonitoringApi.ServiceLevelObjective

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendarPeriod** | **String** | A calendar period, semantically \&quot;since the start of the current \&quot;. At this time, only DAY, WEEK, FORTNIGHT, and MONTH are supported. | [optional] 
**displayName** | **String** | Name used for UI elements listing this SLO. | [optional] 
**goal** | **Number** | The fraction of service that must be good in order for this objective to be met. 0 &lt; goal &lt;&#x3D; 0.999. | [optional] 
**name** | **String** | Resource name for this ServiceLevelObjective. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]  | [optional] 
**rollingPeriod** | **String** | A rolling time period, semantically \&quot;in the past \&quot;. Must be an integer multiple of 1 day no larger than 30 days. | [optional] 
**serviceLevelIndicator** | [**ServiceLevelIndicator**](ServiceLevelIndicator.md) |  | [optional] 
**userLabels** | **{String: String}** | Labels which have been used to annotate the service-level objective. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value. | [optional] 



## Enum: CalendarPeriodEnum


* `CALENDAR_PERIOD_UNSPECIFIED` (value: `"CALENDAR_PERIOD_UNSPECIFIED"`)

* `DAY` (value: `"DAY"`)

* `WEEK` (value: `"WEEK"`)

* `FORTNIGHT` (value: `"FORTNIGHT"`)

* `MONTH` (value: `"MONTH"`)

* `QUARTER` (value: `"QUARTER"`)

* `HALF` (value: `"HALF"`)

* `YEAR` (value: `"YEAR"`)




