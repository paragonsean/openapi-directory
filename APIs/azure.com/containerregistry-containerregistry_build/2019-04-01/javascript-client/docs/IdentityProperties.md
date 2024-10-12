# ContainerRegistryManagementClient.IdentityProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | The principal ID of resource identity. | [optional] 
**tenantId** | **String** | The tenant ID of resource. | [optional] 
**type** | **String** | The identity type. | [optional] 
**userAssignedIdentities** | [**{String: UserIdentityProperties}**](UserIdentityProperties.md) | The list of user identities associated with the resource. The user identity   dictionary key references will be ARM resource ids in the form:   &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/      providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&#39;. | [optional] 



## Enum: TypeEnum


* `SystemAssigned` (value: `"SystemAssigned"`)

* `UserAssigned` (value: `"UserAssigned"`)

* `SystemAssigned, UserAssigned` (value: `"SystemAssigned, UserAssigned"`)

* `None` (value: `"None"`)




