# StorSimple8000SeriesManagementClient.VolumeContainerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandWidthRateInMbps** | **Number** | The bandwidth-rate set on the volume container. | [optional] 
**bandwidthSettingId** | **String** | The ID of the bandwidth setting associated with the volume container. | [optional] 
**encryptionKey** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  | [optional] 
**encryptionStatus** | **String** | The flag to denote whether encryption is enabled or not. | [optional] [readonly] 
**ownerShipStatus** | **String** | The owner ship status of the volume container. Only when the status is \&quot;NotOwned\&quot;, the delete operation on the volume container is permitted. | [optional] [readonly] 
**storageAccountCredentialId** | **String** | The path ID of storage account associated with the volume container. | 
**totalCloudStorageUsageInBytes** | **Number** | The total cloud storage for the volume container. | [optional] [readonly] 
**volumeCount** | **Number** | The number of volumes in the volume Container. | [optional] [readonly] 



## Enum: EncryptionStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: OwnerShipStatusEnum


* `Owned` (value: `"Owned"`)

* `NotOwned` (value: `"NotOwned"`)




