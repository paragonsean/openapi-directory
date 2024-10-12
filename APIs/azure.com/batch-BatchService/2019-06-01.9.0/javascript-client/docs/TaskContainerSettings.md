# BatchService.TaskContainerSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerRunOptions** | **String** | These additional options are supplied as arguments to the \&quot;docker create\&quot; command, in addition to those controlled by the Batch Service. | [optional] 
**imageName** | **String** | This is the full Image reference, as would be specified to \&quot;docker pull\&quot;. If no tag is provided as part of the Image name, the tag \&quot;:latest\&quot; is used as a default. | 
**registry** | [**ContainerRegistry**](ContainerRegistry.md) |  | [optional] 
**workingDirectory** | **String** | The default is &#39;taskWorkingDirectory&#39;. | [optional] 



## Enum: WorkingDirectoryEnum


* `taskWorkingDirectory` (value: `"taskWorkingDirectory"`)

* `containerImageDefault` (value: `"containerImageDefault"`)




