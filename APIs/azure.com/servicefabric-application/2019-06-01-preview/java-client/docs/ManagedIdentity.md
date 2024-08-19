

# ManagedIdentity

Describes the managed identities for an Azure resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | The principal id of the managed identity. This property will only be provided for a system assigned identity. |  [optional] [readonly] |
|**tenantId** | **String** | The tenant id of the managed identity. This property will only be provided for a system assigned identity. |  [optional] [readonly] |
|**type** | **ManagedIdentityType** |  |  [optional] |
|**userAssignedIdentities** | [**Map&lt;String, UserAssignedIdentity&gt;**](UserAssignedIdentity.md) | The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&#39;.  |  [optional] |



