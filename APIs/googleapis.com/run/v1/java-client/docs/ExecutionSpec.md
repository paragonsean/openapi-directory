

# ExecutionSpec

ExecutionSpec describes how the execution will look.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parallelism** | **Integer** | Optional. Specifies the maximum desired number of tasks the execution should run at given time. Must be &lt;&#x3D; task_count. When the job is run, if this field is 0 or unset, the maximum possible value will be used for that execution. The actual number of tasks running in steady state will be less than this number when there are fewer tasks waiting to be completed, i.e. when the work left to do is less than max parallelism. |  [optional] |
|**taskCount** | **Integer** | Optional. Specifies the desired number of tasks the execution should run. Setting to 1 means that parallelism is limited to 1 and the success of that task signals the success of the execution. Defaults to 1. |  [optional] |
|**template** | [**TaskTemplateSpec**](TaskTemplateSpec.md) |  |  [optional] |



