

# GoogleCloudMlV1Capability


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableAccelerators** | [**List&lt;AvailableAcceleratorsEnum&gt;**](#List&lt;AvailableAcceleratorsEnum&gt;) | Available accelerators for the capability. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: List&lt;AvailableAcceleratorsEnum&gt;

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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| TRAINING | &quot;TRAINING&quot; |
| BATCH_PREDICTION | &quot;BATCH_PREDICTION&quot; |
| ONLINE_PREDICTION | &quot;ONLINE_PREDICTION&quot; |



