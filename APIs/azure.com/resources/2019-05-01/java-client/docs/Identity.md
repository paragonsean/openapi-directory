

# Identity

Identity for the resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | The principal ID of resource identity. |  [optional] [readonly] |
|**tenantId** | **String** | The tenant ID of resource. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The identity type. |  [optional] |
|**userAssignedIdentities** | [**Map&lt;String, IdentityUserAssignedIdentitiesValue&gt;**](IdentityUserAssignedIdentitiesValue.md) | The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&#39;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |
| USER_ASSIGNED | &quot;UserAssigned&quot; |
| SYSTEM_ASSIGNED_USER_ASSIGNED | &quot;SystemAssigned, UserAssigned&quot; |
| NONE | &quot;None&quot; |



