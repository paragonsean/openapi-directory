

# TransitionExecutions


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executions** | [**List&lt;TransitionExecutionsExecutionsInner&gt;**](TransitionExecutionsExecutionsInner.md) |  |  |
|**nextToken** | **String** |  |  |
|**status** | [**List&lt;StatusEnum&gt;**](#List&lt;StatusEnum&gt;) |  |  [optional] |
|**transitionId** | [**LogsTransitionId**](LogsTransitionId.md) |  |  |



## Enum: List&lt;StatusEnum&gt;

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |
| REJECTED | &quot;rejected&quot; |
| RETRY | &quot;retry&quot; |



