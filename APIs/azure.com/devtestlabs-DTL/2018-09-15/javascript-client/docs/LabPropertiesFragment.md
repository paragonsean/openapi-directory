# DevTestLabsClient.LabPropertiesFragment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | [**LabAnnouncementPropertiesFragment**](LabAnnouncementPropertiesFragment.md) |  | [optional] 
**environmentPermission** | **String** | The access rights to be granted to the user when provisioning an environment | [optional] 
**extendedProperties** | **{String: String}** | Extended properties of the lab used for experimental features | [optional] 
**labStorageType** | **String** | Type of storage used by the lab. It can be either Premium or Standard. Default is Premium. | [optional] 
**mandatoryArtifactsResourceIdsLinux** | **[String]** | The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user. | [optional] 
**mandatoryArtifactsResourceIdsWindows** | **[String]** | The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user. | [optional] 
**premiumDataDisks** | **String** | The setting to enable usage of premium data disks.  When its value is &#39;Enabled&#39;, creation of standard or premium data disks is allowed.  When its value is &#39;Disabled&#39;, only creation of standard data disks is allowed. | [optional] 
**support** | [**LabSupportPropertiesFragment**](LabSupportPropertiesFragment.md) |  | [optional] 



## Enum: EnvironmentPermissionEnum


* `Reader` (value: `"Reader"`)

* `Contributor` (value: `"Contributor"`)





## Enum: LabStorageTypeEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `StandardSSD` (value: `"StandardSSD"`)





## Enum: PremiumDataDisksEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




