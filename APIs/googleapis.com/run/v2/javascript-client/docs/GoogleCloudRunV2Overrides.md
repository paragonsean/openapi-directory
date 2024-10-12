# CloudRunAdminApi.GoogleCloudRunV2Overrides

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerOverrides** | [**[GoogleCloudRunV2ContainerOverride]**](GoogleCloudRunV2ContainerOverride.md) | Per container override specification. | [optional] 
**taskCount** | **Number** | Optional. The desired number of tasks the execution should run. Will replace existing task_count value. | [optional] 
**timeout** | **String** | Duration in seconds the task may be active before the system will actively try to mark it failed and kill associated containers. Will replace existing timeout_seconds value. | [optional] 


