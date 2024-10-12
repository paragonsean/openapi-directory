# CustomVisionTrainingClient.Iteration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classificationType** | **String** | Gets the classification type of the project. | [optional] [readonly] 
**created** | **Date** | Gets the time this iteration was completed. | [optional] [readonly] 
**domainId** | **String** | Get or sets a guid of the domain the iteration has been trained on. | [optional] [readonly] 
**exportable** | **Boolean** | Whether the iteration can be exported to another format for download. | [optional] [readonly] 
**exportableTo** | **[String]** | A set of platforms this iteration can export to. | [optional] [readonly] 
**id** | **String** | Gets the id of the iteration. | [optional] [readonly] 
**lastModified** | **Date** | Gets the time this iteration was last modified. | [optional] [readonly] 
**name** | **String** | Gets or sets the name of the iteration. | 
**originalPublishResourceId** | **String** | Resource Provider Id this iteration was originally published to. | [optional] [readonly] 
**projectId** | **String** | Gets the project id of the iteration. | [optional] [readonly] 
**publishName** | **String** | Name of the published model. | [optional] [readonly] 
**reservedBudgetInHours** | **Number** | Gets the reserved advanced training budget for the iteration. | [optional] [readonly] 
**status** | **String** | Gets the current iteration status. | [optional] [readonly] 
**trainedAt** | **Date** | Gets the time this iteration was last modified. | [optional] [readonly] 
**trainingTimeInMinutes** | **Number** | Gets the training time for the iteration. | [optional] [readonly] 
**trainingType** | **String** | Gets the training type of the iteration. | [optional] [readonly] 



## Enum: ClassificationTypeEnum


* `Multiclass` (value: `"Multiclass"`)

* `Multilabel` (value: `"Multilabel"`)





## Enum: [ExportableToEnum]


* `CoreML` (value: `"CoreML"`)

* `TensorFlow` (value: `"TensorFlow"`)

* `DockerFile` (value: `"DockerFile"`)

* `ONNX` (value: `"ONNX"`)

* `VAIDK` (value: `"VAIDK"`)





## Enum: TrainingTypeEnum


* `Regular` (value: `"Regular"`)

* `Advanced` (value: `"Advanced"`)




