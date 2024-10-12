# CustomVisionTrainingClient.Export

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downloadUri** | **String** | URI used to download the model. | [optional] [readonly] 
**flavor** | **String** | Flavor of the export. These are specializations of the export platform.  Docker platform has valid flavors: Linux, Windows, ARM.  Tensorflow platform has valid flavors: TensorFlowNormal, TensorFlowLite.  ONNX platform has valid flavors: ONNX10, ONNX12. | [optional] [readonly] 
**newerVersionAvailable** | **Boolean** | Indicates an updated version of the export package is available and should be re-exported for the latest changes. | [optional] [readonly] 
**platform** | **String** | Platform of the export. | [optional] [readonly] 
**status** | **String** | Status of the export. | [optional] [readonly] 



## Enum: FlavorEnum


* `Linux` (value: `"Linux"`)

* `Windows` (value: `"Windows"`)

* `ONNX10` (value: `"ONNX10"`)

* `ONNX12` (value: `"ONNX12"`)

* `ARM` (value: `"ARM"`)

* `TensorFlowNormal` (value: `"TensorFlowNormal"`)

* `TensorFlowLite` (value: `"TensorFlowLite"`)





## Enum: PlatformEnum


* `CoreML` (value: `"CoreML"`)

* `TensorFlow` (value: `"TensorFlow"`)

* `DockerFile` (value: `"DockerFile"`)

* `ONNX` (value: `"ONNX"`)

* `VAIDK` (value: `"VAIDK"`)





## Enum: StatusEnum


* `Exporting` (value: `"Exporting"`)

* `Failed` (value: `"Failed"`)

* `Done` (value: `"Done"`)




