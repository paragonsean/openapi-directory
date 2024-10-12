# WorkflowExecutionsApi.StepEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The creation time of the step entry. | [optional] [readonly] 
**entryId** | **String** | Output only. The numeric ID of this step entry, used for navigation. | [optional] [readonly] 
**exception** | [**Exception**](Exception.md) |  | [optional] 
**name** | **String** | Output only. The full resource name of the step entry. Each step entry has a unique entry ID, which is a monotonically increasing counter. Step entry names have the format: &#x60;projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}/stepEntries/{step_entry}&#x60;. | [optional] [readonly] 
**navigationInfo** | [**NavigationInfo**](NavigationInfo.md) |  | [optional] 
**routine** | **String** | Output only. The name of the routine this step entry belongs to. A routine name is the subworkflow name defined in the YAML source code. The top level routine name is &#x60;main&#x60;. | [optional] [readonly] 
**state** | **String** | Output only. The state of the step entry. | [optional] [readonly] 
**step** | **String** | Output only. The name of the step this step entry belongs to. | [optional] [readonly] 
**stepEntryMetadata** | [**StepEntryMetadata**](StepEntryMetadata.md) |  | [optional] 
**stepType** | **String** | Output only. The type of the step this step entry belongs to. | [optional] [readonly] 
**updateTime** | **String** | Output only. The most recently updated time of the step entry. | [optional] [readonly] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"STATE_IN_PROGRESS"`)

* `SUCCEEDED` (value: `"STATE_SUCCEEDED"`)

* `FAILED` (value: `"STATE_FAILED"`)





## Enum: StepTypeEnum


* `TYPE_UNSPECIFIED` (value: `"STEP_TYPE_UNSPECIFIED"`)

* `ASSIGN` (value: `"STEP_ASSIGN"`)

* `STD_LIB_CALL` (value: `"STEP_STD_LIB_CALL"`)

* `CONNECTOR_CALL` (value: `"STEP_CONNECTOR_CALL"`)

* `SUBWORKFLOW_CALL` (value: `"STEP_SUBWORKFLOW_CALL"`)

* `CALL` (value: `"STEP_CALL"`)

* `SWITCH` (value: `"STEP_SWITCH"`)

* `CONDITION` (value: `"STEP_CONDITION"`)

* `FOR` (value: `"STEP_FOR"`)

* `FOR_ITERATION` (value: `"STEP_FOR_ITERATION"`)

* `PARALLEL_FOR` (value: `"STEP_PARALLEL_FOR"`)

* `PARALLEL_BRANCH` (value: `"STEP_PARALLEL_BRANCH"`)

* `PARALLEL_BRANCH_ENTRY` (value: `"STEP_PARALLEL_BRANCH_ENTRY"`)

* `TRY_RETRY_EXCEPT` (value: `"STEP_TRY_RETRY_EXCEPT"`)

* `TRY` (value: `"STEP_TRY"`)

* `RETRY` (value: `"STEP_RETRY"`)

* `EXCEPT` (value: `"STEP_EXCEPT"`)

* `RETURN` (value: `"STEP_RETURN"`)

* `RAISE` (value: `"STEP_RAISE"`)

* `GOTO` (value: `"STEP_GOTO"`)




