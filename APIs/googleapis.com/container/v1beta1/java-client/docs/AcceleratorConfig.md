

# AcceleratorConfig

AcceleratorConfig represents a Hardware Accelerator request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceleratorCount** | **String** | The number of the accelerator cards exposed to an instance. |  [optional] |
|**acceleratorType** | **String** | The accelerator type resource name. List of supported accelerators [here](https://cloud.google.com/compute/docs/gpus) |  [optional] |
|**gpuDriverInstallationConfig** | [**GPUDriverInstallationConfig**](GPUDriverInstallationConfig.md) |  |  [optional] |
|**gpuPartitionSize** | **String** | Size of partitions to create on the GPU. Valid values are described in the NVIDIA [mig user guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#partitioning). |  [optional] |
|**gpuSharingConfig** | [**GPUSharingConfig**](GPUSharingConfig.md) |  |  [optional] |
|**maxTimeSharedClientsPerGpu** | **String** | The number of time-shared GPU resources to expose for each physical GPU. |  [optional] |



