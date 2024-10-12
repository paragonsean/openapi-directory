# NetworkManagementClient.VirtualNetworkGatewayPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgpSettings** | [**BgpSettings**](BgpSettings.md) |  | [optional] 
**enableBgp** | **Boolean** | EnableBgp Flag | [optional] 
**gatewayDefaultSite** | [**SubResource**](SubResource.md) |  | [optional] 
**gatewayType** | **String** | The type of this virtual network gateway. | [optional] 
**ipConfigurations** | [**[VirtualNetworkGatewayIPConfiguration]**](VirtualNetworkGatewayIPConfiguration.md) | IpConfigurations for Virtual network gateway. | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the VirtualNetworkGateway resource Updating/Deleting/Failed | [optional] 
**resourceGuid** | **String** | Gets or sets resource GUID property of the VirtualNetworkGateway resource | [optional] 
**sku** | [**VirtualNetworkGatewaySku**](VirtualNetworkGatewaySku.md) |  | [optional] 
**vpnClientConfiguration** | [**VpnClientConfiguration**](VpnClientConfiguration.md) |  | [optional] 
**vpnType** | **String** | The type of this virtual network gateway. | [optional] 



## Enum: GatewayTypeEnum


* `Vpn` (value: `"Vpn"`)

* `ExpressRoute` (value: `"ExpressRoute"`)





## Enum: VpnTypeEnum


* `PolicyBased` (value: `"PolicyBased"`)

* `RouteBased` (value: `"RouteBased"`)




