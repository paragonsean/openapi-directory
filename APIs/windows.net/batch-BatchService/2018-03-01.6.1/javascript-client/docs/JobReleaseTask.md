# BatchService.JobReleaseTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commandLine** | **String** | The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. If the command line refers to file paths, it should use a relative path (relative to the task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables). | 
**containerSettings** | [**TaskContainerSettings**](TaskContainerSettings.md) |  | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) |  | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters. If you do not specify this property, the Batch service assigns a default value of &#39;jobrelease&#39;. No other task in the job can have the same ID as the Job Release task. If you try to submit a task with the same id, the Batch service rejects the request with error code TaskIdSameAsJobReleaseTask; if you are calling the REST API directly, the HTTP status code is 409 (Conflict). | [optional] 
**maxWallClockTime** | **String** |  | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | Files listed under this element are located in the task&#39;s working directory. | [optional] 
**retentionTime** | **String** | The default is infinite, i.e. the task directory will be retained until the compute node is removed or reimaged. | [optional] 
**userIdentity** | [**UserIdentity**](UserIdentity.md) |  | [optional] 


