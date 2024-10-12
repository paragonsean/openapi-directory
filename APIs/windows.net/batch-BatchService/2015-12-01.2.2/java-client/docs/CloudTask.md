

# CloudTask

An Azure Batch task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affinityInfo** | [**AffinityInformation**](AffinityInformation.md) |  |  [optional] |
|**commandLine** | **String** | Gets or sets the command line of the task. For multi-instance tasks, the command line is executed on the primary subtask after all the subtasks have finished executing the coordination command line. |  [optional] |
|**constraints** | [**TaskConstraints**](TaskConstraints.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time of the task. |  [optional] |
|**dependsOn** | [**TaskDependencies**](TaskDependencies.md) |  |  [optional] |
|**displayName** | **String** | Gets or sets a display name for the task. |  [optional] |
|**eTag** | **String** | Gets or sets the ETag of the task. |  [optional] |
|**environmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | Gets or sets a list of environment variable settings for the task. |  [optional] |
|**executionInfo** | [**TaskExecutionInformation**](TaskExecutionInformation.md) |  |  [optional] |
|**id** | **String** | Gets or sets a string that uniquely identifies the task within the job. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. |  [optional] |
|**lastModified** | **OffsetDateTime** | Gets or sets the last modified time of the task. |  [optional] |
|**multiInstanceSettings** | [**MultiInstanceSettings**](MultiInstanceSettings.md) |  |  [optional] |
|**nodeInfo** | [**ComputeNodeInformation**](ComputeNodeInformation.md) |  |  [optional] |
|**previousState** | [**PreviousStateEnum**](#PreviousStateEnum) | Gets or sets the previous state of the task. This property is not set if the task is in its initial Active state. |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the task entered its previous state. This property is not set if the task is in its initial Active state. |  [optional] |
|**resourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | Gets or sets a list of files that Batch will download to the compute node before running the command line. For multi-instance tasks, the resource files will only be downloaded to the compute node on which the primary subtask is executed. |  [optional] |
|**runElevated** | **Boolean** | Gets or sets whether to run the task in elevated mode. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the current state of the task. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the task entered its current state. |  [optional] |
|**stats** | [**TaskStatistics**](TaskStatistics.md) |  |  [optional] |
|**url** | **String** | Gets or sets the URL of the task. |  [optional] |



## Enum: PreviousStateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PREPARING | &quot;preparing&quot; |
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PREPARING | &quot;preparing&quot; |
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



