

# PolicyRule

A rule that defines and decision value if the match is found true for a given image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  |
|**gate** | **String** |  |  |
|**id** | **String** |  |  [optional] |
|**params** | [**List&lt;PolicyRuleParamsInner&gt;**](PolicyRuleParamsInner.md) |  |  [optional] |
|**trigger** | **String** |  |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| GO | &quot;GO&quot; |
| STOP | &quot;STOP&quot; |
| WARN | &quot;WARN&quot; |



