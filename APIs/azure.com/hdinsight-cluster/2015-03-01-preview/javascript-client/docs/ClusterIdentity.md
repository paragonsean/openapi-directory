# HdInsightManagementClient.ClusterIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | The principal id of cluster identity. This property will only be provided for a system assigned identity. | [optional] [readonly] 
**tenantId** | **String** | The tenant id associated with the cluster. This property will only be provided for a system assigned identity. | [optional] [readonly] 
**type** | **String** | The type of identity used for the cluster. The type &#39;SystemAssigned, UserAssigned&#39; includes both an implicitly created identity and a set of user assigned identities. | [optional] 
**userAssignedIdentities** | [**{String: ClusterIdentityUserAssignedIdentitiesValue}**](ClusterIdentityUserAssignedIdentitiesValue.md) | The list of user identities associated with the cluster. The user identity dictionary key references will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&#39;. | [optional] 



## Enum: TypeEnum


* `SystemAssigned` (value: `"SystemAssigned"`)

* `UserAssigned` (value: `"UserAssigned"`)

* `SystemAssigned, UserAssigned` (value: `"SystemAssigned, UserAssigned"`)

* `None` (value: `"None"`)




