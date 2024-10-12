

# ComputeVmWorkload

Specificies usage of a set of identical compute VM instances.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableConfidentialCompute** | **Boolean** | Defines whether each instance has confidential compute enabled. |  [optional] |
|**guestAccelerator** | [**GuestAccelerator**](GuestAccelerator.md) |  |  [optional] |
|**instancesRunning** | [**Usage**](Usage.md) |  |  [optional] |
|**licenses** | **List&lt;String&gt;** | Premium image licenses used by each instance. |  [optional] |
|**machineType** | [**MachineType**](MachineType.md) |  |  [optional] |
|**persistentDisks** | [**List&lt;PersistentDisk&gt;**](PersistentDisk.md) | Persistent disks attached to each instance. Must include a boot disk. |  [optional] |
|**preemptible** | **Boolean** | Defines whether each instance is preemptible. |  [optional] |
|**region** | **String** | The [region](https://cloud.google.com/compute/docs/regions-zones) where the VMs run. For example: \&quot;us-central1\&quot;. |  [optional] |



