# WorkloadManagerApi.Execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | Output only. [Output only] End time stamp | [optional] [readonly] 
**evaluationId** | **String** | Output only. [Output only] Evaluation ID | [optional] [readonly] 
**inventoryTime** | **String** | Output only. [Output only] Inventory time stamp | [optional] [readonly] 
**labels** | **{String: String}** | Labels as key value pairs | [optional] 
**name** | **String** | The name of execution resource. The format is projects/{project}/locations/{location}/evaluations/{evaluation}/executions/{execution} | [optional] 
**runType** | **String** | type represent whether the execution executed directly by user or scheduled according evaluation.schedule field. | [optional] 
**startTime** | **String** | Output only. [Output only] Start time stamp | [optional] [readonly] 
**state** | **String** | Output only. [Output only] State | [optional] [readonly] 



## Enum: RunTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `ONE_TIME` (value: `"ONE_TIME"`)

* `SCHEDULED` (value: `"SCHEDULED"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




