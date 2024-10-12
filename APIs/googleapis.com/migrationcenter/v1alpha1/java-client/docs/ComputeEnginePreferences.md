

# ComputeEnginePreferences

The user preferences relating to Compute Engine target platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | License type to consider when calculating costs for virtual machine insights and recommendations. If unspecified, costs are calculated based on the default licensing plan. |  [optional] |
|**machinePreferences** | [**MachinePreferences**](MachinePreferences.md) |  |  [optional] |
|**persistentDiskType** | [**PersistentDiskTypeEnum**](#PersistentDiskTypeEnum) | Persistent disk type to use. If unspecified (default), all types are considered, based on available usage data. |  [optional] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LICENSE_TYPE_UNSPECIFIED&quot; |
| DEFAULT | &quot;LICENSE_TYPE_DEFAULT&quot; |
| BRING_YOUR_OWN_LICENSE | &quot;LICENSE_TYPE_BRING_YOUR_OWN_LICENSE&quot; |



## Enum: PersistentDiskTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PERSISTENT_DISK_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;PERSISTENT_DISK_TYPE_STANDARD&quot; |
| BALANCED | &quot;PERSISTENT_DISK_TYPE_BALANCED&quot; |
| SSD | &quot;PERSISTENT_DISK_TYPE_SSD&quot; |



