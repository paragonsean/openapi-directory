

# VirtualNetworkGatewayConnectionListEntityPropertiesFormat

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
|**localNetworkGateway2** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  |  [optional] |
|**peer** | [**VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer**](VirtualNetworkGatewayConnectionListEntityPropertiesFormatPeer.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the virtual network gateway connection resource. |  [optional] |
|**routingWeight** | **Integer** | The routing weight. |  [optional] |
|**sharedKey** | **String** | The IPSec shared key. |  [optional] |
|**trafficSelectorPolicies** | [**List&lt;TrafficSelectorPolicy&gt;**](TrafficSelectorPolicy.md) | The Traffic Selector Policies to be considered by this connection. |  [optional] |
|**tunnelConnectionStatus** | [**List&lt;TunnelConnectionHealth&gt;**](TunnelConnectionHealth.md) | Collection of all tunnels&#39; connection health status. |  [optional] [readonly] |
|**usePolicyBasedTrafficSelectors** | **Boolean** | Enable policy-based traffic selectors. |  [optional] |
|**virtualNetworkGateway1** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  |  |
|**virtualNetworkGateway2** | [**VirtualNetworkConnectionGatewayReference**](VirtualNetworkConnectionGatewayReference.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



