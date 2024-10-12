

# StartTask

A task defined on a pool and run by compute nodes when they join the pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commandLine** | **String** | Gets or sets the command line of the start task. |  [optional] |
|**environmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | Gets or sets a list of environment variable settings for the start task. |  [optional] |
|**maxTaskRetryCount** | **Integer** | Gets or sets the maximum number of times the task may be retried. |  [optional] |
|**resourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | Gets or sets a list of files that Batch will download to the compute node before running the command line. |  [optional] |
|**runElevated** | **Boolean** | Gets or sets whether to run the start task in elevated mode. The default value is false. |  [optional] |
|**waitForSuccess** | **Boolean** | Gets or sets whether the Batch Service should wait for the start task to complete successfully (that is, to exit with exit code 0) before scheduling any tasks on the compute node. |  [optional] |



