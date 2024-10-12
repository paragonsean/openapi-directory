# MigrationCenterApi.DiskEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskLabel** | **String** | Disk label. | [optional] 
**diskLabelType** | **String** | Disk label type (e.g. BIOS/GPT) | [optional] 
**hwAddress** | **String** | Disk hardware address (e.g. 0:1 for SCSI). | [optional] 
**interfaceType** | **String** | Disks interface type (e.g. SATA/SCSI) | [optional] 
**partitions** | [**DiskPartitionList**](DiskPartitionList.md) |  | [optional] 
**status** | **String** | Disk status (e.g. online). | [optional] 
**totalCapacityBytes** | **String** | Disk capacity. | [optional] 
**totalFreeBytes** | **String** | Disk free space. | [optional] 
**vmwareConfig** | [**VmwareDiskConfig**](VmwareDiskConfig.md) |  | [optional] 


