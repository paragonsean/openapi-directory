# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationGatewayBackendAddressPools** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationGatewayBackendAddressPoolsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationGatewayBackendAddressPoolsInner.md) | The reference of ApplicationGatewayBackendAddressPool resource. | [optional] 
**applicationSecurityGroups** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationSecurityGroupsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationSecurityGroupsInner.md) | Application security groups in which the IP configuration is included. | [optional] 
**loadBalancerBackendAddressPools** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInner.md) | The reference of LoadBalancerBackendAddressPool resource. | [optional] 
**loadBalancerInboundNatRules** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerInboundNatRulesInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerInboundNatRulesInner.md) | A list of references of LoadBalancerInboundNatRules. | [optional] 
**primary** | **Boolean** | Whether this is a primary customer address on the network interface. | [optional] 
**privateIPAddress** | **String** | Private IP address of the IP configuration. | [optional] 
**privateIPAddressVersion** | **String** | IP address version. | [optional] 
**privateIPAllocationMethod** | **String** | IP address allocation method. | [optional] 
**privateLinkConnectionProperties** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPrivateLinkConnectionProperties**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPrivateLinkConnectionProperties.md) |  | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**publicIPAddress** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddress**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddress.md) |  | [optional] 
**subnet** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnet**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnet.md) |  | [optional] 
**virtualNetworkTaps** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInner.md) | The reference to Virtual Network Taps. | [optional] 



## Enum: PrivateIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)





## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




