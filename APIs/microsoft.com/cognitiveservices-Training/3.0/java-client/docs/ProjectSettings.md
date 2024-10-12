

# ProjectSettings

Represents settings associated with a project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classificationType** | [**ClassificationTypeEnum**](#ClassificationTypeEnum) | Gets or sets the classification type of the project. |  [optional] |
|**domainId** | **UUID** | Gets or sets the id of the Domain to use with this project. |  [optional] |
|**targetExportPlatforms** | [**List&lt;TargetExportPlatformsEnum&gt;**](#List&lt;TargetExportPlatformsEnum&gt;) | A list of ExportPlatform that the trained model should be able to support. |  [optional] |



## Enum: ClassificationTypeEnum

| Name | Value |
|---- | -----|
| MULTICLASS | &quot;Multiclass&quot; |
| MULTILABEL | &quot;Multilabel&quot; |



## Enum: List&lt;TargetExportPlatformsEnum&gt;

| Name | Value |
|---- | -----|
| CORE_ML | &quot;CoreML&quot; |
| TENSOR_FLOW | &quot;TensorFlow&quot; |
| DOCKER_FILE | &quot;DockerFile&quot; |
| ONNX | &quot;ONNX&quot; |
| VAIDK | &quot;VAIDK&quot; |



