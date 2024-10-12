

# CustomImageProperties

Properties of a custom image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | **String** | The author of the custom image. |  [optional] |
|**creationDate** | **OffsetDateTime** | The creation date of the custom image. |  [optional] [readonly] |
|**customImagePlan** | [**CustomImagePropertiesFromPlan**](CustomImagePropertiesFromPlan.md) |  |  [optional] |
|**dataDiskStorageInfo** | [**List&lt;DataDiskStorageTypeInfo&gt;**](DataDiskStorageTypeInfo.md) | Storage information about the data disks present in the custom image |  [optional] |
|**description** | **String** | The description of the custom image. |  [optional] |
|**isPlanAuthorized** | **Boolean** | Whether or not the custom images underlying offer/plan has been enabled for programmatic deployment |  [optional] |
|**managedImageId** | **String** | The Managed Image Id backing the custom image. |  [optional] |
|**managedSnapshotId** | **String** | The Managed Snapshot Id backing the custom image. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] [readonly] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] [readonly] |
|**vhd** | [**CustomImagePropertiesCustom**](CustomImagePropertiesCustom.md) |  |  [optional] |
|**vm** | [**CustomImagePropertiesFromVm**](CustomImagePropertiesFromVm.md) |  |  [optional] |



