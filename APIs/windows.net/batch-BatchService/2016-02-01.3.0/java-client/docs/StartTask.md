

# StartTask

A task which is run when a compute node joins a pool in the Azure Batch service, or when the compute node is rebooted or reimaged.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commandLine** | **String** | The command line of the start task. |  [optional] |
|**environmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | A list of environment variable settings for the start task. |  [optional] |
|**maxTaskRetryCount** | **Integer** | The maximum number of times the task may be retried. |  [optional] |
|**resourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | A list of files that the Batch service will download to the compute node before running the command line. |  [optional] |
|**runElevated** | **Boolean** | Whether to run the start task in elevated mode. The default value is false. |  [optional] |
|**waitForSuccess** | **Boolean** | Whether the Batch service should wait for the start task to complete successfully (that is, to exit with exit code 0) before scheduling any tasks on the compute node. |  [optional] |



