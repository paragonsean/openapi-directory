

# ServicePerimeter

`ServicePerimeter` describes a set of Google Cloud resources which can freely import and export data amongst themselves, but not export outside of the `ServicePerimeter`. If a request with a source within this `ServicePerimeter` has a target outside of the `ServicePerimeter`, the request will be blocked. Otherwise the request is allowed. There are two types of Service Perimeter - Regular and Bridge. Regular Service Perimeters cannot overlap, a single Google Cloud project can only belong to a single regular Service Perimeter. Service Perimeter Bridges can contain only Google Cloud projects as members, a single Google Cloud project may belong to multiple Service Perimeter Bridges.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the &#x60;ServicePerimeter&#x60; and its use. Does not affect behavior. |  [optional] |
|**name** | **String** | Resource name for the &#x60;ServicePerimeter&#x60;. Format: &#x60;accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}&#x60;. The &#x60;service_perimeter&#x60; component must begin with a letter, followed by alphanumeric characters or &#x60;_&#x60;. After you create a &#x60;ServicePerimeter&#x60;, you cannot change its &#x60;name&#x60;. |  [optional] |
|**perimeterType** | [**PerimeterTypeEnum**](#PerimeterTypeEnum) | Perimeter type indicator. A single project is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, restricted/unrestricted service lists as well as access lists must be empty. |  [optional] |
|**status** | [**ServicePerimeterConfig**](ServicePerimeterConfig.md) |  |  [optional] |
|**title** | **String** | Human readable title. Must be unique within the Policy. |  [optional] |



## Enum: PerimeterTypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;PERIMETER_TYPE_REGULAR&quot; |
| BRIDGE | &quot;PERIMETER_TYPE_BRIDGE&quot; |



