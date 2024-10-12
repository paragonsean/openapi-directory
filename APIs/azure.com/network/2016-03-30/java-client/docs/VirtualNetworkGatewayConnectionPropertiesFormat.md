

# VirtualNetworkGatewayConnectionPropertiesFormat

VirtualNetworkGatewayConnection properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationKey** | **String** | The authorizationKey. |  [optional] |
|**connectionStatus** | [**ConnectionStatusEnum**](#ConnectionStatusEnum) | Virtual network Gateway connection status |  [optional] |
|**connectionType** | [**ConnectionTypeEnum**](#ConnectionTypeEnum) | Gateway connection type IPsec/Dedicated/VpnClient/Vnet2Vnet |  [optional] |
|**egressBytesTransferred** | **Long** | The Egress Bytes Transferred in this connection |  [optional] |
|**enableBgp** | **Boolean** | EnableBgp Flag |  [optional] |
|**ingressBytesTransferred** | **Long** | The Ingress Bytes Transferred in this connection |  [optional] |
|**localNetworkGateway2** | [**LocalNetworkGateway**](LocalNetworkGateway.md) |  |  [optional] |
|**peer** | [**SubResource**](SubResource.md) |  |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the VirtualNetworkGatewayConnection resource Updating/Deleting/Failed |  [optional] |
|**resourceGuid** | **String** | Gets or sets resource GUID property of the VirtualNetworkGatewayConnection resource |  [optional] |
|**routingWeight** | **Integer** | The Routing weight. |  [optional] |
|**sharedKey** | **String** | The IPsec share key. |  [optional] |
|**virtualNetworkGateway1** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md) |  |  [optional] |
|**virtualNetworkGateway2** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md) |  |  [optional] |



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



