# DataBoxEdgeManagementClient.StorageAccountCredentialProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountKey** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  | [optional] 
**accountType** | **String** | Type of storage accessed on the storage account. | 
**alias** | **String** | Alias for the storage account. | 
**blobDomainName** | **String** | Blob end point for private clouds. | [optional] 
**connectionString** | **String** | Connection string for the storage account. Use this string if username and account key are not specified. | [optional] 
**sslStatus** | **String** | Signifies whether SSL needs to be enabled or not. | 
**userName** | **String** | Username for the storage account. | [optional] 



## Enum: AccountTypeEnum


* `GeneralPurposeStorage` (value: `"GeneralPurposeStorage"`)

* `BlobStorage` (value: `"BlobStorage"`)





## Enum: SslStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




