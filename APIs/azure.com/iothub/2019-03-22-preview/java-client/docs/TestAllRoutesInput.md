

# TestAllRoutesInput

Input for testing all routes

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**RoutingMessage**](RoutingMessage.md) |  |  [optional] |
|**routingSource** | [**RoutingSourceEnum**](#RoutingSourceEnum) | Routing source |  [optional] |
|**twin** | [**RoutingTwin**](RoutingTwin.md) |  |  [optional] |



## Enum: RoutingSourceEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DEVICE_MESSAGES | &quot;DeviceMessages&quot; |
| TWIN_CHANGE_EVENTS | &quot;TwinChangeEvents&quot; |
| DEVICE_LIFECYCLE_EVENTS | &quot;DeviceLifecycleEvents&quot; |
| DEVICE_JOB_LIFECYCLE_EVENTS | &quot;DeviceJobLifecycleEvents&quot; |



