

# DiskEntry

Single disk entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacityBytes** | **String** | Disk capacity. |  [optional] |
|**diskLabel** | **String** | Disk label. |  [optional] |
|**diskLabelType** | **String** | Disk label type (e.g. BIOS/GPT) |  [optional] |
|**freeBytes** | **String** | Disk free space. |  [optional] |
|**hwAddress** | **String** | Disk hardware address (e.g. 0:1 for SCSI). |  [optional] |
|**interfaceType** | [**InterfaceTypeEnum**](#InterfaceTypeEnum) | Disks interface type. |  [optional] |
|**partitions** | [**DiskPartitionList**](DiskPartitionList.md) |  |  [optional] |
|**vmware** | [**VmwareDiskConfig**](VmwareDiskConfig.md) |  |  [optional] |



## Enum: InterfaceTypeEnum

| Name | Value |
|---- | -----|
| INTERFACE_TYPE_UNSPECIFIED | &quot;INTERFACE_TYPE_UNSPECIFIED&quot; |
| IDE | &quot;IDE&quot; |
| SATA | &quot;SATA&quot; |
| SAS | &quot;SAS&quot; |
| SCSI | &quot;SCSI&quot; |
| NVME | &quot;NVME&quot; |
| FC | &quot;FC&quot; |
| ISCSI | &quot;ISCSI&quot; |



