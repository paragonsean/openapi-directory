

# GateSpec

A description of the set of gates available in this engine and the triggers and parameters supported

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the gate |  [optional] |
|**name** | **String** | Gate name, as it would appear in a policy document |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the gate and transitively all triggers it contains if not &#39;active&#39; |  [optional] |
|**supercededBy** | **String** | The name of another trigger that supercedes this on functionally if this is deprecated |  [optional] |
|**triggers** | [**List&lt;TriggerSpec&gt;**](TriggerSpec.md) | List of the triggers that can fire for this Gate |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DEPRECATED | &quot;deprecated&quot; |
| EOL | &quot;eol&quot; |



