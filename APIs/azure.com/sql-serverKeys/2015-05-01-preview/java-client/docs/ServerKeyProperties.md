

# ServerKeyProperties

Properties for a server key execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **OffsetDateTime** | The server key creation date. |  [optional] |
|**serverKeyType** | [**ServerKeyTypeEnum**](#ServerKeyTypeEnum) | The server key type like &#39;ServiceManaged&#39;, &#39;AzureKeyVault&#39;. |  |
|**subregion** | **String** | Subregion of the server key. |  [optional] [readonly] |
|**thumbprint** | **String** | Thumbprint of the server key. |  [optional] |
|**uri** | **String** | The URI of the server key. |  [optional] |



## Enum: ServerKeyTypeEnum

| Name | Value |
|---- | -----|
| SERVICE_MANAGED | &quot;ServiceManaged&quot; |
| AZURE_KEY_VAULT | &quot;AzureKeyVault&quot; |



