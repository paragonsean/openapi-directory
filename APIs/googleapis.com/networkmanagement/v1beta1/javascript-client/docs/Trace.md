# NetworkManagementApi.Trace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpointInfo** | [**EndpointInfo**](EndpointInfo.md) |  | [optional] 
**forwardTraceId** | **Number** | ID of trace. For forward traces, this ID is unique for each trace. For return traces, it matches ID of associated forward trace. A single forward trace can be associated with none, one or more than one return trace. | [optional] 
**steps** | [**[Step]**](Step.md) | A trace of a test contains multiple steps from the initial state to the final state (delivered, dropped, forwarded, or aborted). The steps are ordered by the processing sequence within the simulated network state machine. It is critical to preserve the order of the steps and avoid reordering or sorting them. | [optional] 


