

# RoutingProperties

The routing related properties of the IoT hub. See: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoints** | [**RoutingEndpoints**](RoutingEndpoints.md) |  |  [optional] |
|**fallbackRoute** | [**FallbackRouteProperties**](FallbackRouteProperties.md) |  |  [optional] |
|**routes** | [**List&lt;RouteProperties&gt;**](RouteProperties.md) | The list of user-provided routing rules that the IoT hub uses to route messages to built-in and custom endpoints. A maximum of 100 routing rules are allowed for paid hubs and a maximum of 5 routing rules are allowed for free hubs. |  [optional] |



