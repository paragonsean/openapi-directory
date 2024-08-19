# WorkflowExecutionsApi.Execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument** | **String** | Input parameters of the execution represented as a JSON string. The size limit is 32KB. *Note*: If you are using the REST API directly to run your workflow, you must escape any JSON string value of &#x60;argument&#x60;. Example: &#x60;&#39;{\&quot;argument\&quot;:\&quot;{\\\&quot;firstName\\\&quot;:\\\&quot;FIRST\\\&quot;,\\\&quot;lastName\\\&quot;:\\\&quot;LAST\\\&quot;}\&quot;}&#39;&#x60; | [optional] 
**callLogLevel** | **String** | The call logging level associated to this execution. | [optional] 
**endTime** | **String** | Output only. Marks the end of execution, successful or not. | [optional] [readonly] 
**error** | [**Error**](Error.md) |  | [optional] 
**name** | **String** | Output only. The resource name of the execution. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution} | [optional] [readonly] 
**result** | **String** | Output only. Output of the execution represented as a JSON string. The value can only be present if the execution&#39;s state is &#x60;SUCCEEDED&#x60;. | [optional] [readonly] 
**startTime** | **String** | Output only. Marks the beginning of execution. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the execution. | [optional] [readonly] 
**status** | [**Status**](Status.md) |  | [optional] 
**workflowRevisionId** | **String** | Output only. Revision of the workflow this execution is using. | [optional] [readonly] 



## Enum: CallLogLevelEnum


* `CALL_LOG_LEVEL_UNSPECIFIED` (value: `"CALL_LOG_LEVEL_UNSPECIFIED"`)

* `LOG_ALL_CALLS` (value: `"LOG_ALL_CALLS"`)

* `LOG_ERRORS_ONLY` (value: `"LOG_ERRORS_ONLY"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)

* `QUEUED` (value: `"QUEUED"`)




