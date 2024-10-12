# AnthosOnPremApi.OperationStage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | Time the stage ended. | [optional] 
**metrics** | [**[Metric]**](Metric.md) | Progress metric bundle. | [optional] 
**stage** | **String** | The high-level stage of the operation. | [optional] 
**startTime** | **String** | Time the stage started. | [optional] 
**state** | **String** | Output only. State of the stage. | [optional] [readonly] 



## Enum: StageEnum


* `STAGE_UNSPECIFIED` (value: `"STAGE_UNSPECIFIED"`)

* `PREFLIGHT_CHECK` (value: `"PREFLIGHT_CHECK"`)

* `CONFIGURE` (value: `"CONFIGURE"`)

* `DEPLOY` (value: `"DEPLOY"`)

* `HEALTH_CHECK` (value: `"HEALTH_CHECK"`)

* `UPDATE` (value: `"UPDATE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




