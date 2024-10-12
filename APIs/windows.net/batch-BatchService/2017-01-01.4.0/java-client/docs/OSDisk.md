

# OSDisk


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caching** | [**CachingEnum**](#CachingEnum) | none - The caching mode for the disk is not enabled. readOnly - The caching mode for the disk is read only. readWrite - The caching mode for the disk is read and write. The default value for caching is none. For information about the caching options see: https://blogs.msdn.microsoft.com/windowsazurestorage/2012/06/27/exploring-windows-azure-drives-disks-and-images/. |  [optional] |
|**imageUris** | **List&lt;String&gt;** | All the VHDs must be identical and must reside in an Azure Storage account within the same subscription and same region as the Batch account. For best performance, it is recommended that each VHD resides in a separate Azure Storage account. Each VHD can serve up to 20 Windows compute nodes or 40 Linux compute nodes. You must supply enough VHD URIs to satisfy the &#39;targetDedicated&#39; property of the pool. If you do not supply enough VHD URIs, the pool will partially allocate compute nodes, and a resize error will occur. |  |



## Enum: CachingEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| READ_ONLY | &quot;readOnly&quot; |
| READ_WRITE | &quot;readWrite&quot; |



