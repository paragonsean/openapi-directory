

# RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfig

Contains IPv6 peering config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**microsoftPeeringConfig** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfigMicrosoftPeeringConfig**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfigMicrosoftPeeringConfig.md) |  |  [optional] |
|**primaryPeerAddressPrefix** | **String** | The primary address prefix. |  [optional] |
|**routeFilter** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  |  [optional] |
|**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of peering. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



