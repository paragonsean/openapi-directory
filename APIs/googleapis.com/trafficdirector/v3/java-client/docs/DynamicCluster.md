

# DynamicCluster

Describes a dynamically loaded cluster via the CDS API. [#next-free-field: 6]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientStatus** | [**ClientStatusEnum**](#ClientStatusEnum) | The client status of this resource. [#not-implemented-hide:] |  [optional] |
|**cluster** | **Map&lt;String, Object&gt;** | The cluster config. |  [optional] |
|**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  |  [optional] |
|**lastUpdated** | **String** | The timestamp when the Cluster was last updated. |  [optional] |
|**versionInfo** | **String** | This is the per-resource version information. This version is currently taken from the :ref:&#x60;version_info &#x60; field at the time that the cluster was loaded. In the future, discrete per-cluster versions may be supported by the API. |  [optional] |



## Enum: ClientStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| REQUESTED | &quot;REQUESTED&quot; |
| DOES_NOT_EXIST | &quot;DOES_NOT_EXIST&quot; |
| ACKED | &quot;ACKED&quot; |
| NACKED | &quot;NACKED&quot; |



