

# JobExecutionInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | This property is set only if the job is in the completed state. |  [optional] |
|**poolId** | **String** | This element contains the actual pool where the job is assigned. When you get job details from the service, they also contain a poolInfo element, which contains the pool configuration data from when the job was added or updated. That poolInfo element may also contain a poolId element. If it does, the two IDs are the same. If it does not, it means the job ran on an auto pool, and this property contains the ID of that auto pool. |  [optional] |
|**schedulingError** | [**JobSchedulingError**](JobSchedulingError.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | This is the time at which the job was created. |  |
|**terminateReason** | **String** | This property is set only if the job is in the completed state. If the Batch service terminates the job, it sets the reason as follows: JMComplete - the Job Manager task completed, and killJobOnCompletion was set to true. MaxWallClockTimeExpiry - the job reached its maxWallClockTime constraint. TerminateJobSchedule - the job ran as part of a schedule, and the schedule terminated. AllTasksComplete - the job&#39;s onAllTasksComplete attribute is set to terminatejob, and all tasks in the job are complete. TaskFailed - the job&#39;s onTaskFailure attribute is set to performExitOptionsJobAction, and a task in the job failed with an exit condition that specified a jobAction of terminatejob. Any other string is a user-defined reason specified in a call to the &#39;Terminate a job&#39; operation. |  [optional] |



