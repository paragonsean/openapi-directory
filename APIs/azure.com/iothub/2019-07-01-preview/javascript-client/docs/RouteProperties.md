# IotHubClient.RouteProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **String** | The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language | [optional] 
**endpointNames** | **[String]** | The list of endpoints to which messages that satisfy the condition are routed. Currently only one endpoint is allowed. | 
**isEnabled** | **Boolean** | Used to specify whether a route is enabled. | 
**name** | **String** | The name of the route. The name can only include alphanumeric characters, periods, underscores, hyphens, has a maximum length of 64 characters, and must be unique. | 
**source** | **String** | The source that the routing rule is to be applied to, such as DeviceMessages. | 



## Enum: SourceEnum


* `Invalid` (value: `"Invalid"`)

* `DeviceMessages` (value: `"DeviceMessages"`)

* `TwinChangeEvents` (value: `"TwinChangeEvents"`)

* `DeviceLifecycleEvents` (value: `"DeviceLifecycleEvents"`)

* `DeviceJobLifecycleEvents` (value: `"DeviceJobLifecycleEvents"`)

* `DigitalTwinChangeEvents` (value: `"DigitalTwinChangeEvents"`)




