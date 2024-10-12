# MigrationCenterApi.ComputeEnginePreferences

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licenseType** | **String** | License type to consider when calculating costs for virtual machine insights and recommendations. If unspecified, costs are calculated based on the default licensing plan. | [optional] 
**machinePreferences** | [**MachinePreferences**](MachinePreferences.md) |  | [optional] 
**persistentDiskType** | **String** | Persistent disk type to use. If unspecified (default), all types are considered, based on available usage data. | [optional] 



## Enum: LicenseTypeEnum


* `UNSPECIFIED` (value: `"LICENSE_TYPE_UNSPECIFIED"`)

* `DEFAULT` (value: `"LICENSE_TYPE_DEFAULT"`)

* `BRING_YOUR_OWN_LICENSE` (value: `"LICENSE_TYPE_BRING_YOUR_OWN_LICENSE"`)





## Enum: PersistentDiskTypeEnum


* `UNSPECIFIED` (value: `"PERSISTENT_DISK_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"PERSISTENT_DISK_TYPE_STANDARD"`)

* `BALANCED` (value: `"PERSISTENT_DISK_TYPE_BALANCED"`)

* `SSD` (value: `"PERSISTENT_DISK_TYPE_SSD"`)




