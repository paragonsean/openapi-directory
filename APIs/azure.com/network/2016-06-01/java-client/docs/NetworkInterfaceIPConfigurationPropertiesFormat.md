

# NetworkInterfaceIPConfigurationPropertiesFormat

Properties of IPConfiguration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationGatewayBackendAddressPools** | [**List&lt;ApplicationGatewayBackendAddressPool&gt;**](ApplicationGatewayBackendAddressPool.md) | Gets or sets the reference of ApplicationGatewayBackendAddressPool resource |  [optional] |
|**loadBalancerBackendAddressPools** | [**List&lt;BackendAddressPool&gt;**](BackendAddressPool.md) | Gets or sets the reference of LoadBalancerBackendAddressPool resource |  [optional] |
|**loadBalancerInboundNatRules** | [**List&lt;InboundNatRule&gt;**](InboundNatRule.md) | Gets or sets list of references of LoadBalancerInboundNatRules |  [optional] |
|**primary** | **Boolean** | Gets whether this is a primary customer address on the NIC |  [optional] |
|**privateIPAddress** | **String** |  |  [optional] |
|**privateIPAddressVersion** | [**PrivateIPAddressVersionEnum**](#PrivateIPAddressVersionEnum) | Gets or sets PrivateIP address version (IPv4/IPv6) |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | Gets or sets PrivateIP allocation method |  [optional] |
|**provisioningState** | **String** |  |  [optional] |
|**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  |  [optional] |
|**subnet** | [**Subnet**](Subnet.md) |  |  [optional] |



## Enum: PrivateIPAddressVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



