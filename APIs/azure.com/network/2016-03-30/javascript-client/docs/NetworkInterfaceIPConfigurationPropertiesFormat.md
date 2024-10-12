# NetworkManagementClient.NetworkInterfaceIPConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationGatewayBackendAddressPools** | [**[ApplicationGatewayBackendAddressPool]**](ApplicationGatewayBackendAddressPool.md) | Gets or sets the reference of ApplicationGatewayBackendAddressPool resource | [optional] 
**loadBalancerBackendAddressPools** | [**[BackendAddressPool]**](BackendAddressPool.md) | Gets or sets the reference of LoadBalancerBackendAddressPool resource | [optional] 
**loadBalancerInboundNatRules** | [**[InboundNatRule]**](InboundNatRule.md) | Gets or sets list of references of LoadBalancerInboundNatRules | [optional] 
**primary** | **Boolean** | Gets whether this is a primary customer address on the NIC | [optional] 
**privateIPAddress** | **String** |  | [optional] 
**privateIPAddressVersion** | **String** | Gets or sets PrivateIP address version (IPv4/IPv6) | [optional] 
**privateIPAllocationMethod** | **String** | Gets or sets PrivateIP allocation method (Static/Dynamic) | [optional] 
**provisioningState** | **String** |  | [optional] 
**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 



## Enum: PrivateIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)





## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




