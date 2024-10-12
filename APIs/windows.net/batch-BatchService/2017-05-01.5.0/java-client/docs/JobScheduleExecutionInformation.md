

# JobScheduleExecutionInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | This property is set only if the job schedule is in the completed state. |  [optional] |
|**nextRunTime** | **OffsetDateTime** | This property is meaningful only if the schedule is in the active state when the time comes around. For example, if the schedule is disabled, no job will be created at nextRunTime unless the job is enabled before then. |  [optional] |
|**recentJob** | [**RecentJob**](RecentJob.md) |  |  [optional] |



