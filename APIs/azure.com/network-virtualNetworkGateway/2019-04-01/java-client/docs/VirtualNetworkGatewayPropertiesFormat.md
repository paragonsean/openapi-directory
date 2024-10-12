

# VirtualNetworkGatewayPropertiesFormat

VirtualNetworkGateway properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeActive** | **Boolean** | ActiveActive flag. |  [optional] |
|**bgpSettings** | [**BgpSettings**](BgpSettings.md) |  |  [optional] |
|**customRoutes** | [**LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace**](LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace.md) |  |  [optional] |
|**enableBgp** | **Boolean** | Whether BGP is enabled for this virtual network gateway or not. |  [optional] |
|**gatewayDefaultSite** | [**VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer**](VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer.md) |  |  [optional] |
|**gatewayType** | [**GatewayTypeEnum**](#GatewayTypeEnum) | The type of this virtual network gateway. |  [optional] |
|**ipConfigurations** | [**List&lt;VirtualNetworkGatewayIPConfiguration&gt;**](VirtualNetworkGatewayIPConfiguration.md) | IP configurations for virtual network gateway. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the VirtualNetworkGateway resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the VirtualNetworkGateway resource. |  [optional] |
|**sku** | [**VirtualNetworkGatewaySku**](VirtualNetworkGatewaySku.md) |  |  [optional] |
|**vpnClientConfiguration** | [**VpnClientConfiguration**](VpnClientConfiguration.md) |  |  [optional] |
|**vpnType** | [**VpnTypeEnum**](#VpnTypeEnum) | The type of this virtual network gateway. |  [optional] |



## Enum: GatewayTypeEnum

| Name | Value |
|---- | -----|
| VPN | &quot;Vpn&quot; |
| EXPRESS_ROUTE | &quot;ExpressRoute&quot; |



## Enum: VpnTypeEnum

| Name | Value |
|---- | -----|
| POLICY_BASED | &quot;PolicyBased&quot; |
| ROUTE_BASED | &quot;RouteBased&quot; |



