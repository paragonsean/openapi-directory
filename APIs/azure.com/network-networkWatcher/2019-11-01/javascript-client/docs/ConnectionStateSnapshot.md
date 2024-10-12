# NetworkManagementClient.ConnectionStateSnapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgLatencyInMs** | **Number** | Average latency in ms. | [optional] 
**connectionState** | **String** | The connection state. | [optional] 
**endTime** | **Date** | The end time of the connection snapshot. | [optional] 
**evaluationState** | **String** | Connectivity analysis evaluation state. | [optional] 
**hops** | [**[ConnectionStateSnapshotHopsInner]**](ConnectionStateSnapshotHopsInner.md) | List of hops between the source and the destination. | [optional] [readonly] 
**maxLatencyInMs** | **Number** | Maximum latency in ms. | [optional] 
**minLatencyInMs** | **Number** | Minimum latency in ms. | [optional] 
**probesFailed** | **Number** | The number of failed probes. | [optional] 
**probesSent** | **Number** | The number of sent probes. | [optional] 
**startTime** | **Date** | The start time of the connection snapshot. | [optional] 



## Enum: ConnectionStateEnum


* `Reachable` (value: `"Reachable"`)

* `Unreachable` (value: `"Unreachable"`)

* `Unknown` (value: `"Unknown"`)





## Enum: EvaluationStateEnum


* `NotStarted` (value: `"NotStarted"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)




