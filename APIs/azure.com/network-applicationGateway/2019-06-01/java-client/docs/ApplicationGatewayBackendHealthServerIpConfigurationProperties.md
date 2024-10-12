

# ApplicationGatewayBackendHealthServerIpConfigurationProperties

Properties of IP configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationGatewayBackendAddressPools** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationGatewayBackendAddressPoolsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationGatewayBackendAddressPoolsInner.md) | The reference of ApplicationGatewayBackendAddressPool resource. |  [optional] |
|**applicationSecurityGroups** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationSecurityGroupsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesApplicationSecurityGroupsInner.md) | Application security groups in which the IP configuration is included. |  [optional] |
|**loadBalancerBackendAddressPools** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInner.md) | The reference of LoadBalancerBackendAddressPool resource. |  [optional] |
|**loadBalancerInboundNatRules** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerInboundNatRulesInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerInboundNatRulesInner.md) | A list of references of LoadBalancerInboundNatRules. |  [optional] |
|**primary** | **Boolean** | Gets whether this is a primary customer address on the network interface. |  [optional] |
|**privateIPAddress** | **String** | Private IP address of the IP configuration. |  [optional] |
|**privateIPAddressVersion** | [**PrivateIPAddressVersionEnum**](#PrivateIPAddressVersionEnum) | IP address version. |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | IP address allocation method. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the network interface IP configuration. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddress** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddress**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddress.md) |  |  [optional] |
|**subnet** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnet**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnet.md) |  |  [optional] |
|**virtualNetworkTaps** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInner.md) | The reference to Virtual Network Taps. |  [optional] |



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



