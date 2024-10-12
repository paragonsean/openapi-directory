# NetworkManagementClient.VirtualNetworkGatewayConnectionPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationKey** | **String** | The authorizationKey. | [optional] 
**connectionStatus** | **String** | Virtual network Gateway connection status | [optional] 
**connectionType** | **String** | Gateway connection type IPsec/Dedicated/VpnClient/Vnet2Vnet | [optional] 
**egressBytesTransferred** | **Number** | The Egress Bytes Transferred in this connection | [optional] 
**enableBgp** | **Boolean** | EnableBgp Flag | [optional] 
**ingressBytesTransferred** | **Number** | The Ingress Bytes Transferred in this connection | [optional] 
**localNetworkGateway2** | [**LocalNetworkGateway**](LocalNetworkGateway.md) |  | [optional] 
**peer** | [**SubResource**](SubResource.md) |  | [optional] 
**provisioningState** | **String** | Gets provisioning state of the VirtualNetworkGatewayConnection resource Updating/Deleting/Failed | [optional] 
**resourceGuid** | **String** | Gets or sets resource guid property of the VirtualNetworkGatewayConnection resource | [optional] 
**routingWeight** | **Number** | The Routing weight. | [optional] 
**sharedKey** | **String** | The IPsec share key. | [optional] 
**virtualNetworkGateway1** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md) |  | [optional] 
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




