# NetworkManagementClient.VirtualNetworkGatewayConnectionListEntityPropertiesFormat

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
**localNetworkGateway2** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  | [optional] 
**peer** | [**VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer**](VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer.md) |  | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**resourceGuid** | **String** | The resource GUID property of the virtual network gateway connection resource. | [optional] 
**routingWeight** | **Number** | The routing weight. | [optional] 
**sharedKey** | **String** | The IPSec shared key. | [optional] 
**trafficSelectorPolicies** | [**[TrafficSelectorPolicy]**](TrafficSelectorPolicy.md) | The Traffic Selector Policies to be considered by this connection. | [optional] 
**tunnelConnectionStatus** | [**[TunnelConnectionHealth]**](TunnelConnectionHealth.md) | Collection of all tunnels&#39; connection health status. | [optional] [readonly] 
**usePolicyBasedTrafficSelectors** | **Boolean** | Enable policy-based traffic selectors. | [optional] 
**virtualNetworkGateway1** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  | 
**virtualNetworkGateway2** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




