# NetworkManagementClient.VirtualNetworkGatewayPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeActive** | **Boolean** | ActiveActive flag. | [optional] 
**bgpSettings** | [**BgpSettings**](BgpSettings.md) |  | [optional] 
**customRoutes** | [**LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace**](LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace.md) |  | [optional] 
**enableBgp** | **Boolean** | Whether BGP is enabled for this virtual network gateway or not. | [optional] 
**gatewayDefaultSite** | [**VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer**](VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer.md) |  | [optional] 
**gatewayType** | **String** | The type of this virtual network gateway. | [optional] 
**ipConfigurations** | [**[VirtualNetworkGatewayIPConfiguration]**](VirtualNetworkGatewayIPConfiguration.md) | IP configurations for virtual network gateway. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**resourceGuid** | **String** | The resource GUID property of the virtual network gateway resource. | [optional] 
**sku** | [**VirtualNetworkGatewaySku**](VirtualNetworkGatewaySku.md) |  | [optional] 
**vpnClientConfiguration** | [**VpnClientConfiguration**](VpnClientConfiguration.md) |  | [optional] 
**vpnGatewayGeneration** | **String** | The generation for this VirtualNetworkGateway. Must be None if gatewayType is not VPN. | [optional] 
**vpnType** | **String** | The type of this virtual network gateway. | [optional] 



## Enum: GatewayTypeEnum


* `Vpn` (value: `"Vpn"`)

* `ExpressRoute` (value: `"ExpressRoute"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





## Enum: VpnGatewayGenerationEnum


* `None` (value: `"None"`)

* `Generation1` (value: `"Generation1"`)

* `Generation2` (value: `"Generation2"`)





## Enum: VpnTypeEnum


* `PolicyBased` (value: `"PolicyBased"`)

* `RouteBased` (value: `"RouteBased"`)




