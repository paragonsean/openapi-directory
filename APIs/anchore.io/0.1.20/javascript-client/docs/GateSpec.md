# AnchoreEngineApiServer.GateSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the gate | [optional] 
**name** | **String** | Gate name, as it would appear in a policy document | [optional] 
**state** | **String** | State of the gate and transitively all triggers it contains if not &#39;active&#39; | [optional] 
**supercededBy** | **String** | The name of another trigger that supercedes this on functionally if this is deprecated | [optional] 
**triggers** | [**[TriggerSpec]**](TriggerSpec.md) | List of the triggers that can fire for this Gate | [optional] 



## Enum: StateEnum


* `active` (value: `"active"`)

* `deprecated` (value: `"deprecated"`)

* `eol` (value: `"eol"`)




