

# DynamicEndpointConfig

[#next-free-field: 6]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientStatus** | [**ClientStatusEnum**](#ClientStatusEnum) | The client status of this resource. [#not-implemented-hide:] |  [optional] |
|**endpointConfig** | **Map&lt;String, Object&gt;** | The endpoint config. |  [optional] |
|**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  |  [optional] |
|**lastUpdated** | **String** | [#not-implemented-hide:] The timestamp when the Endpoint was last updated. |  [optional] |
|**versionInfo** | **String** | [#not-implemented-hide:] This is the per-resource version information. This version is currently taken from the :ref:&#x60;version_info &#x60; field at the time that the endpoint configuration was loaded. |  [optional] |



## Enum: ClientStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| REQUESTED | &quot;REQUESTED&quot; |
| DOES_NOT_EXIST | &quot;DOES_NOT_EXIST&quot; |
| ACKED | &quot;ACKED&quot; |
| NACKED | &quot;NACKED&quot; |



