

# VolumeContainerProperties

The properties of volume container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandWidthRateInMbps** | **Integer** | The bandwidth-rate set on the volume container. |  [optional] |
|**bandwidthSettingId** | **String** | The ID of the bandwidth setting associated with the volume container. |  [optional] |
|**encryptionKey** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  |  [optional] |
|**encryptionStatus** | [**EncryptionStatusEnum**](#EncryptionStatusEnum) | The flag to denote whether encryption is enabled or not. |  [optional] [readonly] |
|**ownerShipStatus** | [**OwnerShipStatusEnum**](#OwnerShipStatusEnum) | The owner ship status of the volume container. Only when the status is \&quot;NotOwned\&quot;, the delete operation on the volume container is permitted. |  [optional] [readonly] |
|**storageAccountCredentialId** | **String** | The path ID of storage account associated with the volume container. |  |
|**totalCloudStorageUsageInBytes** | **Long** | The total cloud storage for the volume container. |  [optional] [readonly] |
|**volumeCount** | **Integer** | The number of volumes in the volume Container. |  [optional] [readonly] |



## Enum: EncryptionStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: OwnerShipStatusEnum

| Name | Value |
|---- | -----|
| OWNED | &quot;Owned&quot; |
| NOT_OWNED | &quot;NotOwned&quot; |



