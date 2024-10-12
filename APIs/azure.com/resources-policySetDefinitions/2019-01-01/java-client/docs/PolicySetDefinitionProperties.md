

# PolicySetDefinitionProperties

The policy set definition properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The policy set definition description. |  [optional] |
|**displayName** | **String** | The display name of the policy set definition. |  [optional] |
|**metadata** | **Object** | The policy set definition metadata. |  [optional] |
|**parameters** | **Object** | The policy set definition parameters that can be used in policy definition references. |  [optional] |
|**policyDefinitions** | [**List&lt;PolicyDefinitionReference&gt;**](PolicyDefinitionReference.md) | An array of policy definition references. |  |
|**policyType** | [**PolicyTypeEnum**](#PolicyTypeEnum) | The type of policy definition. Possible values are NotSpecified, BuiltIn, and Custom. |  [optional] |



## Enum: PolicyTypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| BUILT_IN | &quot;BuiltIn&quot; |
| CUSTOM | &quot;Custom&quot; |



