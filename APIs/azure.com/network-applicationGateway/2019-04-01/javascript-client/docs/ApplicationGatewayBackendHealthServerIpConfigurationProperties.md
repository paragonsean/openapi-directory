# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationGatewayBackendAddressPools** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationGatewayBackendAddressPoolsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationGatewayBackendAddressPoolsInner.md) | The reference of ApplicationGatewayBackendAddressPool resource. | [optional] 
**applicationSecurityGroups** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationSecurityGroupsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationSecurityGroupsInner.md) | Application security groups in which the IP configuration is included. | [optional] 
**loadBalancerBackendAddressPools** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInner.md) | The reference of LoadBalancerBackendAddressPool resource. | [optional] 
**loadBalancerInboundNatRules** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerInboundNatRulesInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerInboundNatRulesInner.md) | A list of references of LoadBalancerInboundNatRules. | [optional] 
**primary** | **Boolean** | Gets whether this is a primary customer address on the network interface. | [optional] 
**privateIPAddress** | **String** | Private IP address of the IP configuration. | [optional] 
**privateIPAddressVersion** | **String** | IP address version. | [optional] 
**privateIPAllocationMethod** | **String** | IP address allocation method. | [optional] 
**provisioningState** | **String** | The provisioning state of the network interface IP configuration. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**publicIPAddress** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddress**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddress.md) |  | [optional] 
**subnet** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnet**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnet.md) |  | [optional] 
**virtualNetworkTaps** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInner.md) | The reference to Virtual Network Taps. | [optional] 



## Enum: PrivateIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)





## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




