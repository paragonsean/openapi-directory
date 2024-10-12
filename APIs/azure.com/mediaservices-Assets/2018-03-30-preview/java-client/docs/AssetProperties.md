

# AssetProperties

The Asset properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateId** | **String** | The alternate ID of the Asset. |  [optional] |
|**assetId** | **UUID** | The Asset ID. |  [optional] [readonly] |
|**container** | **String** | The name of the asset blob container. |  [optional] |
|**created** | **OffsetDateTime** | The creation date of the Asset. |  [optional] [readonly] |
|**description** | **String** | The Asset description. |  [optional] |
|**lastModified** | **OffsetDateTime** | The last modified date of the Asset. |  [optional] [readonly] |
|**storageAccountName** | **String** | The name of the storage account. |  [optional] |
|**storageEncryptionFormat** | [**StorageEncryptionFormatEnum**](#StorageEncryptionFormatEnum) | The Asset encryption format. One of None or MediaStorageEncryption. |  [optional] [readonly] |



## Enum: StorageEncryptionFormatEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| MEDIA_STORAGE_CLIENT_ENCRYPTION | &quot;MediaStorageClientEncryption&quot; |



