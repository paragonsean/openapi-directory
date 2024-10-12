# NetworkManagementClient.RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesPeeredConnectionsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPrefix** | **String** | /29 IP address space to carve out Customer addresses for tunnels. | [optional] 
**authResourceGuid** | **String** | The resource guid of the authorization used for the express route circuit connection. | [optional] 
**circuitConnectionStatus** | **String** | Express Route Circuit connection state. | [optional] [readonly] 
**connectionName** | **String** | The name of the express route circuit connection resource. | [optional] 
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




