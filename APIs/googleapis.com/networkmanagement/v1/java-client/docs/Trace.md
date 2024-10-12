

# Trace

Trace represents one simulated packet forwarding path. * Each trace contains multiple ordered steps. * Each step is in a particular state with associated configuration. * State is categorized as final or non-final states. * Each final state has a reason associated. * Each trace must end with a final state (the last step). ``` |---------------------Trace----------------------| Step1(State) Step2(State) --- StepN(State(final)) ```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointInfo** | [**EndpointInfo**](EndpointInfo.md) |  |  [optional] |
|**forwardTraceId** | **Integer** | ID of trace. For forward traces, this ID is unique for each trace. For return traces, it matches ID of associated forward trace. A single forward trace can be associated with none, one or more than one return trace. |  [optional] |
|**steps** | [**List&lt;Step&gt;**](Step.md) | A trace of a test contains multiple steps from the initial state to the final state (delivered, dropped, forwarded, or aborted). The steps are ordered by the processing sequence within the simulated network state machine. It is critical to preserve the order of the steps and avoid reordering or sorting them. |  [optional] |



