# NetworkManagementClient.VirtualNetworkGatewayConnectionPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationKey** | **String** | The authorizationKey. | [optional] 
**connectionProtocol** | [**ConnectionProtocol**](ConnectionProtocol.md) |  | [optional] 
**connectionStatus** | [**VirtualNetworkGatewayConnectionStatus**](VirtualNetworkGatewayConnectionStatus.md) |  | [optional] 
**connectionType** | [**VirtualNetworkGatewayConnectionType**](VirtualNetworkGatewayConnectionType.md) |  | 
**egressBytesTransferred** | **Number** | The egress bytes transferred in this connection. | [optional] [readonly] 
**enableBgp** | **Boolean** | EnableBgp flag. | [optional] 
**expressRouteGatewayBypass** | **Boolean** | Bypass ExpressRoute Gateway for data forwarding. | [optional] 
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


