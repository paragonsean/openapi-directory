

# AgentPool

Represents an On-Premises Agent pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidthLimit** | [**BandwidthLimit**](BandwidthLimit.md) |  |  [optional] |
|**displayName** | **String** | Specifies the client-specified AgentPool description. |  [optional] |
|**name** | **String** | Required. Specifies a unique string that identifies the agent pool. Format: &#x60;projects/{project_id}/agentPools/{agent_pool_id}&#x60; |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Specifies the state of the AgentPool. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| CREATED | &quot;CREATED&quot; |
| DELETING | &quot;DELETING&quot; |



