# BatchService.TaskAddParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityInfo** | [**AffinityInformation**](AffinityInformation.md) |  | [optional] 
**commandLine** | **String** | Gets or sets the command line of the task. For multi-instance tasks, the command line is executed on the primary subtask after all the subtasks have finished executing the coordination command line. | 
**constraints** | [**TaskConstraints**](TaskConstraints.md) |  | [optional] 
**dependsOn** | [**TaskDependencies**](TaskDependencies.md) |  | [optional] 
**displayName** | **String** | Gets or sets a display name for the task. | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) | Gets or sets a list of environment variable settings for the task. | [optional] 
**id** | **String** | Gets or sets a string that uniquely identifies the task within the job. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. | 
**multiInstanceSettings** | [**MultiInstanceSettings**](MultiInstanceSettings.md) |  | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | Gets or sets a list of files that Batch will download to the compute node before running the command line. For multi-instance tasks, the resource files will only be downloaded to the compute node on which the primary subtask is executed. | [optional] 
**runElevated** | **Boolean** | Gets or sets whether to run the task in elevated mode. | [optional] 


