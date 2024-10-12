# BatchService.CloudTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityInfo** | [**AffinityInformation**](AffinityInformation.md) |  | [optional] 
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) |  | [optional] 
**authenticationTokenSettings** | [**AuthenticationTokenSettings**](AuthenticationTokenSettings.md) |  | [optional] 
**commandLine** | **String** | For multi-instance tasks, the command line is executed as the primary task, after the primary task and all subtasks have finished executing the coordination command line. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. | [optional] 
**constraints** | [**TaskConstraints**](TaskConstraints.md) |  | [optional] 
**creationTime** | **Date** |  | [optional] 
**dependsOn** | [**TaskDependencies**](TaskDependencies.md) |  | [optional] 
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**eTag** | **String** | This is an opaque string. You can use it to detect whether the task has changed between requests. In particular, you can be pass the ETag when updating a task to specify that your changes should take effect only if nobody else has modified the task in the meantime. | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) |  | [optional] 
**executionInfo** | [**TaskExecutionInformation**](TaskExecutionInformation.md) |  | [optional] 
**exitConditions** | [**ExitConditions**](ExitConditions.md) |  | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. | [optional] 
**lastModified** | **Date** |  | [optional] 
**multiInstanceSettings** | [**MultiInstanceSettings**](MultiInstanceSettings.md) |  | [optional] 
**nodeInfo** | [**ComputeNodeInformation**](ComputeNodeInformation.md) |  | [optional] 
**outputFiles** | [**[OutputFile]**](OutputFile.md) | For multi-instance tasks, the files will only be uploaded from the compute node on which the primary task is executed. | [optional] 
**previousState** | [**TaskState**](TaskState.md) |  | [optional] 
**previousStateTransitionTime** | **Date** | This property is not set if the task is in its initial Active state. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | For multi-instance tasks, the resource files will only be downloaded to the compute node on which the primary task is executed. | [optional] 
**state** | [**TaskState**](TaskState.md) |  | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**stats** | [**TaskStatistics**](TaskStatistics.md) |  | [optional] 
**url** | **String** |  | [optional] 
**userIdentity** | [**UserIdentity**](UserIdentity.md) |  | [optional] 


