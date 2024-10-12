

# MultiInstanceSettings

Information about the settings required for multi-instance task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonResourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | Gets or sets a list of files that Batch will download on all subtasks. |  [optional] |
|**coordinationCommandLine** | **String** | Gets or sets the command to be run on the compute node instances to setup coordination among the subtasks. |  [optional] |
|**numberOfInstances** | **Integer** | Gets or sets the number of compute node instances used for multi-instance task. |  |



