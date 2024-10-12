# AzureMachineLearningModelManagementService.TargetRuntime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**osType** | **String** | The target operating system. | [optional] 
**properties** | **{String: String}** | The properties dictionary. | [optional] [readonly] 
**runtimeType** | **String** | The target runtime type. | [optional] 
**targetArchitecture** | **String** | The target architecture. | [optional] 



## Enum: OsTypeEnum


* `Linux` (value: `"Linux"`)

* `Windows` (value: `"Windows"`)





## Enum: RuntimeTypeEnum


* `SparkPython` (value: `"SparkPython"`)

* `Tlc37` (value: `"Tlc37"`)

* `Tlc38` (value: `"Tlc38"`)

* `Tlc310` (value: `"Tlc310"`)

* `Python` (value: `"Python"`)

* `PythonSlim` (value: `"PythonSlim"`)

* `PythonCustom` (value: `"PythonCustom"`)





## Enum: TargetArchitectureEnum


* `Amd64` (value: `"Amd64"`)

* `Arm32v7` (value: `"Arm32v7"`)




