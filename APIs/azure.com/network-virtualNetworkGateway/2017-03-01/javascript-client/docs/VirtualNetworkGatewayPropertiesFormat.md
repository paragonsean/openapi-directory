# NetworkManagementClient.VirtualNetworkGatewayPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeActive** | **Boolean** | ActiveActive flag | [optional] 
**bgpSettings** | [**BgpSettings**](BgpSettings.md) |  | [optional] 
**enableBgp** | **Boolean** | Whether BGP is enabled for this virtual network gateway or not. | [optional] 
**gatewayDefaultSite** | [**VirtualNetworkGatewayConnectionPropertiesFormatPeer**](VirtualNetworkGatewayConnectionPropertiesFormatPeer.md) |  | [optional] 
**gatewayType** | **String** | The type of this virtual network gateway. Possible values are: &#39;Vpn&#39; and &#39;ExpressRoute&#39;. | [optional] 
**ipConfigurations** | [**[VirtualNetworkGatewayIPConfiguration]**](VirtualNetworkGatewayIPConfiguration.md) | IP configurations for virtual network gateway. | [optional] 
**provisioningState** | **String** | The provisioning state of the VirtualNetworkGateway resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] [readonly] 
**resourceGuid** | **String** | The resource GUID property of the VirtualNetworkGateway resource. | [optional] 
**sku** | [**VirtualNetworkGatewaySku**](VirtualNetworkGatewaySku.md) |  | [optional] 
**vpnClientConfiguration** | [**VpnClientConfiguration**](VpnClientConfiguration.md) |  | [optional] 
**vpnType** | **String** | The type of this virtual network gateway. Possible values are: &#39;PolicyBased&#39; and &#39;RouteBased&#39;. | [optional] 



## Enum: GatewayTypeEnum


* `Vpn` (value: `"Vpn"`)

* `ExpressRoute` (value: `"ExpressRoute"`)





## Enum: VpnTypeEnum


* `PolicyBased` (value: `"PolicyBased"`)

* `RouteBased` (value: `"RouteBased"`)




