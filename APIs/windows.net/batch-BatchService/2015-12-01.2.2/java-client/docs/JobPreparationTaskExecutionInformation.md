

# JobPreparationTaskExecutionInformation

Contains information about the execution of a Job Preparation task on a compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | Gets or sets the time at which the Job Preparation task completed. This property is set only if the task is in the Completed state. |  [optional] |
|**exitCode** | **Integer** | Gets or sets the exit code of the Job Preparation task. This property is set only if the task is in the Completed state. |  [optional] |
|**lastRetryTime** | **OffsetDateTime** | Gets or sets the most recent time at which a retry of the Job Preparation task started running. This property is set only if the task was retried (i.e. retryCount is nonzero). |  [optional] |
|**retryCount** | **Integer** | Gets or sets the number of times the Job Preparation task has been retried by the Batch service. |  |
|**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Gets or sets the time at which the Job Preparation task started running. |  |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the current running state of the Job Preparation task on the compute node. |  |
|**taskRootDirectory** | **String** | Gets or sets the root directory of the Job Preparation task on the compute node. |  [optional] |
|**taskRootDirectoryUrl** | **String** | Gets or sets the URL to the root directory of the Job Preparation task on the compute node. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



