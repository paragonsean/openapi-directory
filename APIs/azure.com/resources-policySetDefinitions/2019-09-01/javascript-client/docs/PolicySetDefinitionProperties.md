# PolicyClient.PolicySetDefinitionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The policy set definition description. | [optional] 
**displayName** | **String** | The display name of the policy set definition. | [optional] 
**metadata** | **Object** | The policy set definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs. | [optional] 
**parameters** | [**{String: PolicySetDefinitionPropertiesParametersValue}**](PolicySetDefinitionPropertiesParametersValue.md) | The parameter definitions for parameters used in the policy. The keys are the parameter names. | [optional] 
**policyDefinitionGroups** | [**[PolicyDefinitionGroup]**](PolicyDefinitionGroup.md) | The metadata describing groups of policy definition references within the policy set definition. | [optional] 
**policyDefinitions** | [**[PolicyDefinitionReference]**](PolicyDefinitionReference.md) | An array of policy definition references. | 
**policyType** | **String** | The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. | [optional] 



## Enum: PolicyTypeEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `BuiltIn` (value: `"BuiltIn"`)

* `Custom` (value: `"Custom"`)

* `Static` (value: `"Static"`)




