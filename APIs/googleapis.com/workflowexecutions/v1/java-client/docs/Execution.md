

# Execution

A running instance of a [Workflow](/workflows/docs/reference/rest/v1/projects.locations.workflows).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**argument** | **String** | Input parameters of the execution represented as a JSON string. The size limit is 32KB. *Note*: If you are using the REST API directly to run your workflow, you must escape any JSON string value of &#x60;argument&#x60;. Example: &#x60;&#39;{\&quot;argument\&quot;:\&quot;{\\\&quot;firstName\\\&quot;:\\\&quot;FIRST\\\&quot;,\\\&quot;lastName\\\&quot;:\\\&quot;LAST\\\&quot;}\&quot;}&#39;&#x60; |  [optional] |
|**callLogLevel** | [**CallLogLevelEnum**](#CallLogLevelEnum) | The call logging level associated to this execution. |  [optional] |
|**createTime** | **String** | Output only. Marks the creation of the execution. |  [optional] [readonly] |
|**disableConcurrencyQuotaOverflowBuffering** | **Boolean** | Optional. If set to true, the execution will not be backlogged when the concurrency quota is exhausted. The backlog execution starts when the concurrency quota becomes available. |  [optional] |
|**duration** | **String** | Output only. Measures the duration of the execution. |  [optional] [readonly] |
|**endTime** | **String** | Output only. Marks the end of execution, successful or not. |  [optional] [readonly] |
|**error** | [**Error**](Error.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels associated with this execution. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. By default, labels are inherited from the workflow but are overridden by any labels associated with the execution. |  [optional] |
|**name** | **String** | Output only. The resource name of the execution. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution} |  [optional] [readonly] |
|**result** | **String** | Output only. Output of the execution represented as a JSON string. The value can only be present if the execution&#39;s state is &#x60;SUCCEEDED&#x60;. |  [optional] [readonly] |
|**startTime** | **String** | Output only. Marks the beginning of execution. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the execution. |  [optional] [readonly] |
|**stateError** | [**StateError**](StateError.md) |  |  [optional] |
|**status** | [**Status**](Status.md) |  |  [optional] |
|**workflowRevisionId** | **String** | Output only. Revision of the workflow this execution is using. |  [optional] [readonly] |



## Enum: CallLogLevelEnum

| Name | Value |
|---- | -----|
| CALL_LOG_LEVEL_UNSPECIFIED | &quot;CALL_LOG_LEVEL_UNSPECIFIED&quot; |
| LOG_ALL_CALLS | &quot;LOG_ALL_CALLS&quot; |
| LOG_ERRORS_ONLY | &quot;LOG_ERRORS_ONLY&quot; |
| LOG_NONE | &quot;LOG_NONE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |
| QUEUED | &quot;QUEUED&quot; |



