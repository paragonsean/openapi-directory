

# AgentInfo

VM Agent Info.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | **String** | Optional. The assigned Job ID |  [optional] |
|**reportTime** | **String** | When the AgentInfo is generated. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Agent state. |  [optional] |
|**taskGroupId** | **String** | The assigned task group ID. |  [optional] |
|**tasks** | [**List&lt;AgentTaskInfo&gt;**](AgentTaskInfo.md) | Task Info. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;AGENT_STATE_UNSPECIFIED&quot; |
| STARTING | &quot;AGENT_STARTING&quot; |
| RUNNING | &quot;AGENT_RUNNING&quot; |
| STOPPED | &quot;AGENT_STOPPED&quot; |



