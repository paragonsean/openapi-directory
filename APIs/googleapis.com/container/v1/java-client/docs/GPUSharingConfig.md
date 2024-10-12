

# GPUSharingConfig

GPUSharingConfig represents the GPU sharing configuration for Hardware Accelerators.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gpuSharingStrategy** | [**GpuSharingStrategyEnum**](#GpuSharingStrategyEnum) | The type of GPU sharing strategy to enable on the GPU node. |  [optional] |
|**maxSharedClientsPerGpu** | **String** | The max number of containers that can share a physical GPU. |  [optional] |



## Enum: GpuSharingStrategyEnum

| Name | Value |
|---- | -----|
| GPU_SHARING_STRATEGY_UNSPECIFIED | &quot;GPU_SHARING_STRATEGY_UNSPECIFIED&quot; |
| TIME_SHARING | &quot;TIME_SHARING&quot; |



