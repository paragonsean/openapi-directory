

# GoogleCloudRunV2TaskTemplate

TaskTemplate describes the data a task should have when created from a template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containers** | [**List&lt;GoogleCloudRunV2Container&gt;**](GoogleCloudRunV2Container.md) | Holds the single container that defines the unit of execution for this task. |  [optional] |
|**encryptionKey** | **String** | A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |  [optional] |
|**executionEnvironment** | [**ExecutionEnvironmentEnum**](#ExecutionEnvironmentEnum) | The execution environment being used to host this Task. |  [optional] |
|**maxRetries** | **Integer** | Number of retries allowed per Task, before marking this Task failed. Defaults to 3. |  [optional] |
|**serviceAccount** | **String** | Email address of the IAM service account associated with the Task of a Job. The service account represents the identity of the running task, and determines what permissions the task has. If not provided, the task will use the project&#39;s default service account. |  [optional] |
|**timeout** | **String** | Max allowed time duration the Task may be active before the system will actively try to mark it failed and kill associated containers. This applies per attempt of a task, meaning each retry can run for the full timeout. Defaults to 600 seconds. |  [optional] |
|**volumes** | [**List&lt;GoogleCloudRunV2Volume&gt;**](GoogleCloudRunV2Volume.md) | A list of Volumes to make available to containers. |  [optional] |
|**vpcAccess** | [**GoogleCloudRunV2VpcAccess**](GoogleCloudRunV2VpcAccess.md) |  |  [optional] |



## Enum: ExecutionEnvironmentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;EXECUTION_ENVIRONMENT_UNSPECIFIED&quot; |
| GEN1 | &quot;EXECUTION_ENVIRONMENT_GEN1&quot; |
| GEN2 | &quot;EXECUTION_ENVIRONMENT_GEN2&quot; |



