# BlueprintClient.RoleAssignmentArtifactProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalIds** | **Object** | Array of user or group identities in Azure Active Directory. The roleDefinition will apply to these identity. | 
**resourceGroup** | **String** | RoleAssignment will be scope to this resourceGroup, if left empty, it would scope to the subscription. | [optional] 
**roleDefinitionId** | **String** | Azure resource ID of the RoleDefinition. | 
**description** | **String** | Multi-line explain this resource. | [optional] 
**displayName** | **String** | One-liner string explain this resource. | [optional] 
**dependsOn** | **[String]** | Artifacts which need to be deployed before the specified artifact. | [optional] 


