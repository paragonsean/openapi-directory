# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationGatewayBackendAddressPools** | [**[Items]**](Items.md) | The reference of ApplicationGatewayBackendAddressPool resource. | [optional] 
**applicationSecurityGroups** | [**[Items]**](Items.md) | Application security groups in which the IP configuration is included. | [optional] 
**loadBalancerBackendAddressPools** | [**[Items]**](Items.md) | The reference of LoadBalancerBackendAddressPool resource. | [optional] 
**loadBalancerInboundNatRules** | [**[Items]**](Items.md) | A list of references of LoadBalancerInboundNatRules. | [optional] 
**primary** | **Boolean** | Gets whether this is a primary customer address on the network interface. | [optional] 
**privateIPAddress** | **String** | Private IP address of the IP configuration. | [optional] 
**privateIPAddressVersion** | [**PrivateIPAddressVersion**](PrivateIPAddressVersion.md) |  | [optional] 
**privateIPAllocationMethod** | [**PrivateIPAllocationMethod**](PrivateIPAllocationMethod.md) |  | [optional] 
**provisioningState** | **String** | The provisioning state of the network interface IP configuration. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 
**virtualNetworkTaps** | [**[Items]**](Items.md) | The reference to Virtual Network Taps. | [optional] 


