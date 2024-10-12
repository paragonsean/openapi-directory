

# PeerExpressRouteCircuitConnectionPropertiesFormat

Properties of the peer express route circuit connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressPrefix** | **String** | /29 IP address space to carve out Customer addresses for tunnels. |  [optional] |
|**authResourceGuid** | **String** | The resource guid of the authorization used for the express route circuit connection. |  [optional] |
|**circuitConnectionStatus** | **CircuitConnectionStatus** |  |  [optional] |
|**connectionName** | **String** | The name of the express route circuit connection resource. |  [optional] |
|**expressRouteCircuitPeering** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  |  [optional] |
|**peerExpressRouteCircuitPeering** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



