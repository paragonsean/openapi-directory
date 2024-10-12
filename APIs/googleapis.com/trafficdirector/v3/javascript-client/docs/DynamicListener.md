# TrafficDirectorApi.DynamicListener

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeState** | [**DynamicListenerState**](DynamicListenerState.md) |  | [optional] 
**clientStatus** | **String** | The client status of this resource. [#not-implemented-hide:] | [optional] 
**drainingState** | [**DynamicListenerState**](DynamicListenerState.md) |  | [optional] 
**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  | [optional] 
**name** | **String** | The name or unique id of this listener, pulled from the DynamicListenerState config. | [optional] 
**warmingState** | [**DynamicListenerState**](DynamicListenerState.md) |  | [optional] 



## Enum: ClientStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `REQUESTED` (value: `"REQUESTED"`)

* `DOES_NOT_EXIST` (value: `"DOES_NOT_EXIST"`)

* `ACKED` (value: `"ACKED"`)

* `NACKED` (value: `"NACKED"`)




