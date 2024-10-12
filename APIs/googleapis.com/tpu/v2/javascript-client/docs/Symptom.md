# CloudTpuApi.Symptom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Timestamp when the Symptom is created. | [optional] 
**details** | **String** | Detailed information of the current Symptom. | [optional] 
**symptomType** | **String** | Type of the Symptom. | [optional] 
**workerId** | **String** | A string used to uniquely distinguish a worker within a TPU node. | [optional] 



## Enum: SymptomTypeEnum


* `SYMPTOM_TYPE_UNSPECIFIED` (value: `"SYMPTOM_TYPE_UNSPECIFIED"`)

* `LOW_MEMORY` (value: `"LOW_MEMORY"`)

* `OUT_OF_MEMORY` (value: `"OUT_OF_MEMORY"`)

* `EXECUTE_TIMED_OUT` (value: `"EXECUTE_TIMED_OUT"`)

* `MESH_BUILD_FAIL` (value: `"MESH_BUILD_FAIL"`)

* `HBM_OUT_OF_MEMORY` (value: `"HBM_OUT_OF_MEMORY"`)

* `PROJECT_ABUSE` (value: `"PROJECT_ABUSE"`)




