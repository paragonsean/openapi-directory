# TrafficDirectorApi.DynamicRouteConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientStatus** | **String** | The client status of this resource. [#not-implemented-hide:] | [optional] 
**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  | [optional] 
**lastUpdated** | **String** | The timestamp when the Route was last updated. | [optional] 
**routeConfig** | **{String: Object}** | The route config. | [optional] 
**versionInfo** | **String** | This is the per-resource version information. This version is currently taken from the :ref:&#x60;version_info &#x60; field at the time that the route configuration was loaded. | [optional] 



## Enum: ClientStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `REQUESTED` (value: `"REQUESTED"`)

* `DOES_NOT_EXIST` (value: `"DOES_NOT_EXIST"`)

* `ACKED` (value: `"ACKED"`)

* `NACKED` (value: `"NACKED"`)




