

# BiEngineStatistics

Statistics for a BI Engine specific query. Populated as part of JobStatistics2

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accelerationMode** | [**AccelerationModeEnum**](#AccelerationModeEnum) | Output only. Specifies which mode of BI Engine acceleration was performed (if any). |  [optional] [readonly] |
|**biEngineMode** | [**BiEngineModeEnum**](#BiEngineModeEnum) | Output only. Specifies which mode of BI Engine acceleration was performed (if any). |  [optional] [readonly] |
|**biEngineReasons** | [**List&lt;BiEngineReason&gt;**](BiEngineReason.md) | In case of DISABLED or PARTIAL bi_engine_mode, these contain the explanatory reasons as to why BI Engine could not accelerate. In case the full query was accelerated, this field is not populated. |  [optional] |



## Enum: AccelerationModeEnum

| Name | Value |
|---- | -----|
| BI_ENGINE_ACCELERATION_MODE_UNSPECIFIED | &quot;BI_ENGINE_ACCELERATION_MODE_UNSPECIFIED&quot; |
| BI_ENGINE_DISABLED | &quot;BI_ENGINE_DISABLED&quot; |
| PARTIAL_INPUT | &quot;PARTIAL_INPUT&quot; |
| FULL_INPUT | &quot;FULL_INPUT&quot; |
| FULL_QUERY | &quot;FULL_QUERY&quot; |



## Enum: BiEngineModeEnum

| Name | Value |
|---- | -----|
| ACCELERATION_MODE_UNSPECIFIED | &quot;ACCELERATION_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| PARTIAL | &quot;PARTIAL&quot; |
| FULL | &quot;FULL&quot; |



