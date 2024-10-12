

# JobManagerTask

Specifies details of a Job Manager task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commandLine** | **String** | The command line of the Job Manager task. |  [optional] |
|**constraints** | [**TaskConstraints**](TaskConstraints.md) |  |  [optional] |
|**displayName** | **String** | The display name of the Job Manager task. |  [optional] |
|**environmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | A list of environment variable settings for the Job Manager task. |  [optional] |
|**id** | **String** | A string that uniquely identifies the Job Manager task. A GUID is recommended. |  [optional] |
|**killJobOnCompletion** | **Boolean** | Whether completion of the Job Manager task signifies completion of the entire job. |  [optional] |
|**resourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | A list of files that the Batch service will download to the compute node before running the command line. |  [optional] |
|**runElevated** | **Boolean** | Whether to run the Job Manager task in elevated mode. The default value is false. |  [optional] |
|**runExclusive** | **Boolean** | Whether the Job Manager task requires exclusive use of the compute node where it runs. If true, no other tasks will run on the same compute node for as long as the Job Manager is running. If false, other tasks can run simultaneously with the Job Manager on a compute node. (The Job Manager task counts normally against the node&#39;s concurrent task limit, so this is only relevant if the node allows multiple concurrent tasks.) |  [optional] |



