

# JobExecutionInformation

Contains information about the execution of a job in the Azure Batch service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | Gets or sets the completion time of the job. This property is set only if the job is in the completed state. |  [optional] |
|**poolId** | **String** | Gets or sets the id of the pool to which this job is assigned. |  [optional] |
|**schedulingError** | [**JobSchedulingError**](JobSchedulingError.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Gets or sets the start time of the job. |  |
|**terminateReason** | **String** | Gets or sets a string describing the reason the job ended. |  [optional] |



