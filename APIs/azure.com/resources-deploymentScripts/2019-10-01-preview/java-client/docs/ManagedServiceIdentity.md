

# ManagedServiceIdentity

Managed identity generic object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Type of the managed identity. |  [optional] |
|**userAssignedIdentities** | [**Map&lt;String, UserAssignedIdentity&gt;**](UserAssignedIdentity.md) | The list of user-assigned managed identities associated with the resource. Key is the Azure resource Id of the managed identity. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER_ASSIGNED | &quot;UserAssigned&quot; |



