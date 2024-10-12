

# CustomImagePropertiesFragment

Properties of a custom image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | **String** | The author of the custom image. |  [optional] |
|**customImagePlan** | [**CustomImagePropertiesFromPlanFragment**](CustomImagePropertiesFromPlanFragment.md) |  |  [optional] |
|**dataDiskStorageInfo** | [**List&lt;DataDiskStorageTypeInfoFragment&gt;**](DataDiskStorageTypeInfoFragment.md) | Storage information about the data disks present in the custom image |  [optional] |
|**description** | **String** | The description of the custom image. |  [optional] |
|**isPlanAuthorized** | **Boolean** | Whether or not the custom images underlying offer/plan has been enabled for programmatic deployment |  [optional] |
|**managedImageId** | **String** | The Managed Image Id backing the custom image. |  [optional] |
|**managedSnapshotId** | **String** | The Managed Snapshot Id backing the custom image. |  [optional] |
|**vhd** | [**CustomImagePropertiesCustomFragment**](CustomImagePropertiesCustomFragment.md) |  |  [optional] |
|**vm** | [**CustomImagePropertiesFromVmFragment**](CustomImagePropertiesFromVmFragment.md) |  |  [optional] |



