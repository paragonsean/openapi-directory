

# GoogleCloudAiplatformV1MachineSpec

Specification of a single machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceleratorCount** | **Integer** | The number of accelerators to attach to the machine. |  [optional] |
|**acceleratorType** | [**AcceleratorTypeEnum**](#AcceleratorTypeEnum) | Immutable. The type of accelerator(s) that may be attached to the machine as per accelerator_count. |  [optional] |
|**machineType** | **String** | Immutable. The type of the machine. See the [list of machine types supported for prediction](https://cloud.google.com/vertex-ai/docs/predictions/configure-compute#machine-types) See the [list of machine types supported for custom training](https://cloud.google.com/vertex-ai/docs/training/configure-compute#machine-types). For DeployedModel this field is optional, and the default value is &#x60;n1-standard-2&#x60;. For BatchPredictionJob or as part of WorkerPoolSpec this field is required. |  [optional] |
|**tpuTopology** | **String** | Immutable. The topology of the TPUs. Corresponds to the TPU topologies available from GKE. (Example: tpu_topology: \&quot;2x2x1\&quot;). |  [optional] |



## Enum: AcceleratorTypeEnum

| Name | Value |
|---- | -----|
| ACCELERATOR_TYPE_UNSPECIFIED | &quot;ACCELERATOR_TYPE_UNSPECIFIED&quot; |
| NVIDIA_TESLA_K80 | &quot;NVIDIA_TESLA_K80&quot; |
| NVIDIA_TESLA_P100 | &quot;NVIDIA_TESLA_P100&quot; |
| NVIDIA_TESLA_V100 | &quot;NVIDIA_TESLA_V100&quot; |
| NVIDIA_TESLA_P4 | &quot;NVIDIA_TESLA_P4&quot; |
| NVIDIA_TESLA_T4 | &quot;NVIDIA_TESLA_T4&quot; |
| NVIDIA_TESLA_A100 | &quot;NVIDIA_TESLA_A100&quot; |
| NVIDIA_A100_80_GB | &quot;NVIDIA_A100_80GB&quot; |
| NVIDIA_L4 | &quot;NVIDIA_L4&quot; |
| NVIDIA_H100_80_GB | &quot;NVIDIA_H100_80GB&quot; |
| TPU_V2 | &quot;TPU_V2&quot; |
| TPU_V3 | &quot;TPU_V3&quot; |
| TPU_V4_POD | &quot;TPU_V4_POD&quot; |



