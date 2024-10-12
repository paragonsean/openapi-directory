# DevTestLabsClient.LabProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactsStorageAccount** | **String** | The lab&#39;s artifact storage account. | [optional] [readonly] 
**createdDate** | **Date** | The creation date of the lab. | [optional] [readonly] 
**defaultPremiumStorageAccount** | **String** | The lab&#39;s default premium storage account. | [optional] [readonly] 
**defaultStorageAccount** | **String** | The lab&#39;s default storage account. | [optional] [readonly] 
**labStorageType** | **String** | Type of storage used by the lab. It can be either Premium or Standard. Default is Premium. | [optional] 
**premiumDataDiskStorageAccount** | **String** | The lab&#39;s premium data disk storage account. | [optional] [readonly] 
**premiumDataDisks** | **String** | The setting to enable usage of premium data disks.  When its value is &#39;Enabled&#39;, creation of standard or premium data disks is allowed.  When its value is &#39;Disabled&#39;, only creation of standard data disks is allowed. | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] 
**vaultName** | **String** | The lab&#39;s Key vault. | [optional] [readonly] 



## Enum: LabStorageTypeEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)





## Enum: PremiumDataDisksEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




