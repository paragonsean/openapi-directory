# StorSimpleManagementClient.StorageAccountCredentialProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessKey** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  | [optional] 
**cloudType** | **String** | The cloud service provider | 
**enableSSL** | **String** | SSL needs to be enabled or not | 
**endPoint** | **String** | The storage endpoint | 
**location** | **String** | The storage account&#39;s geo location | [optional] 
**login** | **String** | The storage account login | 



## Enum: CloudTypeEnum


* `Azure` (value: `"Azure"`)

* `S3` (value: `"S3"`)

* `S3_RRS` (value: `"S3_RRS"`)

* `OpenStack` (value: `"OpenStack"`)

* `HP` (value: `"HP"`)





## Enum: EnableSSLEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




