# BatchService.CloudTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityInfo** | [**AffinityInformation**](AffinityInformation.md) |  | [optional] 
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | Application packages are downloaded and deployed to a shared directory, not the Task working directory. Therefore, if a referenced package is already on the Node, and is up to date, then it is not re-downloaded; the existing copy on the Compute Node is used. If a referenced Package cannot be installed, for example because the package has been deleted or because download failed, the Task fails. | [optional] 
**authenticationTokenSettings** | [**AuthenticationTokenSettings**](AuthenticationTokenSettings.md) |  | [optional] 
**commandLine** | **String** | For multi-instance Tasks, the command line is executed as the primary Task, after the primary Task and all subtasks have finished executing the coordination command line. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables). | [optional] 
**constraints** | [**TaskConstraints**](TaskConstraints.md) |  | [optional] 
**containerSettings** | [**TaskContainerSettings**](TaskContainerSettings.md) |  | [optional] 
**creationTime** | **Date** |  | [optional] 
**dependsOn** | [**TaskDependencies**](TaskDependencies.md) |  | [optional] 
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**eTag** | **String** | This is an opaque string. You can use it to detect whether the Task has changed between requests. In particular, you can be pass the ETag when updating a Task to specify that your changes should take effect only if nobody else has modified the Task in the meantime. | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) |  | [optional] 
**executionInfo** | [**TaskExecutionInformation**](TaskExecutionInformation.md) |  | [optional] 
**exitConditions** | [**ExitConditions**](ExitConditions.md) |  | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. | [optional] 
**lastModified** | **Date** |  | [optional] 
**multiInstanceSettings** | [**MultiInstanceSettings**](MultiInstanceSettings.md) |  | [optional] 
**nodeInfo** | [**ComputeNodeInformation**](ComputeNodeInformation.md) |  | [optional] 
**outputFiles** | [**[OutputFile]**](OutputFile.md) | For multi-instance Tasks, the files will only be uploaded from the Compute Node on which the primary Task is executed. | [optional] 
**previousState** | [**TaskState**](TaskState.md) |  | [optional] 
**previousStateTransitionTime** | **Date** | This property is not set if the Task is in its initial Active state. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | For multi-instance Tasks, the resource files will only be downloaded to the Compute Node on which the primary Task is executed. There is a maximum size for the list of resource files.  When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers. | [optional] 
**state** | [**TaskState**](TaskState.md) |  | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**stats** | [**TaskStatistics**](TaskStatistics.md) |  | [optional] 
**url** | **String** |  | [optional] 
**userIdentity** | [**UserIdentity**](UserIdentity.md) |  | [optional] 


