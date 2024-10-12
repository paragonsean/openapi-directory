

# LabPropertiesFragment

Properties of a lab.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**announcement** | [**LabAnnouncementPropertiesFragment**](LabAnnouncementPropertiesFragment.md) |  |  [optional] |
|**environmentPermission** | [**EnvironmentPermissionEnum**](#EnvironmentPermissionEnum) | The access rights to be granted to the user when provisioning an environment |  [optional] |
|**extendedProperties** | **Map&lt;String, String&gt;** | Extended properties of the lab used for experimental features |  [optional] |
|**labStorageType** | [**LabStorageTypeEnum**](#LabStorageTypeEnum) | Type of storage used by the lab. It can be either Premium or Standard. Default is Premium. |  [optional] |
|**mandatoryArtifactsResourceIdsLinux** | **List&lt;String&gt;** | The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user. |  [optional] |
|**mandatoryArtifactsResourceIdsWindows** | **List&lt;String&gt;** | The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user. |  [optional] |
|**premiumDataDisks** | [**PremiumDataDisksEnum**](#PremiumDataDisksEnum) | The setting to enable usage of premium data disks.  When its value is &#39;Enabled&#39;, creation of standard or premium data disks is allowed.  When its value is &#39;Disabled&#39;, only creation of standard data disks is allowed. |  [optional] |
|**support** | [**LabSupportPropertiesFragment**](LabSupportPropertiesFragment.md) |  |  [optional] |



## Enum: EnvironmentPermissionEnum

| Name | Value |
|---- | -----|
| READER | &quot;Reader&quot; |
| CONTRIBUTOR | &quot;Contributor&quot; |



## Enum: LabStorageTypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| STANDARD_SSD | &quot;StandardSSD&quot; |



## Enum: PremiumDataDisksEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



