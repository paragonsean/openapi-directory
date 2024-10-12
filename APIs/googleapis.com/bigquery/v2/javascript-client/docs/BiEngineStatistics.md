# BigQueryApi.BiEngineStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerationMode** | **String** | Output only. Specifies which mode of BI Engine acceleration was performed (if any). | [optional] [readonly] 
**biEngineMode** | **String** | Output only. Specifies which mode of BI Engine acceleration was performed (if any). | [optional] [readonly] 
**biEngineReasons** | [**[BiEngineReason]**](BiEngineReason.md) | In case of DISABLED or PARTIAL bi_engine_mode, these contain the explanatory reasons as to why BI Engine could not accelerate. In case the full query was accelerated, this field is not populated. | [optional] 



## Enum: AccelerationModeEnum


* `BI_ENGINE_ACCELERATION_MODE_UNSPECIFIED` (value: `"BI_ENGINE_ACCELERATION_MODE_UNSPECIFIED"`)

* `BI_ENGINE_DISABLED` (value: `"BI_ENGINE_DISABLED"`)

* `PARTIAL_INPUT` (value: `"PARTIAL_INPUT"`)

* `FULL_INPUT` (value: `"FULL_INPUT"`)

* `FULL_QUERY` (value: `"FULL_QUERY"`)





## Enum: BiEngineModeEnum


* `ACCELERATION_MODE_UNSPECIFIED` (value: `"ACCELERATION_MODE_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `PARTIAL` (value: `"PARTIAL"`)

* `FULL` (value: `"FULL"`)




