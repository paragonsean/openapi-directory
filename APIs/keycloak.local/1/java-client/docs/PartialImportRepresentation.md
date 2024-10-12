

# PartialImportRepresentation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clients** | [**List&lt;ClientRepresentation&gt;**](ClientRepresentation.md) |  |  [optional] |
|**groups** | [**List&lt;GroupRepresentation&gt;**](GroupRepresentation.md) |  |  [optional] |
|**identityProviders** | [**List&lt;IdentityProviderRepresentation&gt;**](IdentityProviderRepresentation.md) |  |  [optional] |
|**ifResourceExists** | **String** |  |  [optional] |
|**policy** | [**PolicyEnum**](#PolicyEnum) |  |  [optional] |
|**roles** | [**RolesRepresentation**](RolesRepresentation.md) |  |  [optional] |
|**users** | [**List&lt;UserRepresentation&gt;**](UserRepresentation.md) |  |  [optional] |



## Enum: PolicyEnum

| Name | Value |
|---- | -----|
| SKIP | &quot;SKIP&quot; |
| OVERWRITE | &quot;OVERWRITE&quot; |
| FAIL | &quot;FAIL&quot; |



