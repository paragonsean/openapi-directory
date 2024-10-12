# AppConfigurationManagementClient.ResourceIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | The principal id of the identity. This property will only be provided for a system-assigned identity. | [optional] [readonly] 
**tenantId** | **String** | The tenant id associated with the resource&#39;s identity. This property will only be provided for a system-assigned identity. | [optional] [readonly] 
**type** | **String** | The type of managed identity used. The type &#39;SystemAssigned, UserAssigned&#39; includes both an implicitly created identity and a set of user-assigned identities. The type &#39;None&#39; will remove any identities. | [optional] 
**userAssignedIdentities** | [**{String: UserIdentity}**](UserIdentity.md) | The list of user-assigned identities associated with the resource. The user-assigned identity dictionary keys will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&#39;. | [optional] 



## Enum: TypeEnum


* `None` (value: `"None"`)

* `SystemAssigned` (value: `"SystemAssigned"`)

* `UserAssigned` (value: `"UserAssigned"`)

* `SystemAssigned, UserAssigned` (value: `"SystemAssigned, UserAssigned"`)




