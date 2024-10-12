# ApiManagementClient.ApiManagementServiceIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | The principal id of the identity. | [optional] [readonly] 
**tenantId** | **String** | The client tenant id of the identity. | [optional] [readonly] 
**type** | **String** | The type of identity used for the resource. The type &#39;SystemAssigned, UserAssigned&#39; includes both an implicitly created identity and a set of user assigned identities. The type &#39;None&#39; will remove any identities from the service. | 
**userAssignedIdentities** | [**{String: ApiManagementServiceIdentityUserAssignedIdentitiesValue}**](ApiManagementServiceIdentityUserAssignedIdentitiesValue.md) |  | [optional] 



## Enum: TypeEnum


* `SystemAssigned` (value: `"SystemAssigned"`)

* `UserAssigned` (value: `"UserAssigned"`)

* `SystemAssigned, UserAssigned` (value: `"SystemAssigned, UserAssigned"`)

* `None` (value: `"None"`)




