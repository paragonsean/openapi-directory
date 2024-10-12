

# RouteFilterPropertiesFormatIpv6PeeringsInnerProperties

Properties of the express route circuit peering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureASN** | **Integer** | The Azure ASN. |  [optional] |
|**connections** | [**List&lt;RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInner&gt;**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInner.md) | The list of circuit connections associated with Azure Private Peering for this circuit. |  [optional] |
|**expressRouteConnection** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesExpressRouteConnection**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesExpressRouteConnection.md) |  |  [optional] |
|**gatewayManagerEtag** | **String** | The GatewayManager Etag. |  [optional] |
|**ipv6PeeringConfig** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfig**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfig.md) |  |  [optional] |
|**lastModifiedBy** | **String** | Who was the last to modify the peering. |  [optional] |
|**microsoftPeeringConfig** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfigMicrosoftPeeringConfig**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfigMicrosoftPeeringConfig.md) |  |  [optional] |
|**peerASN** | **Long** | The peer ASN. |  [optional] |
|**peeredConnections** | [**List&lt;RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesPeeredConnectionsInner&gt;**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesPeeredConnectionsInner.md) | The list of peered circuit connections associated with Azure Private Peering for this circuit. |  [optional] [readonly] |
|**peeringType** | [**PeeringTypeEnum**](#PeeringTypeEnum) | The peering type. |  [optional] |
|**primaryAzurePort** | **String** | The primary port. |  [optional] |
|**primaryPeerAddressPrefix** | **String** | The primary address prefix. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**routeFilter** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesConnectionsInnerPropertiesExpressRouteCircuitPeering.md) |  |  [optional] |
|**secondaryAzurePort** | **String** | The secondary port. |  [optional] |
|**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. |  [optional] |
|**sharedKey** | **String** | The shared key. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of peering. |  [optional] |
|**stats** | [**RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesStats**](RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesStats.md) |  |  [optional] |
|**vlanId** | **Integer** | The VLAN ID. |  [optional] |



## Enum: PeeringTypeEnum

| Name | Value |
|---- | -----|
| AZURE_PUBLIC_PEERING | &quot;AzurePublicPeering&quot; |
| AZURE_PRIVATE_PEERING | &quot;AzurePrivatePeering&quot; |
| MICROSOFT_PEERING | &quot;MicrosoftPeering&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



