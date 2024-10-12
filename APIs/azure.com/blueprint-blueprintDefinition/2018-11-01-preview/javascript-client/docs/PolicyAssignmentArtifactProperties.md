# BlueprintClient.PolicyAssignmentArtifactProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**{String: ParameterValue}**](ParameterValue.md) | A dictionary for parameters and their corresponding values. | 
**policyDefinitionId** | **String** | Azure resource ID of the policy definition. | 
**resourceGroup** | **String** | Name of the resource group placeholder to which the policy will be assigned. | [optional] 
**description** | **String** | Multi-line explain this resource. | [optional] 
**displayName** | **String** | One-liner string explain this resource. | [optional] 
**dependsOn** | **[String]** | Artifacts which need to be deployed before the specified artifact. | [optional] 


