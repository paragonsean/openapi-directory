# NetworkManagementClient.ConnectionStateSnapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionState** | **String** | The connection state. | [optional] 
**endTime** | **Date** | The end time of the connection snapshot. | [optional] 
**evaluationState** | **String** | Connectivity analysis evaluation state. | [optional] 
**hops** | [**[ConnectivityHop]**](ConnectivityHop.md) | List of hops between the source and the destination. | [optional] [readonly] 
**startTime** | **Date** | The start time of the connection snapshot. | [optional] 



## Enum: ConnectionStateEnum


* `Reachable` (value: `"Reachable"`)

* `Unreachable` (value: `"Unreachable"`)

* `Unknown` (value: `"Unknown"`)





## Enum: EvaluationStateEnum


* `NotStarted` (value: `"NotStarted"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)




