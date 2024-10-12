

# GoogleCloudRunV2Overrides

RunJob Overrides that contains Execution fields to be overridden.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerOverrides** | [**List&lt;GoogleCloudRunV2ContainerOverride&gt;**](GoogleCloudRunV2ContainerOverride.md) | Per container override specification. |  [optional] |
|**taskCount** | **Integer** | Optional. The desired number of tasks the execution should run. Will replace existing task_count value. |  [optional] |
|**timeout** | **String** | Duration in seconds the task may be active before the system will actively try to mark it failed and kill associated containers. Will replace existing timeout_seconds value. |  [optional] |



