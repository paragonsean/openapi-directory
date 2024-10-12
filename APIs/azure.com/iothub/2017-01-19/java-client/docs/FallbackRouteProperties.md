

# FallbackRouteProperties

The properties related to the fallback route based on which the IoT hub routes messages to the fallback endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | **String** | The condition which is evaluated in order to apply the fallback route. If the condition is not provided it will evaluate to true by default. For grammar, See: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language |  [optional] |
|**endpointNames** | **List&lt;String&gt;** | The list of endpoints to which the messages that satisfy the condition are routed to. Currently only 1 endpoint is allowed. |  |
|**isEnabled** | **Boolean** | Used to specify whether the fallback route is enabled or not. |  |
|**source** | [**SourceEnum**](#SourceEnum) | The source to which the routing rule is to be applied to. e.g. DeviceMessages |  |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| DEVICE_MESSAGES | &quot;DeviceMessages&quot; |



