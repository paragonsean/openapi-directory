

# JobRecurrence


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Gets or sets the maximum number of times that the job should run. |  [optional] |
|**endTime** | **OffsetDateTime** | Gets or sets the time at which the job will complete. |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | Gets or sets the frequency of recurrence (second, minute, hour, day, week, month). |  [optional] |
|**interval** | **Integer** | Gets or sets the interval between retries. |  [optional] |
|**schedule** | [**JobRecurrenceSchedule**](JobRecurrenceSchedule.md) |  |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| MINUTE | &quot;Minute&quot; |
| HOUR | &quot;Hour&quot; |
| DAY | &quot;Day&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |



