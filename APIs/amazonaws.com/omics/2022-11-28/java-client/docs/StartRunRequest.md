

# StartRunRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workflowId** | **String** | The run&#39;s workflow ID. |  [optional] |
|**workflowType** | [**WorkflowTypeEnum**](#WorkflowTypeEnum) | The run&#39;s workflows type. |  [optional] |
|**runId** | **String** | The run&#39;s ID. |  [optional] |
|**roleArn** | **String** | A service role for the run. |  |
|**name** | **String** | A name for the run. |  [optional] |
|**runGroupId** | **String** | The run&#39;s group ID. |  [optional] |
|**priority** | **Integer** | A priority for the run. |  [optional] |
|**parameters** | **Object** | Parameters for the run. |  [optional] |
|**storageCapacity** | **Integer** | A storage capacity for the run in gigabytes. |  [optional] |
|**outputUri** | **String** | An output URI for the run. |  [optional] |
|**logLevel** | [**LogLevelEnum**](#LogLevelEnum) | A log level for the run. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags for the run. |  [optional] |
|**requestId** | **String** | To ensure that requests don&#39;t run multiple times, specify a unique ID for each request. |  |



## Enum: WorkflowTypeEnum

| Name | Value |
|---- | -----|
| PRIVATE | &quot;PRIVATE&quot; |
| READY2_RUN | &quot;READY2RUN&quot; |



## Enum: LogLevelEnum

| Name | Value |
|---- | -----|
| OFF | &quot;OFF&quot; |
| FATAL | &quot;FATAL&quot; |
| ERROR | &quot;ERROR&quot; |
| ALL | &quot;ALL&quot; |



