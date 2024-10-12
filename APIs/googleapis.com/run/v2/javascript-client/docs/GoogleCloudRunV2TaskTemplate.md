# CloudRunAdminApi.GoogleCloudRunV2TaskTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**[GoogleCloudRunV2Container]**](GoogleCloudRunV2Container.md) | Holds the single container that defines the unit of execution for this task. | [optional] 
**encryptionKey** | **String** | A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek | [optional] 
**executionEnvironment** | **String** | The execution environment being used to host this Task. | [optional] 
**maxRetries** | **Number** | Number of retries allowed per Task, before marking this Task failed. Defaults to 3. | [optional] 
**serviceAccount** | **String** | Email address of the IAM service account associated with the Task of a Job. The service account represents the identity of the running task, and determines what permissions the task has. If not provided, the task will use the project&#39;s default service account. | [optional] 
**timeout** | **String** | Max allowed time duration the Task may be active before the system will actively try to mark it failed and kill associated containers. This applies per attempt of a task, meaning each retry can run for the full timeout. Defaults to 600 seconds. | [optional] 
**volumes** | [**[GoogleCloudRunV2Volume]**](GoogleCloudRunV2Volume.md) | A list of Volumes to make available to containers. | [optional] 
**vpcAccess** | [**GoogleCloudRunV2VpcAccess**](GoogleCloudRunV2VpcAccess.md) |  | [optional] 



## Enum: ExecutionEnvironmentEnum


* `UNSPECIFIED` (value: `"EXECUTION_ENVIRONMENT_UNSPECIFIED"`)

* `GEN1` (value: `"EXECUTION_ENVIRONMENT_GEN1"`)

* `GEN2` (value: `"EXECUTION_ENVIRONMENT_GEN2"`)




