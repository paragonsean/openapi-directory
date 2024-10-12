# NetworkManagementClient.VirtualNetworkGatewayConnectionPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationKey** | **String** | The authorizationKey. | [optional] 
**connectionStatus** | **String** | Virtual network Gateway connection status. Possible values are &#39;Unknown&#39;, &#39;Connecting&#39;, &#39;Connected&#39; and &#39;NotConnected&#39;. | [optional] [readonly] 
**connectionType** | **String** | Gateway connection type. Possible values are: &#39;IPsec&#39;,&#39;Vnet2Vnet&#39;,&#39;ExpressRoute&#39;, and &#39;VPNClient. | 
**egressBytesTransferred** | **Number** | The egress bytes transferred in this connection. | [optional] [readonly] 
**enableBgp** | **Boolean** | EnableBgp flag | [optional] 
**ingressBytesTransferred** | **Number** | The ingress bytes transferred in this connection. | [optional] [readonly] 
**ipsecPolicies** | [**[IpsecPolicy]**](IpsecPolicy.md) | The IPSec Policies to be considered by this connection. | [optional] 
**localNetworkGateway2** | [**LocalNetworkGateway**](LocalNetworkGateway.md) |  | [optional] 
**peer** | [**VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer**](VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer.md) |  | [optional] 
**provisioningState** | **String** | The provisioning state of the VirtualNetworkGatewayConnection resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] [readonly] 
**resourceGuid** | **String** | The resource GUID property of the VirtualNetworkGatewayConnection resource. | [optional] 
**routingWeight** | **Number** | The routing weight. | [optional] 
**sharedKey** | **String** | The IPSec shared key. | [optional] 
**tunnelConnectionStatus** | [**[TunnelConnectionHealth]**](TunnelConnectionHealth.md) | Collection of all tunnels&#39; connection health status. | [optional] [readonly] 
**usePolicyBasedTrafficSelectors** | **Boolean** | Enable policy-based traffic selectors. | [optional] 
**virtualNetworkGateway1** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md) |  | 
**virtualNetworkGateway2** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md) |  | [optional] 



## Enum: ConnectionStatusEnum


* `Unknown` (value: `"Unknown"`)

* `Connecting` (value: `"Connecting"`)

* `Connected` (value: `"Connected"`)

* `NotConnected` (value: `"NotConnected"`)





## Enum: ConnectionTypeEnum


* `IPsec` (value: `"IPsec"`)

* `Vnet2Vnet` (value: `"Vnet2Vnet"`)

* `ExpressRoute` (value: `"ExpressRoute"`)

* `VPNClient` (value: `"VPNClient"`)




