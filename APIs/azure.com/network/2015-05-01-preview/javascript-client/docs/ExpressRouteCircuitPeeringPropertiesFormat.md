# NetworkResourceProviderClient.ExpressRouteCircuitPeeringPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureASN** | **Number** | Gets or sets the azure ASN | [optional] 
**microsoftPeeringConfig** | [**ExpressRouteCircuitPeeringConfig**](ExpressRouteCircuitPeeringConfig.md) |  | [optional] 
**peerASN** | **Number** | Gets or sets the peer ASN | [optional] 
**peeringType** | **String** | Gets or sets PeeringType | [optional] 
**primaryAzurePort** | **String** | Gets or sets the primary port | [optional] 
**primaryPeerAddressPrefix** | **String** | Gets or sets the primary address prefix | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**secondaryAzurePort** | **String** | Gets or sets the secondary port | [optional] 
**secondaryPeerAddressPrefix** | **String** | Gets or sets the secondary address prefix | [optional] 
**sharedKey** | **String** | Gets or sets the shared key | [optional] 
**state** | **String** | Gets or sets state of Peering | [optional] 
**stats** | [**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md) |  | [optional] 
**vlanId** | **Number** | Gets or sets the vlan id | [optional] 



## Enum: PeeringTypeEnum


* `AzurePublicPeering` (value: `"AzurePublicPeering"`)

* `AzurePrivatePeering` (value: `"AzurePrivatePeering"`)

* `MicrosoftPeering` (value: `"MicrosoftPeering"`)





## Enum: StateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




