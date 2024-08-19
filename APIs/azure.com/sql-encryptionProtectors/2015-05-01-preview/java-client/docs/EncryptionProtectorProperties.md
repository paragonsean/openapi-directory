

# EncryptionProtectorProperties

Properties for an encryption protector execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serverKeyName** | **String** | The name of the server key. |  [optional] |
|**serverKeyType** | [**ServerKeyTypeEnum**](#ServerKeyTypeEnum) | The encryption protector type like &#39;ServiceManaged&#39;, &#39;AzureKeyVault&#39;. |  |
|**subregion** | **String** | Subregion of the encryption protector. |  [optional] [readonly] |
|**thumbprint** | **String** | Thumbprint of the server key. |  [optional] [readonly] |
|**uri** | **String** | The URI of the server key. |  [optional] [readonly] |



## Enum: ServerKeyTypeEnum

| Name | Value |
|---- | -----|
| SERVICE_MANAGED | &quot;ServiceManaged&quot; |
| AZURE_KEY_VAULT | &quot;AzureKeyVault&quot; |



