

# RouteProperties

The properties of a routing rule that your IoT hub uses to route messages to endpoints.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | **String** | The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, See: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language |  [optional] |
|**endpointNames** | **List&lt;String&gt;** | The list of endpoints to which messages that satisfy the condition are routed. Currently only one endpoint is allowed. |  |
|**isEnabled** | **Boolean** | Used to specify whether a route is enabled. |  |
|**name** | **String** | The name of the route. The name can only include alphanumeric characters, periods, underscores, hyphens, has a maximum length of 64 characters,  and must be unique. |  |
|**source** | [**SourceEnum**](#SourceEnum) | The source that the routing rule is to be applied to, such as DeviceMessages. |  |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| DEVICE_MESSAGES | &quot;DeviceMessages&quot; |
| TWIN_CHANGE_EVENTS | &quot;TwinChangeEvents&quot; |
| DEVICE_LIFECYCLE_EVENTS | &quot;DeviceLifecycleEvents&quot; |
| DEVICE_JOB_LIFECYCLE_EVENTS | &quot;DeviceJobLifecycleEvents&quot; |



