

# RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesPeeredConnectionsInnerProperties

Properties of the peer express route circuit connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressPrefix** | **String** | /29 IP address space to carve out Customer addresses for tunnels. |  [optional] |
|**authResourceGuid** | **String** | The resource guid of the authorization used for the express route circuit connection. |  [optional] |
|**circuitConnectionStatus** | [**CircuitConnectionStatusEnum**](#CircuitConnectionStatusEnum) | Express Route Circuit connection state. |  [optional] [readonly] |
|**connectionName** | **String** | The name of the express route circuit connection resource. |  [optional] |
|**expressRouteCircuitPeering** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  |  [optional] |
|**peerExpressRouteCircuitPeering** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: CircuitConnectionStatusEnum

| Name | Value |
|---- | -----|
| CONNECTED | &quot;Connected&quot; |
| CONNECTING | &quot;Connecting&quot; |
| DISCONNECTED | &quot;Disconnected&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



