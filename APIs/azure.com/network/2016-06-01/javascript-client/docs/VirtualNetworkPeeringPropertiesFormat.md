# NetworkManagementClient.VirtualNetworkPeeringPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowForwardedTraffic** | **Boolean** | Gets or sets whether the forwarded traffic from the VMs in the remote virtual network will be allowed/disallowed | [optional] 
**allowGatewayTransit** | **Boolean** | Gets or sets if gatewayLinks can be used in remote virtual network’s link to this virtual network | [optional] 
**allowVirtualNetworkAccess** | **Boolean** | Gets or sets whether the VMs in the linked virtual network space would be able to access all the VMs in local Virtual network space | [optional] 
**peeringState** | **String** | Gets the status of the virtual network peering | [optional] 
**provisioningState** | **String** | Gets provisioning state of the resource | [optional] 
**remoteVirtualNetwork** | [**SubResource**](SubResource.md) |  | [optional] 
**useRemoteGateways** | **Boolean** | Gets or sets if remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only 1 peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway. | [optional] 



## Enum: PeeringStateEnum


* `Initiated` (value: `"Initiated"`)

* `Connected` (value: `"Connected"`)

* `Disconnected` (value: `"Disconnected"`)




