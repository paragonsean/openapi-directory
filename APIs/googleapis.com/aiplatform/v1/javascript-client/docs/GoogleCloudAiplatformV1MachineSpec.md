# VertexAiApi.GoogleCloudAiplatformV1MachineSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceleratorCount** | **Number** | The number of accelerators to attach to the machine. | [optional] 
**acceleratorType** | **String** | Immutable. The type of accelerator(s) that may be attached to the machine as per accelerator_count. | [optional] 
**machineType** | **String** | Immutable. The type of the machine. See the [list of machine types supported for prediction](https://cloud.google.com/vertex-ai/docs/predictions/configure-compute#machine-types) See the [list of machine types supported for custom training](https://cloud.google.com/vertex-ai/docs/training/configure-compute#machine-types). For DeployedModel this field is optional, and the default value is &#x60;n1-standard-2&#x60;. For BatchPredictionJob or as part of WorkerPoolSpec this field is required. | [optional] 
**tpuTopology** | **String** | Immutable. The topology of the TPUs. Corresponds to the TPU topologies available from GKE. (Example: tpu_topology: \&quot;2x2x1\&quot;). | [optional] 



## Enum: AcceleratorTypeEnum


* `ACCELERATOR_TYPE_UNSPECIFIED` (value: `"ACCELERATOR_TYPE_UNSPECIFIED"`)

* `NVIDIA_TESLA_K80` (value: `"NVIDIA_TESLA_K80"`)

* `NVIDIA_TESLA_P100` (value: `"NVIDIA_TESLA_P100"`)

* `NVIDIA_TESLA_V100` (value: `"NVIDIA_TESLA_V100"`)

* `NVIDIA_TESLA_P4` (value: `"NVIDIA_TESLA_P4"`)

* `NVIDIA_TESLA_T4` (value: `"NVIDIA_TESLA_T4"`)

* `NVIDIA_TESLA_A100` (value: `"NVIDIA_TESLA_A100"`)

* `NVIDIA_A100_80GB` (value: `"NVIDIA_A100_80GB"`)

* `NVIDIA_L4` (value: `"NVIDIA_L4"`)

* `NVIDIA_H100_80GB` (value: `"NVIDIA_H100_80GB"`)

* `TPU_V2` (value: `"TPU_V2"`)

* `TPU_V3` (value: `"TPU_V3"`)

* `TPU_V4_POD` (value: `"TPU_V4_POD"`)




