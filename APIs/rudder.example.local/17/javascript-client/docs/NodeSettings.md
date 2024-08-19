# RudderApi.NodeSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentKey** | [**AgentKey**](AgentKey.md) |  | [optional] 
**policyMode** | **String** | In which mode the node will apply its configuration policy. Use &#x60;default&#x60; to use the global mode. | [optional] 
**properties** | [**[NodeAddInnerPropertiesInner]**](NodeAddInnerPropertiesInner.md) |  | [optional] 
**state** | **String** | The node life cycle state. See [dedicated doc](https://docs.rudder.io/reference/current/usage/advanced_node_management.html#node-lifecycle) for more information. | [optional] 



## Enum: PolicyModeEnum


* `audit` (value: `"audit"`)

* `enforce` (value: `"enforce"`)

* `default` (value: `"default"`)





## Enum: StateEnum


* `enabled` (value: `"enabled"`)

* `ignored` (value: `"ignored"`)

* `empty-policies` (value: `"empty-policies"`)

* `initializing` (value: `"initializing"`)

* `preparing-eol` (value: `"preparing-eol"`)




