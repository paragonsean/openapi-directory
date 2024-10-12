# ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionPeeringProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureASN** | **Number** | The Azure ASN. | [optional] [readonly] 
**gatewayManagerEtag** | **String** | The GatewayManager Etag. | [optional] 
**ipv6PeeringConfig** | [**ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfig**](ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfig.md) |  | [optional] 
**lastModifiedBy** | **String** | Gets whether the provider or the customer last modified the peering. | [optional] 
**microsoftPeeringConfig** | [**ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigMicrosoftPeeringConfig**](ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigMicrosoftPeeringConfig.md) |  | [optional] 
**peerASN** | **Number** | The peer ASN. | [optional] 
**peeringType** | **String** | The peering type. | [optional] 
**primaryAzurePort** | **String** | The primary port. | [optional] [readonly] 
**primaryPeerAddressPrefix** | **String** | The primary address prefix. | [optional] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] [readonly] 
**secondaryAzurePort** | **String** | The secondary port. | [optional] [readonly] 
**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. | [optional] 
**sharedKey** | **String** | The shared key. | [optional] 
**state** | **String** | The state of peering. | [optional] 
**vlanId** | **Number** | The VLAN ID. | [optional] 



## Enum: PeeringTypeEnum


* `AzurePublicPeering` (value: `"AzurePublicPeering"`)

* `AzurePrivatePeering` (value: `"AzurePrivatePeering"`)

* `MicrosoftPeering` (value: `"MicrosoftPeering"`)





## Enum: StateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




