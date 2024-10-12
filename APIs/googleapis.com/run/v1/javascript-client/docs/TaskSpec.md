# CloudRunAdminApi.TaskSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**[Container]**](Container.md) | Optional. List of containers belonging to the task. We disallow a number of fields on this Container. | [optional] 
**maxRetries** | **Number** | Optional. Number of retries allowed per task, before marking this job failed. Defaults to 3. | [optional] 
**serviceAccountName** | **String** | Optional. Email address of the IAM service account associated with the task of a job execution. The service account represents the identity of the running task, and determines what permissions the task has. If not provided, the task will use the project&#39;s default service account. | [optional] 
**timeoutSeconds** | **String** | Optional. Duration in seconds the task may be active before the system will actively try to mark it failed and kill associated containers. This applies per attempt of a task, meaning each retry can run for the full timeout. Defaults to 600 seconds. | [optional] 
**volumes** | [**[Volume]**](Volume.md) | Optional. List of volumes that can be mounted by containers belonging to the task. | [optional] 


