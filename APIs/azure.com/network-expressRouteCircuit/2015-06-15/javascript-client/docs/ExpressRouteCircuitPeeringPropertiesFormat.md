# NetworkManagementClient.ExpressRouteCircuitPeeringPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureASN** | **Number** | The Azure ASN. | [optional] 
**microsoftPeeringConfig** | [**ExpressRouteCircuitPeeringConfig**](ExpressRouteCircuitPeeringConfig.md) |  | [optional] 
**peerASN** | **Number** | The peer ASN. | [optional] 
**peeringType** | **String** | The PeeringType. Possible values are: &#39;AzurePublicPeering&#39;, &#39;AzurePrivatePeering&#39;, and &#39;MicrosoftPeering&#39;. | [optional] 
**primaryAzurePort** | **String** | The primary port. | [optional] 
**primaryPeerAddressPrefix** | **String** | The primary address prefix. | [optional] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**secondaryAzurePort** | **String** | The secondary port. | [optional] 
**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. | [optional] 
**sharedKey** | **String** | The shared key. | [optional] 
**state** | **String** | The state of peering. Possible values are: &#39;Disabled&#39; and &#39;Enabled&#39; | [optional] 
**stats** | [**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md) |  | [optional] 
**vlanId** | **Number** | The VLAN ID. | [optional] 



## Enum: PeeringTypeEnum


* `AzurePublicPeering` (value: `"AzurePublicPeering"`)

* `AzurePrivatePeering` (value: `"AzurePrivatePeering"`)

* `MicrosoftPeering` (value: `"MicrosoftPeering"`)





## Enum: StateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




