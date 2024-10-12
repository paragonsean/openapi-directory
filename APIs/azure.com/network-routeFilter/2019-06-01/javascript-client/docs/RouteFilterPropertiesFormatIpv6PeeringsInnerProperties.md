# NetworkManagementClient.RouteFilterPropertiesFormatIpv6PeeringsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureASN** | **Number** | The Azure ASN. | [optional] 
**connections** | [**[RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInner]**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInner.md) | The list of circuit connections associated with Azure Private Peering for this circuit. | [optional] 
**expressRouteConnection** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesExpressRouteConnection**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesExpressRouteConnection.md) |  | [optional] 
**gatewayManagerEtag** | **String** | The GatewayManager Etag. | [optional] 
**ipv6PeeringConfig** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfig**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfig.md) |  | [optional] 
**lastModifiedBy** | **String** | Gets whether the provider or the customer last modified the peering. | [optional] 
**microsoftPeeringConfig** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfigMicrosoftPeeringConfig**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfigMicrosoftPeeringConfig.md) |  | [optional] 
**peerASN** | **Number** | The peer ASN. | [optional] 
**peeredConnections** | [**[RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesPeeredConnectionsInner]**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesPeeredConnectionsInner.md) | The list of peered circuit connections associated with Azure Private Peering for this circuit. | [optional] [readonly] 
**peeringType** | **String** | The peering type. | [optional] 
**primaryAzurePort** | **String** | The primary port. | [optional] 
**primaryPeerAddressPrefix** | **String** | The primary address prefix. | [optional] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**routeFilter** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  | [optional] 
**secondaryAzurePort** | **String** | The secondary port. | [optional] 
**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. | [optional] 
**sharedKey** | **String** | The shared key. | [optional] 
**state** | **String** | The state of peering. | [optional] 
**stats** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesStats**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesStats.md) |  | [optional] 
**vlanId** | **Number** | The VLAN ID. | [optional] 



## Enum: PeeringTypeEnum


* `AzurePublicPeering` (value: `"AzurePublicPeering"`)

* `AzurePrivatePeering` (value: `"AzurePrivatePeering"`)

* `MicrosoftPeering` (value: `"MicrosoftPeering"`)





## Enum: StateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




