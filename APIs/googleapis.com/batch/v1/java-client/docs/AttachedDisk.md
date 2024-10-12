

# AttachedDisk

A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceName** | **String** | Device name that the guest operating system will see. It is used by Runnable.volumes field to mount disks. So please specify the device_name if you want Batch to help mount the disk, and it should match the device_name field in volumes. |  [optional] |
|**existingDisk** | **String** | Name of an existing PD. |  [optional] |
|**newDisk** | [**Disk**](Disk.md) |  |  [optional] |



