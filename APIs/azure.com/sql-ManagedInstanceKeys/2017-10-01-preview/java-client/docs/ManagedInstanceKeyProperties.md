

# ManagedInstanceKeyProperties

Properties for a key execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **OffsetDateTime** | The key creation date. |  [optional] [readonly] |
|**serverKeyType** | [**ServerKeyTypeEnum**](#ServerKeyTypeEnum) | The key type like &#39;ServiceManaged&#39;, &#39;AzureKeyVault&#39;. |  |
|**thumbprint** | **String** | Thumbprint of the key. |  [optional] [readonly] |
|**uri** | **String** | The URI of the key. If the ServerKeyType is AzureKeyVault, then the URI is required. |  [optional] |



## Enum: ServerKeyTypeEnum

| Name | Value |
|---- | -----|
| SERVICE_MANAGED | &quot;ServiceManaged&quot; |
| AZURE_KEY_VAULT | &quot;AzureKeyVault&quot; |



