# NetworkManagementClient.ExpressRouteCircuitPeeringPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureASN** | **Number** | The Azure ASN. | [optional] 
**connections** | [**[ExpressRouteCircuitConnection]**](ExpressRouteCircuitConnection.md) | The list of circuit connections associated with Azure Private Peering for this circuit. | [optional] 
**expressRouteConnection** | [**ExpressRouteCircuitPeeringPropertiesFormatExpressRouteConnection**](ExpressRouteCircuitPeeringPropertiesFormatExpressRouteConnection.md) |  | [optional] 
**gatewayManagerEtag** | **String** | The GatewayManager Etag. | [optional] 
**ipv6PeeringConfig** | [**Ipv6ExpressRouteCircuitPeeringConfig**](Ipv6ExpressRouteCircuitPeeringConfig.md) |  | [optional] 
**lastModifiedBy** | **String** | Who was the last to modify the peering. | [optional] 
**microsoftPeeringConfig** | [**ExpressRouteCircuitPeeringConfig**](ExpressRouteCircuitPeeringConfig.md) |  | [optional] 
**peerASN** | **Number** | The peer ASN. | [optional] 
**peeredConnections** | [**[PeerExpressRouteCircuitConnection]**](PeerExpressRouteCircuitConnection.md) | The list of peered circuit connections associated with Azure Private Peering for this circuit. | [optional] [readonly] 
**peeringType** | [**ExpressRoutePeeringType**](ExpressRoutePeeringType.md) |  | [optional] 
**primaryAzurePort** | **String** | The primary port. | [optional] 
**primaryPeerAddressPrefix** | **String** | The primary address prefix. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**routeFilter** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  | [optional] 
**secondaryAzurePort** | **String** | The secondary port. | [optional] 
**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. | [optional] 
**sharedKey** | **String** | The shared key. | [optional] 
**state** | [**ExpressRoutePeeringState**](ExpressRoutePeeringState.md) |  | [optional] 
**stats** | [**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md) |  | [optional] 
**vlanId** | **Number** | The VLAN ID. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




