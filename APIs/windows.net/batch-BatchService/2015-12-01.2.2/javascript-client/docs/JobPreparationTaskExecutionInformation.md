# BatchService.JobPreparationTaskExecutionInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | Gets or sets the time at which the Job Preparation task completed. This property is set only if the task is in the Completed state. | [optional] 
**exitCode** | **Number** | Gets or sets the exit code of the Job Preparation task. This property is set only if the task is in the Completed state. | [optional] 
**lastRetryTime** | **Date** | Gets or sets the most recent time at which a retry of the Job Preparation task started running. This property is set only if the task was retried (i.e. retryCount is nonzero). | [optional] 
**retryCount** | **Number** | Gets or sets the number of times the Job Preparation task has been retried by the Batch service. | 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | Gets or sets the time at which the Job Preparation task started running. | 
**state** | **String** | Gets or sets the current running state of the Job Preparation task on the compute node. | 
**taskRootDirectory** | **String** | Gets or sets the root directory of the Job Preparation task on the compute node. | [optional] 
**taskRootDirectoryUrl** | **String** | Gets or sets the URL to the root directory of the Job Preparation task on the compute node. | [optional] 



## Enum: StateEnum


* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




