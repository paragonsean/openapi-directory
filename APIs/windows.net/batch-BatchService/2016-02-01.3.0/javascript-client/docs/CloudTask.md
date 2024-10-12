# BatchService.CloudTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityInfo** | [**AffinityInformation**](AffinityInformation.md) |  | [optional] 
**commandLine** | **String** | The command line of the task. For multi-instance tasks, the command line is executed on the primary subtask after all the subtasks have finished executing the coordination command line. | [optional] 
**constraints** | [**TaskConstraints**](TaskConstraints.md) |  | [optional] 
**creationTime** | **Date** | The creation time of the task. | [optional] 
**dependsOn** | [**TaskDependencies**](TaskDependencies.md) |  | [optional] 
**displayName** | **String** | A display name for the task. | [optional] 
**eTag** | **String** | The ETag of the task. | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) | A list of environment variable settings for the task. | [optional] 
**executionInfo** | [**TaskExecutionInformation**](TaskExecutionInformation.md) |  | [optional] 
**id** | **String** | A string that uniquely identifies the task within the job. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. | [optional] 
**lastModified** | **Date** | The last modified time of the task. | [optional] 
**multiInstanceSettings** | [**MultiInstanceSettings**](MultiInstanceSettings.md) |  | [optional] 
**nodeInfo** | [**ComputeNodeInformation**](ComputeNodeInformation.md) |  | [optional] 
**previousState** | **String** | The previous state of the task. This property is not set if the task is in its initial Active state. | [optional] 
**previousStateTransitionTime** | **Date** | The time at which the task entered its previous state. This property is not set if the task is in its initial Active state. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | A list of files that the Batch service will download to the compute node before running the command line. For multi-instance tasks, the resource files will only be downloaded to the compute node on which the primary subtask is executed. | [optional] 
**runElevated** | **Boolean** | Whether to run the task in elevated mode. | [optional] 
**state** | **String** | The current state of the task. | [optional] 
**stateTransitionTime** | **Date** | The time at which the task entered its current state. | [optional] 
**stats** | [**TaskStatistics**](TaskStatistics.md) |  | [optional] 
**url** | **String** | The URL of the task. | [optional] 



## Enum: PreviousStateEnum


* `active` (value: `"active"`)

* `preparing` (value: `"preparing"`)

* `running` (value: `"running"`)

* `completed` (value: `"completed"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `preparing` (value: `"preparing"`)

* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




