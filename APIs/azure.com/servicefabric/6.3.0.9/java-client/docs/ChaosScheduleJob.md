

# ChaosScheduleJob

Defines a repetition rule and parameters of Chaos to be used with the Chaos Schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chaosParameters** | **String** | A reference to which Chaos Parameters of the Chaos Schedule to use. |  [optional] |
|**days** | [**ChaosScheduleJobActiveDaysOfWeek**](ChaosScheduleJobActiveDaysOfWeek.md) |  |  [optional] |
|**times** | [**List&lt;TimeRange&gt;**](TimeRange.md) | A list of Time Ranges that specify when during active days that this job will run. The times are interpreted as UTC. |  [optional] |



