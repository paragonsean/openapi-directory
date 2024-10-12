

# ServerKeyProperties

Properties for a key execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **OffsetDateTime** | The key creation date. |  [optional] [readonly] |
|**serverKeyType** | [**ServerKeyTypeEnum**](#ServerKeyTypeEnum) | The key type like  &#39;AzureKeyVault&#39;. |  |
|**uri** | **String** | The URI of the key. |  [optional] |



## Enum: ServerKeyTypeEnum

| Name | Value |
|---- | -----|
| AZURE_KEY_VAULT | &quot;AzureKeyVault&quot; |



