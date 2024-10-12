# MigrationCenterApi.DiskEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacityBytes** | **String** | Disk capacity. | [optional] 
**diskLabel** | **String** | Disk label. | [optional] 
**diskLabelType** | **String** | Disk label type (e.g. BIOS/GPT) | [optional] 
**freeBytes** | **String** | Disk free space. | [optional] 
**hwAddress** | **String** | Disk hardware address (e.g. 0:1 for SCSI). | [optional] 
**interfaceType** | **String** | Disks interface type. | [optional] 
**partitions** | [**DiskPartitionList**](DiskPartitionList.md) |  | [optional] 
**vmware** | [**VmwareDiskConfig**](VmwareDiskConfig.md) |  | [optional] 



## Enum: InterfaceTypeEnum


* `INTERFACE_TYPE_UNSPECIFIED` (value: `"INTERFACE_TYPE_UNSPECIFIED"`)

* `IDE` (value: `"IDE"`)

* `SATA` (value: `"SATA"`)

* `SAS` (value: `"SAS"`)

* `SCSI` (value: `"SCSI"`)

* `NVME` (value: `"NVME"`)

* `FC` (value: `"FC"`)

* `ISCSI` (value: `"ISCSI"`)




