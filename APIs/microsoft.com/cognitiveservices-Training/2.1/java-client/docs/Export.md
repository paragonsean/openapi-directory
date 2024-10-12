

# Export


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downloadUri** | **String** |  |  [optional] [readonly] |
|**flavor** | [**FlavorEnum**](#FlavorEnum) |  |  [optional] [readonly] |
|**newerVersionAvailable** | **Boolean** |  |  [optional] [readonly] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] [readonly] |



## Enum: FlavorEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;Linux&quot; |
| WINDOWS | &quot;Windows&quot; |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| CORE_ML | &quot;CoreML&quot; |
| TENSOR_FLOW | &quot;TensorFlow&quot; |
| DOCKER_FILE | &quot;DockerFile&quot; |
| ONNX | &quot;ONNX&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| EXPORTING | &quot;Exporting&quot; |
| FAILED | &quot;Failed&quot; |
| DONE | &quot;Done&quot; |



