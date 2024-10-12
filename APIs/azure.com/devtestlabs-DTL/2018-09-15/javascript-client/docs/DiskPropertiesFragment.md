# DevTestLabsClient.DiskPropertiesFragment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskBlobName** | **String** | When backed by a blob, the name of the VHD blob without extension. | [optional] 
**diskSizeGiB** | **Number** | The size of the disk in GibiBytes. | [optional] 
**diskType** | **String** | The storage type for the disk (i.e. Standard, Premium). | [optional] 
**diskUri** | **String** | When backed by a blob, the URI of underlying blob. | [optional] 
**hostCaching** | **String** | The host caching policy of the disk (i.e. None, ReadOnly, ReadWrite). | [optional] 
**leasedByLabVmId** | **String** | The resource ID of the VM to which this disk is leased. | [optional] 
**managedDiskId** | **String** | When backed by managed disk, this is the ID of the compute disk resource. | [optional] 



## Enum: DiskTypeEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `StandardSSD` (value: `"StandardSSD"`)




