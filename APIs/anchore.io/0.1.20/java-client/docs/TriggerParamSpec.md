

# TriggerParamSpec


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  |  [optional] |
|**example** | **String** | An example value for the parameter (encoded as a string if the parameter is an object or list type) |  [optional] |
|**name** | **String** | Parameter name as it appears in policy document |  [optional] |
|**required** | **Boolean** | Is this a required parameter or optional |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the trigger parameter |  [optional] |
|**supercededBy** | **String** | The name of another trigger that supercedes this on functionally if this is deprecated |  [optional] |
|**validator** | **Object** | If present, a definition for validation of input. Typically a jsonschema object that can be used to validate an input against. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DEPRECATED | &quot;deprecated&quot; |
| EOL | &quot;eol&quot; |



