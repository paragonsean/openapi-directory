# CloudRunAdminApi.Overrides

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerOverrides** | [**[ContainerOverride]**](ContainerOverride.md) | Per container override specification. | [optional] 
**taskCount** | **Number** | The desired number of tasks the execution should run. Will replace existing task_count value. | [optional] 
**timeoutSeconds** | **Number** | Duration in seconds the task may be active before the system will actively try to mark it failed and kill associated containers. Will replace existing timeout_seconds value. | [optional] 


