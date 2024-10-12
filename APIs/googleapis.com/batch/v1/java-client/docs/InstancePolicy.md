

# InstancePolicy

InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accelerators** | [**List&lt;Accelerator&gt;**](Accelerator.md) | The accelerators attached to each VM instance. |  [optional] |
|**bootDisk** | [**Disk**](Disk.md) |  |  [optional] |
|**disks** | [**List&lt;AttachedDisk&gt;**](AttachedDisk.md) | Non-boot disks to be attached for each VM created by this InstancePolicy. New disks will be deleted when the VM is deleted. A non-boot disk is a disk that can be of a device with a file system or a raw storage drive that is not ready for data storage and accessing. |  [optional] |
|**machineType** | **String** | The Compute Engine machine type. |  [optional] |
|**minCpuPlatform** | **String** | The minimum CPU platform. See https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform. |  [optional] |
|**provisioningModel** | [**ProvisioningModelEnum**](#ProvisioningModelEnum) | The provisioning model. |  [optional] |
|**reservation** | **String** | Optional. If specified, VMs will consume only the specified reservation. If not specified (default), VMs will consume any applicable reservation. |  [optional] |



## Enum: ProvisioningModelEnum

| Name | Value |
|---- | -----|
| PROVISIONING_MODEL_UNSPECIFIED | &quot;PROVISIONING_MODEL_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| SPOT | &quot;SPOT&quot; |
| PREEMPTIBLE | &quot;PREEMPTIBLE&quot; |



