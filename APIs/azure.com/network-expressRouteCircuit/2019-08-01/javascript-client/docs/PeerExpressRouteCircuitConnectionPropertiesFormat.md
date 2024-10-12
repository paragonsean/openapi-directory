# NetworkManagementClient.PeerExpressRouteCircuitConnectionPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPrefix** | **String** | /29 IP address space to carve out Customer addresses for tunnels. | [optional] 
**authResourceGuid** | **String** | The resource guid of the authorization used for the express route circuit connection. | [optional] 
**circuitConnectionStatus** | [**CircuitConnectionStatus**](CircuitConnectionStatus.md) |  | [optional] 
**connectionName** | **String** | The name of the express route circuit connection resource. | [optional] 
**expressRouteCircuitPeering** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  | [optional] 
**peerExpressRouteCircuitPeering** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




