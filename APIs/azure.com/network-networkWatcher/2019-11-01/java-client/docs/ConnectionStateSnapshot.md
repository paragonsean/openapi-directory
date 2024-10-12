

# ConnectionStateSnapshot

Connection state snapshot.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avgLatencyInMs** | **Integer** | Average latency in ms. |  [optional] |
|**connectionState** | [**ConnectionStateEnum**](#ConnectionStateEnum) | The connection state. |  [optional] |
|**endTime** | **OffsetDateTime** | The end time of the connection snapshot. |  [optional] |
|**evaluationState** | [**EvaluationStateEnum**](#EvaluationStateEnum) | Connectivity analysis evaluation state. |  [optional] |
|**hops** | [**List&lt;ConnectionStateSnapshotHopsInner&gt;**](ConnectionStateSnapshotHopsInner.md) | List of hops between the source and the destination. |  [optional] [readonly] |
|**maxLatencyInMs** | **Integer** | Maximum latency in ms. |  [optional] |
|**minLatencyInMs** | **Integer** | Minimum latency in ms. |  [optional] |
|**probesFailed** | **Integer** | The number of failed probes. |  [optional] |
|**probesSent** | **Integer** | The number of sent probes. |  [optional] |
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



