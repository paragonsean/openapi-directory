

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
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the virtual network gateway resource. |  [optional] |
|**sku** | [**VirtualNetworkGatewaySku**](VirtualNetworkGatewaySku.md) |  |  [optional] |
|**vpnClientConfiguration** | [**VpnClientConfiguration**](VpnClientConfiguration.md) |  |  [optional] |
|**vpnGatewayGeneration** | [**VpnGatewayGenerationEnum**](#VpnGatewayGenerationEnum) | The generation for this VirtualNetworkGateway. Must be None if gatewayType is not VPN. |  [optional] |
|**vpnType** | [**VpnTypeEnum**](#VpnTypeEnum) | The type of this virtual network gateway. |  [optional] |



## Enum: GatewayTypeEnum

| Name | Value |
|---- | -----|
| VPN | &quot;Vpn&quot; |
| EXPRESS_ROUTE | &quot;ExpressRoute&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: VpnGatewayGenerationEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| GENERATION1 | &quot;Generation1&quot; |
| GENERATION2 | &quot;Generation2&quot; |



## Enum: VpnTypeEnum

| Name | Value |
|---- | -----|
| POLICY_BASED | &quot;PolicyBased&quot; |
| ROUTE_BASED | &quot;RouteBased&quot; |



