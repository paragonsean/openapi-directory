# AnchoreEngineApiServer.TriggerParamSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** |  | [optional] 
**example** | **String** | An example value for the parameter (encoded as a string if the parameter is an object or list type) | [optional] 
**name** | **String** | Parameter name as it appears in policy document | [optional] 
**required** | **Boolean** | Is this a required parameter or optional | [optional] 
**state** | **String** | State of the trigger parameter | [optional] 
**supercededBy** | **String** | The name of another trigger that supercedes this on functionally if this is deprecated | [optional] 
**validator** | **Object** | If present, a definition for validation of input. Typically a jsonschema object that can be used to validate an input against. | [optional] 



## Enum: StateEnum


* `active` (value: `"active"`)

* `deprecated` (value: `"deprecated"`)

* `eol` (value: `"eol"`)




