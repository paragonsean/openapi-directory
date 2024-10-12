

# ScheduleProperties

Definition of schedule parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedSchedule** | [**AdvancedSchedule**](AdvancedSchedule.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time. |  [optional] |
|**description** | **String** | Gets or sets the description. |  [optional] |
|**expiryTime** | **OffsetDateTime** | Gets or sets the end time of the schedule. |  [optional] |
|**expiryTimeOffsetMinutes** | **Double** | Gets or sets the expiry time&#39;s offset in minutes. |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | Gets or sets the frequency of the schedule. |  [optional] |
|**interval** | **Integer** | Gets or sets the interval of the schedule. |  [optional] |
|**isEnabled** | **Boolean** | Gets or sets a value indicating whether this schedule is enabled. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Gets or sets the last modified time. |  [optional] |
|**nextRun** | **OffsetDateTime** | Gets or sets the next run time of the schedule. |  [optional] |
|**nextRunOffsetMinutes** | **Double** | Gets or sets the next run time&#39;s offset in minutes. |  [optional] |
|**startTime** | **OffsetDateTime** | Gets or sets the start time of the schedule. |  [optional] |
|**startTimeOffsetMinutes** | **Double** | Gets the start time&#39;s offset in minutes. |  [optional] [readonly] |
|**timeZone** | **String** | Gets or sets the time zone of the schedule. |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| ONE_TIME | &quot;OneTime&quot; |
| DAY | &quot;Day&quot; |
| HOUR | &quot;Hour&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |
| MINUTE | &quot;Minute&quot; |



