

# ExpressRouteCircuitPeeringPropertiesFormat


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureASN** | **Integer** | Gets or sets the azure ASN |  [optional] |
|**gatewayManagerEtag** | **String** | Gets or sets the GatewayManager Etag |  [optional] |
|**lastModifiedBy** | **String** | Gets whether the provider or the customer last modified the peering |  [optional] |
|**microsoftPeeringConfig** | [**ExpressRouteCircuitPeeringConfig**](ExpressRouteCircuitPeeringConfig.md) |  |  [optional] |
|**peerASN** | **Integer** | Gets or sets the peer ASN |  [optional] |
|**peeringType** | [**PeeringTypeEnum**](#PeeringTypeEnum) | Gets or sets PeeringType |  [optional] |
|**primaryAzurePort** | **String** | Gets or sets the primary port |  [optional] |
|**primaryPeerAddressPrefix** | **String** | Gets or sets the primary address prefix |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**secondaryAzurePort** | **String** | Gets or sets the secondary port |  [optional] |
|**secondaryPeerAddressPrefix** | **String** | Gets or sets the secondary address prefix |  [optional] |
|**sharedKey** | **String** | Gets or sets the shared key |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets state of Peering |  [optional] |
|**stats** | [**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md) |  |  [optional] |
|**vlanId** | **Integer** | Gets or sets the vlan id |  [optional] |



## Enum: PeeringTypeEnum

| Name | Value |
|---- | -----|
| AZURE_PUBLIC_PEERING | &quot;AzurePublicPeering&quot; |
| AZURE_PRIVATE_PEERING | &quot;AzurePrivatePeering&quot; |
| MICROSOFT_PEERING | &quot;MicrosoftPeering&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



