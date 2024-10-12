

# Recurrence

The repeating times at which this profile begins. This element is not used if the FixedDate element is used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | the recurrence frequency. How often the schedule profile should take effect. This value must be Week, meaning each week will have the same set of profiles. For example, to set a daily schedule, set **schedule** to every day of the week. The frequency property specifies that the schedule is repeated weekly. |  |
|**schedule** | [**RecurrentSchedule**](RecurrentSchedule.md) |  |  |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SECOND | &quot;Second&quot; |
| MINUTE | &quot;Minute&quot; |
| HOUR | &quot;Hour&quot; |
| DAY | &quot;Day&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |
| YEAR | &quot;Year&quot; |



