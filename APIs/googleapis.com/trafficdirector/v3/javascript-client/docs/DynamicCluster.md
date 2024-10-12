# TrafficDirectorApi.DynamicCluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientStatus** | **String** | The client status of this resource. [#not-implemented-hide:] | [optional] 
**cluster** | **{String: Object}** | The cluster config. | [optional] 
**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  | [optional] 
**lastUpdated** | **String** | The timestamp when the Cluster was last updated. | [optional] 
**versionInfo** | **String** | This is the per-resource version information. This version is currently taken from the :ref:&#x60;version_info &#x60; field at the time that the cluster was loaded. In the future, discrete per-cluster versions may be supported by the API. | [optional] 



## Enum: ClientStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `REQUESTED` (value: `"REQUESTED"`)

* `DOES_NOT_EXIST` (value: `"DOES_NOT_EXIST"`)

* `ACKED` (value: `"ACKED"`)

* `NACKED` (value: `"NACKED"`)




