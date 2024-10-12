# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTablePropertiesRoutesInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPrefix** | **String** | The destination CIDR to which the route applies. | [optional] 
**nextHopIpAddress** | **String** | The IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is VirtualAppliance. | [optional] 
**nextHopType** | **String** | The type of Azure hop the packet should be sent to. | 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 



## Enum: NextHopTypeEnum


* `VirtualNetworkGateway` (value: `"VirtualNetworkGateway"`)

* `VnetLocal` (value: `"VnetLocal"`)

* `Internet` (value: `"Internet"`)

* `VirtualAppliance` (value: `"VirtualAppliance"`)

* `None` (value: `"None"`)




