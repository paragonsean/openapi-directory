

# NodeSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentKey** | [**AgentKey**](AgentKey.md) |  |  [optional] |
|**policyMode** | [**PolicyModeEnum**](#PolicyModeEnum) | In which mode the node will apply its configuration policy. Use &#x60;default&#x60; to use the global mode. |  [optional] |
|**properties** | [**List&lt;NodeAddInnerPropertiesInner&gt;**](NodeAddInnerPropertiesInner.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The node life cycle state. See [dedicated doc](https://docs.rudder.io/reference/current/usage/advanced_node_management.html#node-lifecycle) for more information. |  [optional] |



## Enum: PolicyModeEnum

| Name | Value |
|---- | -----|
| AUDIT | &quot;audit&quot; |
| ENFORCE | &quot;enforce&quot; |
| DEFAULT | &quot;default&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| IGNORED | &quot;ignored&quot; |
| EMPTY_POLICIES | &quot;empty-policies&quot; |
| INITIALIZING | &quot;initializing&quot; |
| PREPARING_EOL | &quot;preparing-eol&quot; |



