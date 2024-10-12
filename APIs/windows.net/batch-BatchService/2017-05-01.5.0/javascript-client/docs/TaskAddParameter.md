# BatchService.TaskAddParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityInfo** | [**AffinityInformation**](AffinityInformation.md) |  | [optional] 
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) |  | [optional] 
**authenticationTokenSettings** | [**AuthenticationTokenSettings**](AuthenticationTokenSettings.md) |  | [optional] 
**commandLine** | **String** | For multi-instance tasks, the command line is executed as the primary task, after the primary task and all subtasks have finished executing the coordination command line. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. | 
**constraints** | [**TaskConstraints**](TaskConstraints.md) |  | [optional] 
**dependsOn** | [**TaskDependencies**](TaskDependencies.md) |  | [optional] 
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) |  | [optional] 
**exitConditions** | [**ExitConditions**](ExitConditions.md) |  | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within a job that differ only by case). | 
**multiInstanceSettings** | [**MultiInstanceSettings**](MultiInstanceSettings.md) |  | [optional] 
**outputFiles** | [**[OutputFile]**](OutputFile.md) | For multi-instance tasks, the files will only be uploaded from the compute node on which the primary task is executed. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | For multi-instance tasks, the resource files will only be downloaded to the compute node on which the primary task is executed. | [optional] 
**userIdentity** | [**UserIdentity**](UserIdentity.md) |  | [optional] 


