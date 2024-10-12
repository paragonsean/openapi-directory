

# VirtualNetworkGatewayConnectionPropertiesFormat

VirtualNetworkGatewayConnection properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationKey** | **String** | The authorizationKey. |  [optional] |
|**connectionProtocol** | **ConnectionProtocol** |  |  [optional] |
|**connectionStatus** | **VirtualNetworkGatewayConnectionStatus** |  |  [optional] |
|**connectionType** | **VirtualNetworkGatewayConnectionType** |  |  |
|**egressBytesTransferred** | **Long** | The egress bytes transferred in this connection. |  [optional] [readonly] |
|**enableBgp** | **Boolean** | EnableBgp flag. |  [optional] |
|**expressRouteGatewayBypass** | **Boolean** | Bypass ExpressRoute Gateway for data forwarding. |  [optional] |
|**ingressBytesTransferred** | **Long** | The ingress bytes transferred in this connection. |  [optional] [readonly] |
|**ipsecPolicies** | [**List&lt;IpsecPolicy&gt;**](IpsecPolicy.md) | The IPSec Policies to be considered by this connection. |  [optional] |
|**localNetworkGateway2** | [**LocalNetworkGateway**](LocalNetworkGateway.md) |  |  [optional] |
|**peer** | [**VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer**](VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning state of the VirtualNetworkGatewayConnection resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the VirtualNetworkGatewayConnection resource. |  [optional] |
|**routingWeight** | **Integer** | The routing weight. |  [optional] |
|**sharedKey** | **String** | The IPSec shared key. |  [optional] |
|**tunnelConnectionStatus** | [**List&lt;TunnelConnectionHealth&gt;**](TunnelConnectionHealth.md) | Collection of all tunnels&#39; connection health status. |  [optional] [readonly] |
|**usePolicyBasedTrafficSelectors** | **Boolean** | Enable policy-based traffic selectors. |  [optional] |
|**virtualNetworkGateway1** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md) |  |  |
|**virtualNetworkGateway2** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md) |  |  [optional] |



