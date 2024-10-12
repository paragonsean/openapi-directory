

# DynamicListener

Describes a dynamically loaded listener via the LDS API. [#next-free-field: 7]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeState** | [**DynamicListenerState**](DynamicListenerState.md) |  |  [optional] |
|**clientStatus** | [**ClientStatusEnum**](#ClientStatusEnum) | The client status of this resource. [#not-implemented-hide:] |  [optional] |
|**drainingState** | [**DynamicListenerState**](DynamicListenerState.md) |  |  [optional] |
|**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  |  [optional] |
|**name** | **String** | The name or unique id of this listener, pulled from the DynamicListenerState config. |  [optional] |
|**warmingState** | [**DynamicListenerState**](DynamicListenerState.md) |  |  [optional] |



## Enum: ClientStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| REQUESTED | &quot;REQUESTED&quot; |
| DOES_NOT_EXIST | &quot;DOES_NOT_EXIST&quot; |
| ACKED | &quot;ACKED&quot; |
| NACKED | &quot;NACKED&quot; |



