# AnchoreEngineApiServer.TriggerSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Trigger description for what it tests and when it will fire during evaluation | [optional] 
**name** | **String** | Name of the trigger as it would appear in a policy document | [optional] 
**parameters** | [**[TriggerParamSpec]**](TriggerParamSpec.md) | The list of parameters that are valid for this trigger | [optional] 
**state** | **String** | State of the trigger | [optional] 
**supercededBy** | **String** | The name of another trigger that supercedes this on functionally if this is deprecated | [optional] 



## Enum: StateEnum


* `active` (value: `"active"`)

* `deprecated` (value: `"deprecated"`)

* `eol` (value: `"eol"`)




