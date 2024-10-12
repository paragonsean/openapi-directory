

# PolicySetDefinitionProperties

The policy set definition properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The policy set definition description. |  [optional] |
|**displayName** | **String** | The display name of the policy set definition. |  [optional] |
|**metadata** | **Object** | The policy set definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs. |  [optional] |
|**parameters** | [**Map&lt;String, PolicySetDefinitionPropertiesParametersValue&gt;**](PolicySetDefinitionPropertiesParametersValue.md) | The parameter definitions for parameters used in the policy. The keys are the parameter names. |  [optional] |
|**policyDefinitionGroups** | [**List&lt;PolicyDefinitionGroup&gt;**](PolicyDefinitionGroup.md) | The metadata describing groups of policy definition references within the policy set definition. |  [optional] |
|**policyDefinitions** | [**List&lt;PolicyDefinitionReference&gt;**](PolicyDefinitionReference.md) | An array of policy definition references. |  |
|**policyType** | [**PolicyTypeEnum**](#PolicyTypeEnum) | The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. |  [optional] |



## Enum: PolicyTypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| BUILT_IN | &quot;BuiltIn&quot; |
| CUSTOM | &quot;Custom&quot; |
| STATIC | &quot;Static&quot; |



