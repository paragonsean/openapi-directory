

# Execution

Message describing Execution object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | Output only. [Output only] End time stamp |  [optional] [readonly] |
|**evaluationId** | **String** | Output only. [Output only] Evaluation ID |  [optional] [readonly] |
|**inventoryTime** | **String** | Output only. [Output only] Inventory time stamp |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs |  [optional] |
|**name** | **String** | The name of execution resource. The format is projects/{project}/locations/{location}/evaluations/{evaluation}/executions/{execution} |  [optional] |
|**runType** | [**RunTypeEnum**](#RunTypeEnum) | type represent whether the execution executed directly by user or scheduled according evaluation.schedule field. |  [optional] |
|**startTime** | **String** | Output only. [Output only] Start time stamp |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. [Output only] State |  [optional] [readonly] |



## Enum: RunTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| ONE_TIME | &quot;ONE_TIME&quot; |
| SCHEDULED | &quot;SCHEDULED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



