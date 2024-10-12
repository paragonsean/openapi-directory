

# VirtualNetworkGatewayConnectionListEntityPropertiesFormat

VirtualNetworkGatewayConnection properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationKey** | **String** | The authorizationKey. |  [optional] |
|**connectionStatus** | [**ConnectionStatusEnum**](#ConnectionStatusEnum) | Virtual network Gateway connection status. Possible values are &#39;Unknown&#39;, &#39;Connecting&#39;, &#39;Connected&#39; and &#39;NotConnected&#39;. |  [optional] [readonly] |
|**connectionType** | [**ConnectionTypeEnum**](#ConnectionTypeEnum) | Gateway connection type. Possible values are: &#39;IPsec&#39;,&#39;Vnet2Vnet&#39;,&#39;ExpressRoute&#39;, and &#39;VPNClient. |  |
|**egressBytesTransferred** | **Long** | The egress bytes transferred in this connection. |  [optional] [readonly] |
|**enableBgp** | **Boolean** | EnableBgp flag |  [optional] |
|**ingressBytesTransferred** | **Long** | The ingress bytes transferred in this connection. |  [optional] [readonly] |
|**ipsecPolicies** | [**List&lt;IpsecPolicy&gt;**](IpsecPolicy.md) | The IPSec Policies to be considered by this connection. |  [optional] |
|**localNetworkGateway2** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  |  [optional] |
|**peer** | [**VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer**](VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning state of the VirtualNetworkGatewayConnection resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the VirtualNetworkGatewayConnection resource. |  [optional] |
|**routingWeight** | **Integer** | The routing weight. |  [optional] |
|**sharedKey** | **String** | The IPSec shared key. |  [optional] |
|**tunnelConnectionStatus** | [**List&lt;TunnelConnectionHealth&gt;**](TunnelConnectionHealth.md) | Collection of all tunnels&#39; connection health status. |  [optional] [readonly] |
|**usePolicyBasedTrafficSelectors** | **Boolean** | Enable policy-based traffic selectors. |  [optional] |
|**virtualNetworkGateway1** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  |  |
|**virtualNetworkGateway2** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  |  [optional] |



## Enum: ConnectionStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CONNECTING | &quot;Connecting&quot; |
| CONNECTED | &quot;Connected&quot; |
| NOT_CONNECTED | &quot;NotConnected&quot; |



## Enum: ConnectionTypeEnum

| Name | Value |
|---- | -----|
| I_PSEC | &quot;IPsec&quot; |
| VNET2_VNET | &quot;Vnet2Vnet&quot; |
| EXPRESS_ROUTE | &quot;ExpressRoute&quot; |
| VPN_CLIENT | &quot;VPNClient&quot; |



