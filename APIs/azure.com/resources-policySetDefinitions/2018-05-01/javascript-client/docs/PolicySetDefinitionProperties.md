# PolicyClient.PolicySetDefinitionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The policy set definition description. | [optional] 
**displayName** | **String** | The display name of the policy set definition. | [optional] 
**metadata** | **Object** | The policy set definition metadata. | [optional] 
**parameters** | **Object** | The policy set definition parameters that can be used in policy definition references. | [optional] 
**policyDefinitions** | [**[PolicyDefinitionReference]**](PolicyDefinitionReference.md) | An array of policy definition references. | 
**policyType** | **String** | The type of policy definition. Possible values are NotSpecified, BuiltIn, and Custom. | [optional] 



## Enum: PolicyTypeEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `BuiltIn` (value: `"BuiltIn"`)

* `Custom` (value: `"Custom"`)




