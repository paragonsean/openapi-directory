

# ManagedServiceIdentity

Managed identity generic object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | Azure Active Directory principal ID associated with this Identity. |  [optional] |
|**tenantId** | **String** | ID of the Azure Active Directory. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the managed identity. |  |
|**userAssignedIdentities** | [**Map&lt;String, UserAssignedIdentity&gt;**](UserAssignedIdentity.md) | The list of user-assigned managed identities associated with the resource. Key is the Azure resource Id of the managed identity. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |
| USER_ASSIGNED | &quot;UserAssigned&quot; |



