

# RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerProperties

Properties of the express route circuit connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressPrefix** | **String** | /29 IP address space to carve out Customer addresses for tunnels. |  [optional] |
|**authorizationKey** | **String** | The authorization key. |  [optional] |
|**circuitConnectionStatus** | [**CircuitConnectionStatusEnum**](#CircuitConnectionStatusEnum) | Express Route Circuit connection state. |  [optional] [readonly] |
|**expressRouteCircuitPeering** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  |  [optional] |
|**peerExpressRouteCircuitPeering** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  |  [optional] |
|**provisioningState** | **String** | Provisioning state of the circuit connection resource. Possible values are: &#39;Succeeded&#39;, &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |



## Enum: CircuitConnectionStatusEnum

| Name | Value |
|---- | -----|
| CONNECTED | &quot;Connected&quot; |
| CONNECTING | &quot;Connecting&quot; |
| DISCONNECTED | &quot;Disconnected&quot; |



