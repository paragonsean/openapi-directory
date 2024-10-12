# DevTestLabsClient.LabPropertiesFragment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labStorageType** | **String** | Type of storage used by the lab. It can be either Premium or Standard. Default is Premium. | [optional] 
**premiumDataDisks** | **String** | The setting to enable usage of premium data disks.  When its value is &#39;Enabled&#39;, creation of standard or premium data disks is allowed.  When its value is &#39;Disabled&#39;, only creation of standard data disks is allowed. | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] 



## Enum: LabStorageTypeEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)





## Enum: PremiumDataDisksEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




