# LinodeApi.Volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When this Volume was created. | [optional] [readonly] 
**filesystemPath** | **String** | The full filesystem path for the Volume based on the Volume&#39;s label. Path is /dev/disk/by-id/scsi-0Linode_Volume_ + Volume label.  | [optional] [readonly] 
**hardwareType** | **String** | The storage type of this Volume. | [optional] [readonly] 
**id** | **Number** | The unique ID of this Volume. | [optional] [readonly] 
**label** | **String** | The Volume&#39;s label is for display purposes only.  | [optional] 
**linodeId** | **Number** | If a Volume is attached to a specific Linode, the ID of that Linode will be displayed here.  | [optional] 
**linodeLabel** | **String** | If a Volume is attached to a specific Linode, the label of that Linode will be displayed here.  | [optional] [readonly] 
**region** | **String** | The unique ID of this Region. | [optional] [readonly] 
**size** | **Number** | The Volume&#39;s size, in GiB.  | [optional] 
**status** | **String** | The current status of the volume.  Can be one of:    * &#x60;creating&#x60; - the Volume is being created and is not yet available     for use.   * &#x60;active&#x60; - the Volume is online and available for use.   * &#x60;resizing&#x60; - the Volume is in the process of upgrading     its current capacity.  | [optional] [readonly] 
**tags** | **[String]** | An array of Tags applied to this object.  Tags are for organizational purposes only.  | [optional] 
**updated** | **Date** | When this Volume was last updated. | [optional] [readonly] 



## Enum: HardwareTypeEnum


* `hdd` (value: `"hdd"`)

* `nvme` (value: `"nvme"`)





## Enum: StatusEnum


* `creating` (value: `"creating"`)

* `active` (value: `"active"`)

* `resizing` (value: `"resizing"`)




