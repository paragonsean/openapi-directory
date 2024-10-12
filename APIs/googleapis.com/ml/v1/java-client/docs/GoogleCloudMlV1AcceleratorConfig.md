

# GoogleCloudMlV1AcceleratorConfig

Represents a hardware accelerator request config. Note that the AcceleratorConfig can be used in both Jobs and Versions. Learn more about [accelerators for training](/ml-engine/docs/using-gpus) and [accelerators for online prediction](/ml-engine/docs/machine-types-online-prediction#gpus).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **String** | The number of accelerators to attach to each machine running the job. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of accelerator to use. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCELERATOR_TYPE_UNSPECIFIED | &quot;ACCELERATOR_TYPE_UNSPECIFIED&quot; |
| NVIDIA_TESLA_K80 | &quot;NVIDIA_TESLA_K80&quot; |
| NVIDIA_TESLA_P100 | &quot;NVIDIA_TESLA_P100&quot; |
| NVIDIA_TESLA_V100 | &quot;NVIDIA_TESLA_V100&quot; |
| NVIDIA_TESLA_P4 | &quot;NVIDIA_TESLA_P4&quot; |
| NVIDIA_TESLA_T4 | &quot;NVIDIA_TESLA_T4&quot; |
| NVIDIA_TESLA_A100 | &quot;NVIDIA_TESLA_A100&quot; |
| TPU_V2 | &quot;TPU_V2&quot; |
| TPU_V3 | &quot;TPU_V3&quot; |
| TPU_V2_POD | &quot;TPU_V2_POD&quot; |
| TPU_V3_POD | &quot;TPU_V3_POD&quot; |
| TPU_V4_POD | &quot;TPU_V4_POD&quot; |



