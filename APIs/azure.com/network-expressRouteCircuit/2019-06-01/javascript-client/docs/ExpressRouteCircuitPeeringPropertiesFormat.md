# NetworkManagementClient.ExpressRouteCircuitPeeringPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureASN** | **Number** | The Azure ASN. | [optional] 
**connections** | [**[ExpressRouteCircuitConnection]**](ExpressRouteCircuitConnection.md) | The list of circuit connections associated with Azure Private Peering for this circuit. | [optional] 
**expressRouteConnection** | [**ExpressRouteCircuitPeeringPropertiesFormatExpressRouteConnection**](ExpressRouteCircuitPeeringPropertiesFormatExpressRouteConnection.md) |  | [optional] 
**gatewayManagerEtag** | **String** | The GatewayManager Etag. | [optional] 
**ipv6PeeringConfig** | [**Ipv6ExpressRouteCircuitPeeringConfig**](Ipv6ExpressRouteCircuitPeeringConfig.md) |  | [optional] 
**lastModifiedBy** | **String** | Gets whether the provider or the customer last modified the peering. | [optional] 
**microsoftPeeringConfig** | [**ExpressRouteCircuitPeeringConfig**](ExpressRouteCircuitPeeringConfig.md) |  | [optional] 
**peerASN** | **Number** | The peer ASN. | [optional] 
**peeredConnections** | [**[PeerExpressRouteCircuitConnection]**](PeerExpressRouteCircuitConnection.md) | The list of peered circuit connections associated with Azure Private Peering for this circuit. | [optional] [readonly] 
**peeringType** | [**ExpressRoutePeeringType**](ExpressRoutePeeringType.md) |  | [optional] 
**primaryAzurePort** | **String** | The primary port. | [optional] 
**primaryPeerAddressPrefix** | **String** | The primary address prefix. | [optional] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**routeFilter** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  | [optional] 
**secondaryAzurePort** | **String** | The secondary port. | [optional] 
**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. | [optional] 
**sharedKey** | **String** | The shared key. | [optional] 
**state** | [**ExpressRoutePeeringState**](ExpressRoutePeeringState.md) |  | [optional] 
**stats** | [**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md) |  | [optional] 
**vlanId** | **Number** | The VLAN ID. | [optional] 


