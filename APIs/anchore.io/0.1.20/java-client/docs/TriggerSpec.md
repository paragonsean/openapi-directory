

# TriggerSpec

Definition of a trigger and its parameters

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Trigger description for what it tests and when it will fire during evaluation |  [optional] |
|**name** | **String** | Name of the trigger as it would appear in a policy document |  [optional] |
|**parameters** | [**List&lt;TriggerParamSpec&gt;**](TriggerParamSpec.md) | The list of parameters that are valid for this trigger |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the trigger |  [optional] |
|**supercededBy** | **String** | The name of another trigger that supercedes this on functionally if this is deprecated |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DEPRECATED | &quot;deprecated&quot; |
| EOL | &quot;eol&quot; |



