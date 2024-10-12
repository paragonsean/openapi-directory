

# WorkflowExecutions


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executions** | [**List&lt;WorkflowExecutionsExecutionsInner&gt;**](WorkflowExecutionsExecutionsInner.md) |  |  |
|**nextToken** | **String** |  |  |
|**order** | [**OrderEnum**](#OrderEnum) |  |  [optional] |
|**sortBy** | [**SortByEnum**](#SortByEnum) |  |  [optional] |
|**status** | [**List&lt;StatusEnum&gt;**](#List&lt;StatusEnum&gt;) |  |  [optional] |
|**workflowId** | **String** |  |  |



## Enum: OrderEnum

| Name | Value |
|---- | -----|
| ASCENDING | &quot;ascending&quot; |
| DESCENDING | &quot;descending&quot; |



## Enum: SortByEnum

| Name | Value |
|---- | -----|
| START_TIME | &quot;startTime&quot; |
| END_TIME | &quot;endTime&quot; |



## Enum: List&lt;StatusEnum&gt;

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |
| REJECTED | &quot;rejected&quot; |
| RETRY | &quot;retry&quot; |
| ERROR | &quot;error&quot; |



