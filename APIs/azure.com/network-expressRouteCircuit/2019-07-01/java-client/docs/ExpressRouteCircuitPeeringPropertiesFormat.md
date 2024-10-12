

# ExpressRouteCircuitPeeringPropertiesFormat

Properties of the express route circuit peering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureASN** | **Integer** | The Azure ASN. |  [optional] |
|**connections** | [**List&lt;ExpressRouteCircuitConnection&gt;**](ExpressRouteCircuitConnection.md) | The list of circuit connections associated with Azure Private Peering for this circuit. |  [optional] |
|**expressRouteConnection** | [**ExpressRouteCircuitPeeringPropertiesFormatExpressRouteConnection**](ExpressRouteCircuitPeeringPropertiesFormatExpressRouteConnection.md) |  |  [optional] |
|**gatewayManagerEtag** | **String** | The GatewayManager Etag. |  [optional] |
|**ipv6PeeringConfig** | [**Ipv6ExpressRouteCircuitPeeringConfig**](Ipv6ExpressRouteCircuitPeeringConfig.md) |  |  [optional] |
|**lastModifiedBy** | **String** | Who was the last to modify the peering. |  [optional] |
|**microsoftPeeringConfig** | [**ExpressRouteCircuitPeeringConfig**](ExpressRouteCircuitPeeringConfig.md) |  |  [optional] |
|**peerASN** | **Long** | The peer ASN. |  [optional] |
|**peeredConnections** | [**List&lt;PeerExpressRouteCircuitConnection&gt;**](PeerExpressRouteCircuitConnection.md) | The list of peered circuit connections associated with Azure Private Peering for this circuit. |  [optional] [readonly] |
|**peeringType** | **ExpressRoutePeeringType** |  |  [optional] |
|**primaryAzurePort** | **String** | The primary port. |  [optional] |
|**primaryPeerAddressPrefix** | **String** | The primary address prefix. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**routeFilter** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  |  [optional] |
|**secondaryAzurePort** | **String** | The secondary port. |  [optional] |
|**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. |  [optional] |
|**sharedKey** | **String** | The shared key. |  [optional] |
|**state** | **ExpressRoutePeeringState** |  |  [optional] |
|**stats** | [**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md) |  |  [optional] |
|**vlanId** | **Integer** | The VLAN ID. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



