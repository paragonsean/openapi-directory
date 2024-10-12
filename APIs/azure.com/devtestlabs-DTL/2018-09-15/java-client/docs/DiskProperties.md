

# DiskProperties

Properties of a disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDate** | **OffsetDateTime** | The creation date of the disk. |  [optional] [readonly] |
|**diskBlobName** | **String** | When backed by a blob, the name of the VHD blob without extension. |  [optional] |
|**diskSizeGiB** | **Integer** | The size of the disk in GibiBytes. |  [optional] |
|**diskType** | [**DiskTypeEnum**](#DiskTypeEnum) | The storage type for the disk (i.e. Standard, Premium). |  [optional] |
|**diskUri** | **String** | When backed by a blob, the URI of underlying blob. |  [optional] |
|**hostCaching** | **String** | The host caching policy of the disk (i.e. None, ReadOnly, ReadWrite). |  [optional] |
|**leasedByLabVmId** | **String** | The resource ID of the VM to which this disk is leased. |  [optional] |
|**managedDiskId** | **String** | When backed by managed disk, this is the ID of the compute disk resource. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] [readonly] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] [readonly] |



## Enum: DiskTypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| STANDARD_SSD | &quot;StandardSSD&quot; |



