# BatchService.JobReleaseTaskExecutionInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The time at which the Job Release task completed. This property is set only if the task is in the Completed state. | [optional] 
**exitCode** | **Number** | The exit code of the Job Release task. This property is set only if the task is in the Completed state. | [optional] 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | The time at which the task started running. Note that every time the task is restarted, this value is updated. | 
**state** | **String** | The current state of the Job Release task. | 
**taskRootDirectory** | **String** | The root directory of the Job Release task on the compute node. You can use this path to retrieve files created by the task, such as log files. | [optional] 
**taskRootDirectoryUrl** | **String** | The URL to the root directory of the Job Release task on the compute node. | [optional] 



## Enum: StateEnum


* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




