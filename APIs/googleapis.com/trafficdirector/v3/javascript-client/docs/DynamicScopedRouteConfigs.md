# TrafficDirectorApi.DynamicScopedRouteConfigs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientStatus** | **String** | The client status of this resource. [#not-implemented-hide:] | [optional] 
**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  | [optional] 
**lastUpdated** | **String** | The timestamp when the scoped route config set was last updated. | [optional] 
**name** | **String** | The name assigned to the scoped route configurations. | [optional] 
**scopedRouteConfigs** | **[{String: Object}]** | The scoped route configurations. | [optional] 
**versionInfo** | **String** | This is the per-resource version information. This version is currently taken from the :ref:&#x60;version_info &#x60; field at the time that the scoped routes configuration was loaded. | [optional] 



## Enum: ClientStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `REQUESTED` (value: `"REQUESTED"`)

* `DOES_NOT_EXIST` (value: `"DOES_NOT_EXIST"`)

* `ACKED` (value: `"ACKED"`)

* `NACKED` (value: `"NACKED"`)




