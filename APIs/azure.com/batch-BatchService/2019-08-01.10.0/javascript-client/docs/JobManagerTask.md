# BatchService.JobManagerTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowLowPriorityNode** | **Boolean** | The default value is true. | [optional] 
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | Application Packages are downloaded and deployed to a shared directory, not the Task working directory. Therefore, if a referenced Application Package is already on the Compute Node, and is up to date, then it is not re-downloaded; the existing copy on the Compute Node is used. If a referenced Application Package cannot be installed, for example because the package has been deleted or because download failed, the Task fails. | [optional] 
**authenticationTokenSettings** | [**AuthenticationTokenSettings**](AuthenticationTokenSettings.md) |  | [optional] 
**commandLine** | **String** | The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables). | 
**constraints** | [**TaskConstraints**](TaskConstraints.md) |  | [optional] 
**containerSettings** | [**TaskContainerSettings**](TaskContainerSettings.md) |  | [optional] 
**displayName** | **String** | It need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) |  | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters. | 
**killJobOnCompletion** | **Boolean** | If true, when the Job Manager Task completes, the Batch service marks the Job as complete. If any Tasks are still running at this time (other than Job Release), those Tasks are terminated. If false, the completion of the Job Manager Task does not affect the Job status. In this case, you should either use the onAllTasksComplete attribute to terminate the Job, or have a client or user terminate the Job explicitly. An example of this is if the Job Manager creates a set of Tasks but then takes no further role in their execution. The default value is true. If you are using the onAllTasksComplete and onTaskFailure attributes to control Job lifetime, and using the Job Manager Task only to create the Tasks for the Job (not to monitor progress), then it is important to set killJobOnCompletion to false. | [optional] 
**outputFiles** | [**[OutputFile]**](OutputFile.md) | For multi-instance Tasks, the files will only be uploaded from the Compute Node on which the primary Task is executed. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | Files listed under this element are located in the Task&#39;s working directory. There is a maximum size for the list of resource files.  When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers. | [optional] 
**runExclusive** | **Boolean** | If true, no other Tasks will run on the same Node for as long as the Job Manager is running. If false, other Tasks can run simultaneously with the Job Manager on a Compute Node. The Job Manager Task counts normally against the Compute Node&#39;s concurrent Task limit, so this is only relevant if the Compute Node allows multiple concurrent Tasks. The default value is true. | [optional] 
**userIdentity** | [**UserIdentity**](UserIdentity.md) |  | [optional] 


