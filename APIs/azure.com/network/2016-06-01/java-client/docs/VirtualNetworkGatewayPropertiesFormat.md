

# VirtualNetworkGatewayPropertiesFormat

VirtualNetworkGateway properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeActive** | **Boolean** | ActiveActive flag |  [optional] |
|**bgpSettings** | [**BgpSettings**](BgpSettings.md) |  |  [optional] |
|**enableBgp** | **Boolean** | EnableBgp Flag |  [optional] |
|**gatewayDefaultSite** | [**SubResource**](SubResource.md) |  |  [optional] |
|**gatewayType** | [**GatewayTypeEnum**](#GatewayTypeEnum) | The type of this virtual network gateway. |  [optional] |
|**ipConfigurations** | [**List&lt;VirtualNetworkGatewayIPConfiguration&gt;**](VirtualNetworkGatewayIPConfiguration.md) | IpConfigurations for Virtual network gateway. |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the VirtualNetworkGateway resource Updating/Deleting/Failed |  [optional] |
|**resourceGuid** | **String** | Gets or sets resource guid property of the VirtualNetworkGateway resource |  [optional] |
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



