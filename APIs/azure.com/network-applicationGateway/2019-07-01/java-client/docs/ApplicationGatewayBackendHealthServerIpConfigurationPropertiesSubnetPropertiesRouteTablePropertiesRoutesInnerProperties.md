

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTablePropertiesRoutesInnerProperties

Route resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressPrefix** | **String** | The destination CIDR to which the route applies. |  [optional] |
|**nextHopIpAddress** | **String** | The IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is VirtualAppliance. |  [optional] |
|**nextHopType** | [**NextHopTypeEnum**](#NextHopTypeEnum) | The type of Azure hop the packet should be sent to. |  |
|**provisioningState** | **ProvisioningState** |  |  [optional] |



## Enum: NextHopTypeEnum

| Name | Value |
|---- | -----|
| VIRTUAL_NETWORK_GATEWAY | &quot;VirtualNetworkGateway&quot; |
| VNET_LOCAL | &quot;VnetLocal&quot; |
| INTERNET | &quot;Internet&quot; |
| VIRTUAL_APPLIANCE | &quot;VirtualAppliance&quot; |
| NONE | &quot;None&quot; |



