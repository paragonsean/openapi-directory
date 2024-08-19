

# ConnectionStateSnapshot

Connection state snapshot.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionState** | [**ConnectionStateEnum**](#ConnectionStateEnum) | The connection state. |  [optional] |
|**endTime** | **OffsetDateTime** | The end time of the connection snapshot. |  [optional] |
|**evaluationState** | [**EvaluationStateEnum**](#EvaluationStateEnum) | Connectivity analysis evaluation state. |  [optional] |
|**hops** | [**List&lt;ConnectivityHop&gt;**](ConnectivityHop.md) | List of hops between the source and the destination. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The start time of the connection snapshot. |  [optional] |



## Enum: ConnectionStateEnum

| Name | Value |
|---- | -----|
| REACHABLE | &quot;Reachable&quot; |
| UNREACHABLE | &quot;Unreachable&quot; |
| UNKNOWN | &quot;Unknown&quot; |



## Enum: EvaluationStateEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;NotStarted&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |



