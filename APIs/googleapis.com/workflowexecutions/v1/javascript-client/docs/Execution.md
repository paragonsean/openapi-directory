# WorkflowExecutionsApi.Execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument** | **String** | Input parameters of the execution represented as a JSON string. The size limit is 32KB. *Note*: If you are using the REST API directly to run your workflow, you must escape any JSON string value of &#x60;argument&#x60;. Example: &#x60;&#39;{\&quot;argument\&quot;:\&quot;{\\\&quot;firstName\\\&quot;:\\\&quot;FIRST\\\&quot;,\\\&quot;lastName\\\&quot;:\\\&quot;LAST\\\&quot;}\&quot;}&#39;&#x60; | [optional] 
**callLogLevel** | **String** | The call logging level associated to this execution. | [optional] 
**createTime** | **String** | Output only. Marks the creation of the execution. | [optional] [readonly] 
**disableConcurrencyQuotaOverflowBuffering** | **Boolean** | Optional. If set to true, the execution will not be backlogged when the concurrency quota is exhausted. The backlog execution starts when the concurrency quota becomes available. | [optional] 
**duration** | **String** | Output only. Measures the duration of the execution. | [optional] [readonly] 
**endTime** | **String** | Output only. Marks the end of execution, successful or not. | [optional] [readonly] 
**error** | [**Error**](Error.md) |  | [optional] 
**labels** | **{String: String}** | Labels associated with this execution. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. By default, labels are inherited from the workflow but are overridden by any labels associated with the execution. | [optional] 
**name** | **String** | Output only. The resource name of the execution. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution} | [optional] [readonly] 
**result** | **String** | Output only. Output of the execution represented as a JSON string. The value can only be present if the execution&#39;s state is &#x60;SUCCEEDED&#x60;. | [optional] [readonly] 
**startTime** | **String** | Output only. Marks the beginning of execution. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the execution. | [optional] [readonly] 
**stateError** | [**StateError**](StateError.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**workflowRevisionId** | **String** | Output only. Revision of the workflow this execution is using. | [optional] [readonly] 



## Enum: CallLogLevelEnum


* `CALL_LOG_LEVEL_UNSPECIFIED` (value: `"CALL_LOG_LEVEL_UNSPECIFIED"`)

* `LOG_ALL_CALLS` (value: `"LOG_ALL_CALLS"`)

* `LOG_ERRORS_ONLY` (value: `"LOG_ERRORS_ONLY"`)

* `LOG_NONE` (value: `"LOG_NONE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)

* `QUEUED` (value: `"QUEUED"`)




