

# Iteration

Iteration model to be sent over JSON.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classificationType** | [**ClassificationTypeEnum**](#ClassificationTypeEnum) | Gets the classification type of the project. |  [optional] [readonly] |
|**created** | **OffsetDateTime** | Gets the time this iteration was completed. |  [optional] [readonly] |
|**domainId** | **UUID** | Get or sets a guid of the domain the iteration has been trained on. |  [optional] [readonly] |
|**exportable** | **Boolean** | Whether the iteration can be exported to another format for download. |  [optional] [readonly] |
|**exportableTo** | [**List&lt;ExportableToEnum&gt;**](#List&lt;ExportableToEnum&gt;) | A set of platforms this iteration can export to. |  [optional] [readonly] |
|**id** | **UUID** | Gets the id of the iteration. |  [optional] [readonly] |
|**lastModified** | **OffsetDateTime** | Gets the time this iteration was last modified. |  [optional] [readonly] |
|**name** | **String** | Gets or sets the name of the iteration. |  |
|**originalPublishResourceId** | **String** | Resource Provider Id this iteration was originally published to. |  [optional] [readonly] |
|**projectId** | **UUID** | Gets the project id of the iteration. |  [optional] [readonly] |
|**publishName** | **String** | Name of the published model. |  [optional] [readonly] |
|**reservedBudgetInHours** | **Integer** | Gets the reserved advanced training budget for the iteration. |  [optional] [readonly] |
|**status** | **String** | Gets the current iteration status. |  [optional] [readonly] |
|**trainedAt** | **OffsetDateTime** | Gets the time this iteration was last modified. |  [optional] [readonly] |
|**trainingType** | [**TrainingTypeEnum**](#TrainingTypeEnum) | Gets the training type of the iteration. |  [optional] [readonly] |



## Enum: ClassificationTypeEnum

| Name | Value |
|---- | -----|
| MULTICLASS | &quot;Multiclass&quot; |
| MULTILABEL | &quot;Multilabel&quot; |



## Enum: List&lt;ExportableToEnum&gt;

| Name | Value |
|---- | -----|
| CORE_ML | &quot;CoreML&quot; |
| TENSOR_FLOW | &quot;TensorFlow&quot; |
| DOCKER_FILE | &quot;DockerFile&quot; |
| ONNX | &quot;ONNX&quot; |
| VAIDK | &quot;VAIDK&quot; |



## Enum: TrainingTypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;Regular&quot; |
| ADVANCED | &quot;Advanced&quot; |



