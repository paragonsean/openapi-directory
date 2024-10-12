

# FallbackRouteProperties

The properties of the fallback route. IoT Hub uses these properties when it routes messages to the fallback endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | **String** | The condition which is evaluated in order to apply the fallback route. If the condition is not provided it will evaluate to true by default. For grammar, See: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language |  [optional] |
|**endpointNames** | **List&lt;String&gt;** | The list of endpoints to which the messages that satisfy the condition are routed to. Currently only 1 endpoint is allowed. |  |
|**isEnabled** | **Boolean** | Used to specify whether the fallback route is enabled. |  |
|**name** | **String** | The name of the route. The name can only include alphanumeric characters, periods, underscores, hyphens, has a maximum length of 64 characters, and must be unique. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | The source to which the routing rule is to be applied to. For example, DeviceMessages |  |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| DEVICE_MESSAGES | &quot;DeviceMessages&quot; |



