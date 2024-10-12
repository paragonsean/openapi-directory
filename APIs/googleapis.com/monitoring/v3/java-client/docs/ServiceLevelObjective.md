

# ServiceLevelObjective

A Service-Level Objective (SLO) describes a level of desired good service. It consists of a service-level indicator (SLI), a performance goal, and a period over which the objective is to be evaluated against that goal. The SLO can use SLIs defined in a number of different manners. Typical SLOs might include \"99% of requests in each rolling week have latency below 200 milliseconds\" or \"99.5% of requests in each calendar month return successfully.\"

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calendarPeriod** | [**CalendarPeriodEnum**](#CalendarPeriodEnum) | A calendar period, semantically \&quot;since the start of the current \&quot;. At this time, only DAY, WEEK, FORTNIGHT, and MONTH are supported. |  [optional] |
|**displayName** | **String** | Name used for UI elements listing this SLO. |  [optional] |
|**goal** | **Double** | The fraction of service that must be good in order for this objective to be met. 0 &lt; goal &lt;&#x3D; 0.999. |  [optional] |
|**name** | **String** | Resource name for this ServiceLevelObjective. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]  |  [optional] |
|**rollingPeriod** | **String** | A rolling time period, semantically \&quot;in the past \&quot;. Must be an integer multiple of 1 day no larger than 30 days. |  [optional] |
|**serviceLevelIndicator** | [**ServiceLevelIndicator**](ServiceLevelIndicator.md) |  |  [optional] |
|**userLabels** | **Map&lt;String, String&gt;** | Labels which have been used to annotate the service-level objective. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value. |  [optional] |



## Enum: CalendarPeriodEnum

| Name | Value |
|---- | -----|
| CALENDAR_PERIOD_UNSPECIFIED | &quot;CALENDAR_PERIOD_UNSPECIFIED&quot; |
| DAY | &quot;DAY&quot; |
| WEEK | &quot;WEEK&quot; |
| FORTNIGHT | &quot;FORTNIGHT&quot; |
| MONTH | &quot;MONTH&quot; |
| QUARTER | &quot;QUARTER&quot; |
| HALF | &quot;HALF&quot; |
| YEAR | &quot;YEAR&quot; |



