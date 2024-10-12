

# DynamicScopedRouteConfigs

[#next-free-field: 7]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientStatus** | [**ClientStatusEnum**](#ClientStatusEnum) | The client status of this resource. [#not-implemented-hide:] |  [optional] |
|**errorState** | [**UpdateFailureState**](UpdateFailureState.md) |  |  [optional] |
|**lastUpdated** | **String** | The timestamp when the scoped route config set was last updated. |  [optional] |
|**name** | **String** | The name assigned to the scoped route configurations. |  [optional] |
|**scopedRouteConfigs** | **List&lt;Map&lt;String, Object&gt;&gt;** | The scoped route configurations. |  [optional] |
|**versionInfo** | **String** | This is the per-resource version information. This version is currently taken from the :ref:&#x60;version_info &#x60; field at the time that the scoped routes configuration was loaded. |  [optional] |



## Enum: ClientStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| REQUESTED | &quot;REQUESTED&quot; |
| DOES_NOT_EXIST | &quot;DOES_NOT_EXIST&quot; |
| ACKED | &quot;ACKED&quot; |
| NACKED | &quot;NACKED&quot; |



