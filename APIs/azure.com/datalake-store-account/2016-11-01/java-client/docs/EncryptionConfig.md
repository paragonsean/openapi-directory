

# EncryptionConfig

The encryption configuration for the account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyVaultMetaInfo** | [**KeyVaultMetaInfo**](KeyVaultMetaInfo.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of encryption configuration being used. Currently the only supported types are &#39;UserManaged&#39; and &#39;ServiceManaged&#39;. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER_MANAGED | &quot;UserManaged&quot; |
| SERVICE_MANAGED | &quot;ServiceManaged&quot; |



