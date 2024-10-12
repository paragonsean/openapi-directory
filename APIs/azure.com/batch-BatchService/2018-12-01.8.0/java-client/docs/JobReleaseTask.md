

# JobReleaseTask

The Job Release task runs when the job ends, because of one of the following: The user calls the Terminate Job API, or the Delete Job API while the job is still active, the job's maximum wall clock time constraint is reached, and the job is still active, or the job's Job Manager task completed, and the job is configured to terminate when the Job Manager completes. The Job Release task runs on each compute node where tasks of the job have run and the Job Preparation task ran and completed. If you reimage a compute node after it has run the Job Preparation task, and the job ends without any further tasks of the job running on that compute node (and hence the Job Preparation task does not re-run), then the Job Release task does not run on that node. If a compute node reboots while the Job Release task is still running, the Job Release task runs again when the compute node starts up. The job is not marked as complete until all Job Release tasks have completed. The Job Release task runs in the background. It does not occupy a scheduling slot; that is, it does not count towards the maxTasksPerNode limit specified on the pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commandLine** | **String** | The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. If the command line refers to file paths, it should use a relative path (relative to the task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables). |  |
|**containerSettings** | [**TaskContainerSettings**](TaskContainerSettings.md) |  |  [optional] |
|**environmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) |  |  [optional] |
|**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters. If you do not specify this property, the Batch service assigns a default value of &#39;jobrelease&#39;. No other task in the job can have the same ID as the Job Release task. If you try to submit a task with the same id, the Batch service rejects the request with error code TaskIdSameAsJobReleaseTask; if you are calling the REST API directly, the HTTP status code is 409 (Conflict). |  [optional] |
|**maxWallClockTime** | **String** |  |  [optional] |
|**resourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | Files listed under this element are located in the task&#39;s working directory. |  [optional] |
|**retentionTime** | **String** | The default is 7 days, i.e. the task directory will be retained for 7 days unless the compute node is removed or the job is deleted. |  [optional] |
|**userIdentity** | [**UserIdentity**](UserIdentity.md) |  |  [optional] |



