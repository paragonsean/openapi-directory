# SharedImageGalleryServiceClient.GalleryDataDiskImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun** | **Number** | This property specifies the logical unit number of the data disk. This value is used to identify data disks within the Virtual Machine and therefore must be unique for each data disk attached to the Virtual Machine. | 
**hostCaching** | **String** | The host caching of the disk. Valid values are &#39;None&#39;, &#39;ReadOnly&#39;, and &#39;ReadWrite&#39; | [optional] 
**sizeInGB** | **Number** | This property indicates the size of the VHD to be created. | [optional] [readonly] 
**source** | [**GalleryArtifactVersionSource**](GalleryArtifactVersionSource.md) |  | [optional] 



## Enum: HostCachingEnum


* `None` (value: `"None"`)

* `ReadOnly` (value: `"ReadOnly"`)

* `ReadWrite` (value: `"ReadWrite"`)




