# BatchService.JobPreparationTaskExecutionInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The time at which the Job Preparation task completed. This property is set only if the task is in the Completed state. | [optional] 
**exitCode** | **Number** | The exit code of the Job Preparation task. This property is set only if the task is in the Completed state. | [optional] 
**lastRetryTime** | **Date** | The most recent time at which a retry of the Job Preparation task started running. This property is set only if the task was retried (i.e. retryCount is nonzero). | [optional] 
**retryCount** | **Number** | The number of times the task has been retried by the Batch service. Every time the task exits with a non-zero exit code, it is deemed a task failure. The Batch service will retry the task up to the limit specified by the constraints. | 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | The time at which the task started running. Note that every time the task is restarted, this value is updated. | 
**state** | **String** | The current state of the Job Preparation task. | 
**taskRootDirectory** | **String** | The root directory of the Job Preparation task on the compute node. You can use this path to retrieve files created by the task, such as log files. | [optional] 
**taskRootDirectoryUrl** | **String** | The URL to the root directory of the Job Preparation task on the compute node. | [optional] 



## Enum: StateEnum


* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




