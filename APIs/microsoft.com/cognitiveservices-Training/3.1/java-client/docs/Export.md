

# Export


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downloadUri** | **String** | URI used to download the model. |  [optional] [readonly] |
|**flavor** | [**FlavorEnum**](#FlavorEnum) | Flavor of the export. |  [optional] [readonly] |
|**newerVersionAvailable** | **Boolean** | Indicates an updated version of the export package is available and should be re-exported for the latest changes. |  [optional] [readonly] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform of the export. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the export. |  [optional] [readonly] |



## Enum: FlavorEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;Linux&quot; |
| WINDOWS | &quot;Windows&quot; |
| ONNX10 | &quot;ONNX10&quot; |
| ONNX12 | &quot;ONNX12&quot; |
| ARM | &quot;ARM&quot; |
| TENSOR_FLOW_NORMAL | &quot;TensorFlowNormal&quot; |
| TENSOR_FLOW_LITE | &quot;TensorFlowLite&quot; |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| CORE_ML | &quot;CoreML&quot; |
| TENSOR_FLOW | &quot;TensorFlow&quot; |
| DOCKER_FILE | &quot;DockerFile&quot; |
| ONNX | &quot;ONNX&quot; |
| VAIDK | &quot;VAIDK&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| EXPORTING | &quot;Exporting&quot; |
| FAILED | &quot;Failed&quot; |
| DONE | &quot;Done&quot; |



