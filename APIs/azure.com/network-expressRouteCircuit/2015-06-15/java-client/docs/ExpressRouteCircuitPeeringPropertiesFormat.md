

# ExpressRouteCircuitPeeringPropertiesFormat


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureASN** | **Integer** | The Azure ASN. |  [optional] |
|**microsoftPeeringConfig** | [**ExpressRouteCircuitPeeringConfig**](ExpressRouteCircuitPeeringConfig.md) |  |  [optional] |
|**peerASN** | **Integer** | The peer ASN. |  [optional] |
|**peeringType** | [**PeeringTypeEnum**](#PeeringTypeEnum) | The PeeringType. Possible values are: &#39;AzurePublicPeering&#39;, &#39;AzurePrivatePeering&#39;, and &#39;MicrosoftPeering&#39;. |  [optional] |
|**primaryAzurePort** | **String** | The primary port. |  [optional] |
|**primaryPeerAddressPrefix** | **String** | The primary address prefix. |  [optional] |
|**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**secondaryAzurePort** | **String** | The secondary port. |  [optional] |
|**secondaryPeerAddressPrefix** | **String** | The secondary address prefix. |  [optional] |
|**sharedKey** | **String** | The shared key. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of peering. Possible values are: &#39;Disabled&#39; and &#39;Enabled&#39; |  [optional] |
|**stats** | [**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md) |  |  [optional] |
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



