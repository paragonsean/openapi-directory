

# StorageAccountCredentialProperties

The storage account credential properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountKey** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  |  [optional] |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Type of storage accessed on the storage account. |  |
|**alias** | **String** | Alias for the storage account. |  |
|**blobDomainName** | **String** | Blob end point for private clouds. |  [optional] |
|**connectionString** | **String** | Connection string for the storage account. Use this string if username and account key are not specified. |  [optional] |
|**sslStatus** | [**SslStatusEnum**](#SslStatusEnum) | Signifies whether SSL needs to be enabled or not. |  |
|**userName** | **String** | Username for the storage account. |  [optional] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| GENERAL_PURPOSE_STORAGE | &quot;GeneralPurposeStorage&quot; |
| BLOB_STORAGE | &quot;BlobStorage&quot; |



## Enum: SslStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



