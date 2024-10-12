

# PolicyAssignmentProperties

The policy assignment properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | This message will be part of response in case of policy violation. |  [optional] |
|**displayName** | **String** | The display name of the policy assignment. |  [optional] |
|**enforcementMode** | [**EnforcementModeEnum**](#EnforcementModeEnum) | The policy assignment enforcement mode. Possible values are Default and DoNotEnforce. |  [optional] |
|**metadata** | **Object** | The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs. |  [optional] |
|**notScopes** | **List&lt;String&gt;** | The policy&#39;s excluded scopes. |  [optional] |
|**parameters** | [**Map&lt;String, ParameterValuesValue&gt;**](ParameterValuesValue.md) | The parameter values for the policy rule. The keys are the parameter names. |  [optional] |
|**policyDefinitionId** | **String** | The ID of the policy definition or policy set definition being assigned. |  [optional] |
|**scope** | **String** | The scope for the policy assignment. |  [optional] |



## Enum: EnforcementModeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| DO_NOT_ENFORCE | &quot;DoNotEnforce&quot; |



