# CustomVisionTrainingClient.ProjectSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classificationType** | **String** | Gets or sets the classification type of the project. | [optional] 
**domainId** | **String** | Gets or sets the id of the Domain to use with this project. | [optional] 
**targetExportPlatforms** | **[String]** | A list of ExportPlatform that the trained model should be able to support. | [optional] 



## Enum: ClassificationTypeEnum


* `Multiclass` (value: `"Multiclass"`)

* `Multilabel` (value: `"Multilabel"`)





## Enum: [TargetExportPlatformsEnum]


* `CoreML` (value: `"CoreML"`)

* `TensorFlow` (value: `"TensorFlow"`)

* `DockerFile` (value: `"DockerFile"`)

* `ONNX` (value: `"ONNX"`)

* `VAIDK` (value: `"VAIDK"`)




