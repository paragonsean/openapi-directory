

# Symptom

A Symptom instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Timestamp when the Symptom is created. |  [optional] |
|**details** | **String** | Detailed information of the current Symptom. |  [optional] |
|**symptomType** | [**SymptomTypeEnum**](#SymptomTypeEnum) | Type of the Symptom. |  [optional] |
|**workerId** | **String** | A string used to uniquely distinguish a worker within a TPU node. |  [optional] |



## Enum: SymptomTypeEnum

| Name | Value |
|---- | -----|
| SYMPTOM_TYPE_UNSPECIFIED | &quot;SYMPTOM_TYPE_UNSPECIFIED&quot; |
| LOW_MEMORY | &quot;LOW_MEMORY&quot; |
| OUT_OF_MEMORY | &quot;OUT_OF_MEMORY&quot; |
| EXECUTE_TIMED_OUT | &quot;EXECUTE_TIMED_OUT&quot; |
| MESH_BUILD_FAIL | &quot;MESH_BUILD_FAIL&quot; |
| HBM_OUT_OF_MEMORY | &quot;HBM_OUT_OF_MEMORY&quot; |
| PROJECT_ABUSE | &quot;PROJECT_ABUSE&quot; |



