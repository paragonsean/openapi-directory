# BlueprintClient.ManagedServiceIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | Azure Active Directory principal ID associated with this Identity. | [optional] 
**tenantId** | **String** | ID of the Azure Active Directory. | [optional] 
**type** | **String** | Type of the managed identity. | 
**userAssignedIdentities** | [**{String: UserAssignedIdentity}**](UserAssignedIdentity.md) | The list of user-assigned managed identities associated with the resource. Key is the Azure resource Id of the managed identity. | [optional] 



## Enum: TypeEnum


* `None` (value: `"None"`)

* `SystemAssigned` (value: `"SystemAssigned"`)

* `UserAssigned` (value: `"UserAssigned"`)




