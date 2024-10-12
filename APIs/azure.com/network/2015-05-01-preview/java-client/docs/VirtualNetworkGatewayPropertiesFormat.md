

# VirtualNetworkGatewayPropertiesFormat

VirtualNetworkGateway properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableBgp** | **Boolean** | EnableBgp Flag |  [optional] |
|**gatewayDefaultSite** | [**SubResource**](SubResource.md) |  |  [optional] |
|**gatewayType** | [**GatewayTypeEnum**](#GatewayTypeEnum) | The type of this virtual network gateway. |  [optional] |
|**ipConfigurations** | [**List&lt;VirtualNetworkGatewayIpConfiguration&gt;**](VirtualNetworkGatewayIpConfiguration.md) | IpConfigurations for Virtual network gateway. |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the VirtualNetworkGateway resource Updating/Deleting/Failed |  [optional] |
|**resourceGuid** | **String** | Gets or sets resource guid property of the VirtualNetworkGateway resource |  [optional] |
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



