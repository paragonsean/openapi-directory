

# StepEntry

An StepEntry contains debugging information for a step transition in a workflow execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The creation time of the step entry. |  [optional] [readonly] |
|**entryId** | **String** | Output only. The numeric ID of this step entry, used for navigation. |  [optional] [readonly] |
|**exception** | [**Exception**](Exception.md) |  |  [optional] |
|**name** | **String** | Output only. The full resource name of the step entry. Each step entry has a unique entry ID, which is a monotonically increasing counter. Step entry names have the format: &#x60;projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}/stepEntries/{step_entry}&#x60;. |  [optional] [readonly] |
|**navigationInfo** | [**NavigationInfo**](NavigationInfo.md) |  |  [optional] |
|**routine** | **String** | Output only. The name of the routine this step entry belongs to. A routine name is the subworkflow name defined in the YAML source code. The top level routine name is &#x60;main&#x60;. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the step entry. |  [optional] [readonly] |
|**step** | **String** | Output only. The name of the step this step entry belongs to. |  [optional] [readonly] |
|**stepEntryMetadata** | [**StepEntryMetadata**](StepEntryMetadata.md) |  |  [optional] |
|**stepType** | [**StepTypeEnum**](#StepTypeEnum) | Output only. The type of the step this step entry belongs to. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The most recently updated time of the step entry. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;STATE_IN_PROGRESS&quot; |
| SUCCEEDED | &quot;STATE_SUCCEEDED&quot; |
| FAILED | &quot;STATE_FAILED&quot; |



## Enum: StepTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;STEP_TYPE_UNSPECIFIED&quot; |
| ASSIGN | &quot;STEP_ASSIGN&quot; |
| STD_LIB_CALL | &quot;STEP_STD_LIB_CALL&quot; |
| CONNECTOR_CALL | &quot;STEP_CONNECTOR_CALL&quot; |
| SUBWORKFLOW_CALL | &quot;STEP_SUBWORKFLOW_CALL&quot; |
| CALL | &quot;STEP_CALL&quot; |
| SWITCH | &quot;STEP_SWITCH&quot; |
| CONDITION | &quot;STEP_CONDITION&quot; |
| FOR | &quot;STEP_FOR&quot; |
| FOR_ITERATION | &quot;STEP_FOR_ITERATION&quot; |
| PARALLEL_FOR | &quot;STEP_PARALLEL_FOR&quot; |
| PARALLEL_BRANCH | &quot;STEP_PARALLEL_BRANCH&quot; |
| PARALLEL_BRANCH_ENTRY | &quot;STEP_PARALLEL_BRANCH_ENTRY&quot; |
| TRY_RETRY_EXCEPT | &quot;STEP_TRY_RETRY_EXCEPT&quot; |
| TRY | &quot;STEP_TRY&quot; |
| RETRY | &quot;STEP_RETRY&quot; |
| EXCEPT | &quot;STEP_EXCEPT&quot; |
| RETURN | &quot;STEP_RETURN&quot; |
| RAISE | &quot;STEP_RAISE&quot; |
| GOTO | &quot;STEP_GOTO&quot; |



