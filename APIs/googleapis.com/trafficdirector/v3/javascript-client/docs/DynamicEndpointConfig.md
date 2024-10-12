# TrafficDirectorApi.DynamicEndpointConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientStatus** | **String** | The client status of this resource. [#not-implemented-hide:] | [optional] 
**endpointConfig** | **{String: Object}** | The endpoint config. | [optional] 
**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  | [optional] 
**lastUpdated** | **String** | [#not-implemented-hide:] The timestamp when the Endpoint was last updated. | [optional] 
**versionInfo** | **String** | [#not-implemented-hide:] This is the per-resource version information. This version is currently taken from the :ref:&#x60;version_info &#x60; field at the time that the endpoint configuration was loaded. | [optional] 



## Enum: ClientStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `REQUESTED` (value: `"REQUESTED"`)

* `DOES_NOT_EXIST` (value: `"DOES_NOT_EXIST"`)

* `ACKED` (value: `"ACKED"`)

* `NACKED` (value: `"NACKED"`)




