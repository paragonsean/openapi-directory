

# ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfig

Contains IPv6 peering config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**microsoftPeeringConfig** | [**ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigMicrosoftPeeringConfig**](ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigMicrosoftPeeringConfig.md) |  |  [optional] |
|**primaryPeerAddressPrefix** | **String** | The primary address prefix. |  [optional] |
|**routeFilter** | [**ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigRouteFilter**](ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigRouteFilter.md) |  |  [optional] |
|**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of peering. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



