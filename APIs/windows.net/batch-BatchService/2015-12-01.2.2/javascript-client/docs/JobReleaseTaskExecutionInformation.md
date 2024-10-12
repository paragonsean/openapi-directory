# BatchService.JobReleaseTaskExecutionInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | Gets or sets the time at which the Job Release task completed. This property is set only if the task is in the Completed state. | [optional] 
**exitCode** | **Number** | Gets or sets the exit code of the Job Release task. This property is set only if the task is in the Completed state. | [optional] 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | Gets or sets the time at which the Job Release task started running. | 
**state** | **String** | Gets or sets the current running state of the Job Release task on the compute node. | 
**taskRootDirectory** | **String** | Gets or sets the root directory of the Job Release task on the compute node. | [optional] 
**taskRootDirectoryUrl** | **String** | Gets or sets the URL to the root directory of the Job Release task on the compute node. | [optional] 



## Enum: StateEnum


* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




