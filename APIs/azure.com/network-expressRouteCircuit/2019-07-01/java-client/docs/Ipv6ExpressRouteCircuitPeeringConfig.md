

# Ipv6ExpressRouteCircuitPeeringConfig

Contains IPv6 peering config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**microsoftPeeringConfig** | [**ExpressRouteCircuitPeeringConfig**](ExpressRouteCircuitPeeringConfig.md) |  |  [optional] |
|**primaryPeerAddressPrefix** | **String** | The primary address prefix. |  [optional] |
|**routeFilter** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  |  [optional] |
|**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of peering. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



