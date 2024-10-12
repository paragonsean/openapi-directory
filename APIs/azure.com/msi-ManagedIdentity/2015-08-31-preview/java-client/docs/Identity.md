

# Identity

Describes an identity resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The id of the created identity. |  [optional] [readonly] |
|**location** | **String** | The Azure region where the identity lives. |  [optional] |
|**name** | **String** | The name of the created identity. |  [optional] [readonly] |
|**properties** | [**IdentityProperties**](IdentityProperties.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Resource tags |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of resource i.e. Microsoft.ManagedIdentity/userAssignedIdentities |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MICROSOFT_MANAGED_IDENTITY_USER_ASSIGNED_IDENTITIES | &quot;Microsoft.ManagedIdentity/userAssignedIdentities&quot; |



