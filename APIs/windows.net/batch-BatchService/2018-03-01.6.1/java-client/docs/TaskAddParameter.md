

# TaskAddParameter

Batch will retry tasks when a recovery operation is triggered on a compute node. Examples of recovery operations include (but are not limited to) when an unhealthy compute node is rebooted or a compute node disappeared due to host failure. Retries due to recovery operations are independent of and are not counted against the maxTaskRetryCount. Even if the maxTaskRetryCount is 0, an internal retry due to a recovery operation may occur. Because of this, all tasks should be idempotent. This means tasks need to tolerate being interrupted and restarted without causing any corruption or duplicate data. The best practice for long running tasks is to use some form of checkpointing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affinityInfo** | [**AffinityInformation**](AffinityInformation.md) |  |  [optional] |
|**applicationPackageReferences** | [**List&lt;ApplicationPackageReference&gt;**](ApplicationPackageReference.md) | Application packages are downloaded and deployed to a shared directory, not the task working directory. Therefore, if a referenced package is already on the compute node, and is up to date, then it is not re-downloaded; the existing copy on the compute node is used. If a referenced application package cannot be installed, for example because the package has been deleted or because download failed, the task fails. |  [optional] |
|**authenticationTokenSettings** | [**AuthenticationTokenSettings**](AuthenticationTokenSettings.md) |  |  [optional] |
|**commandLine** | **String** | For multi-instance tasks, the command line is executed as the primary task, after the primary task and all subtasks have finished executing the coordination command line. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. If the command line refers to file paths, it should use a relative path (relative to the task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables). |  |
|**constraints** | [**TaskConstraints**](TaskConstraints.md) |  |  [optional] |
|**containerSettings** | [**TaskContainerSettings**](TaskContainerSettings.md) |  |  [optional] |
|**dependsOn** | [**TaskDependencies**](TaskDependencies.md) |  |  [optional] |
|**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. |  [optional] |
|**environmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) |  |  [optional] |
|**exitConditions** | [**ExitConditions**](ExitConditions.md) |  |  [optional] |
|**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within a job that differ only by case). |  |
|**multiInstanceSettings** | [**MultiInstanceSettings**](MultiInstanceSettings.md) |  |  [optional] |
|**outputFiles** | [**List&lt;OutputFile&gt;**](OutputFile.md) | For multi-instance tasks, the files will only be uploaded from the compute node on which the primary task is executed. |  [optional] |
|**resourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | For multi-instance tasks, the resource files will only be downloaded to the compute node on which the primary task is executed. There is a maximum size for the list of resource files.  When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers. |  [optional] |
|**userIdentity** | [**UserIdentity**](UserIdentity.md) |  |  [optional] |



