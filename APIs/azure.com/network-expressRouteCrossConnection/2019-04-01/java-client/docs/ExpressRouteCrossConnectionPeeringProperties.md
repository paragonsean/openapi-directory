

# ExpressRouteCrossConnectionPeeringProperties

Properties of express route cross connection peering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureASN** | **Integer** | The Azure ASN. |  [optional] [readonly] |
|**gatewayManagerEtag** | **String** | The GatewayManager Etag. |  [optional] |
|**ipv6PeeringConfig** | [**ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfig**](ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfig.md) |  |  [optional] |
|**lastModifiedBy** | **String** | Gets whether the provider or the customer last modified the peering. |  [optional] |
|**microsoftPeeringConfig** | [**ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigMicrosoftPeeringConfig**](ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigMicrosoftPeeringConfig.md) |  |  [optional] |
|**peerASN** | **Long** | The peer ASN. |  [optional] |
|**peeringType** | [**PeeringTypeEnum**](#PeeringTypeEnum) | The peering type. |  [optional] |
|**primaryAzurePort** | **String** | The primary port. |  [optional] [readonly] |
|**primaryPeerAddressPrefix** | **String** | The primary address prefix. |  [optional] |
|**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**secondaryAzurePort** | **String** | The secondary port. |  [optional] [readonly] |
|**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. |  [optional] |
|**sharedKey** | **String** | The shared key. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of peering. |  [optional] |
|**vlanId** | **Integer** | The VLAN ID. |  [optional] |



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



