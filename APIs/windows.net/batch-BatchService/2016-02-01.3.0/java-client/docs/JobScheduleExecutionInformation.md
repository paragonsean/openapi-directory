

# JobScheduleExecutionInformation

Specifies how tasks should be run in a job associated with a job schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The time at which the schedule ended. This property is set only if the job schedule is in the completed state. |  [optional] |
|**nextRunTime** | **OffsetDateTime** | The next time at which a job will be created under this schedule. |  [optional] |
|**recentJob** | [**RecentJob**](RecentJob.md) |  |  [optional] |



