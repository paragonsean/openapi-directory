# NetworkManagementClient.RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPrefix** | **String** | /29 IP address space to carve out Customer addresses for tunnels. | [optional] 
**authorizationKey** | **String** | The authorization key. | [optional] 
**circuitConnectionStatus** | **String** | Express Route Circuit connection state. | [optional] [readonly] 
**expressRouteCircuitPeering** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  | [optional] 
**peerExpressRouteCircuitPeering** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 



## Enum: CircuitConnectionStatusEnum


* `Connected` (value: `"Connected"`)

* `Connecting` (value: `"Connecting"`)

* `Disconnected` (value: `"Disconnected"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




