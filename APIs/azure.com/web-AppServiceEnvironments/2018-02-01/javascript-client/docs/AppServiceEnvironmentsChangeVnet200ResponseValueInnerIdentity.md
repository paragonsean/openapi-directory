# AppServiceEnvironmentsApiClient.AppServiceEnvironmentsChangeVnet200ResponseValueInnerIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | Principal Id of managed service identity. | [optional] [readonly] 
**tenantId** | **String** | Tenant of managed service identity. | [optional] [readonly] 
**type** | **String** | Type of managed service identity. | [optional] 
**userAssignedIdentities** | [**{String: AppServiceEnvironmentsChangeVnet200ResponseValueInnerIdentityUserAssignedIdentitiesValue}**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerIdentityUserAssignedIdentitiesValue.md) | The list of user assigned identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName} | [optional] 



## Enum: TypeEnum


* `SystemAssigned` (value: `"SystemAssigned"`)

* `UserAssigned` (value: `"UserAssigned"`)

* `SystemAssigned, UserAssigned` (value: `"SystemAssigned, UserAssigned"`)

* `None` (value: `"None"`)




