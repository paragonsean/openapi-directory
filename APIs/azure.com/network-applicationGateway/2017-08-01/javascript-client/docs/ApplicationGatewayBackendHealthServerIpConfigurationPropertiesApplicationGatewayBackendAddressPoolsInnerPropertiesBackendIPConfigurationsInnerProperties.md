# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationGatewayBackendAddressPoolsInnerPropertiesBackendIPConfigurationsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationGatewayBackendAddressPools** | [**[Items]**](Items.md) | The reference of ApplicationGatewayBackendAddressPool resource. | [optional] 
**loadBalancerBackendAddressPools** | [**[Items]**](Items.md) | The reference of LoadBalancerBackendAddressPool resource. | [optional] 
**loadBalancerInboundNatRules** | [**[Items]**](Items.md) | A list of references of LoadBalancerInboundNatRules. | [optional] 
**primary** | **Boolean** | Gets whether this is a primary customer address on the network interface. | [optional] 
**privateIPAddress** | **String** | Private IP address of the IP configuration. | [optional] 
**privateIPAddressVersion** | **String** | Available from Api-Version 2016-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4.  Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. | [optional] 
**privateIPAllocationMethod** | **String** | Defines how a private IP address is assigned. Possible values are: &#39;Static&#39; and &#39;Dynamic&#39;. | [optional] 
**provisioningState** | **String** | The provisioning state of the network interface IP configuration. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 



## Enum: PrivateIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)





## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




