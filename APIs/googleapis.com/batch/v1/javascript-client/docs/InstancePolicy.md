# BatchApi.InstancePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerators** | [**[Accelerator]**](Accelerator.md) | The accelerators attached to each VM instance. | [optional] 
**bootDisk** | [**Disk**](Disk.md) |  | [optional] 
**disks** | [**[AttachedDisk]**](AttachedDisk.md) | Non-boot disks to be attached for each VM created by this InstancePolicy. New disks will be deleted when the VM is deleted. A non-boot disk is a disk that can be of a device with a file system or a raw storage drive that is not ready for data storage and accessing. | [optional] 
**machineType** | **String** | The Compute Engine machine type. | [optional] 
**minCpuPlatform** | **String** | The minimum CPU platform. See https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform. | [optional] 
**provisioningModel** | **String** | The provisioning model. | [optional] 
**reservation** | **String** | Optional. If specified, VMs will consume only the specified reservation. If not specified (default), VMs will consume any applicable reservation. | [optional] 



## Enum: ProvisioningModelEnum


* `PROVISIONING_MODEL_UNSPECIFIED` (value: `"PROVISIONING_MODEL_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `SPOT` (value: `"SPOT"`)

* `PREEMPTIBLE` (value: `"PREEMPTIBLE"`)




