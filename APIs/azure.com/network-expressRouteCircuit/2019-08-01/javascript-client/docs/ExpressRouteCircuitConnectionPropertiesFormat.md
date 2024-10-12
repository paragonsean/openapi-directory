# NetworkManagementClient.ExpressRouteCircuitConnectionPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPrefix** | **String** | /29 IP address space to carve out Customer addresses for tunnels. | [optional] 
**authorizationKey** | **String** | The authorization key. | [optional] 
**circuitConnectionStatus** | [**CircuitConnectionStatus**](CircuitConnectionStatus.md) |  | [optional] 
**expressRouteCircuitPeering** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  | [optional] 
**peerExpressRouteCircuitPeering** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




