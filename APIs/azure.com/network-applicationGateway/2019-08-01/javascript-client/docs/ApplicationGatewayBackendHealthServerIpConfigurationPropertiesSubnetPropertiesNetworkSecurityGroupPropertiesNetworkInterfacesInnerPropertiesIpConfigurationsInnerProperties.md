# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationGatewayBackendAddressPools** | [**[Items]**](Items.md) | The reference of ApplicationGatewayBackendAddressPool resource. | [optional] 
**applicationSecurityGroups** | [**[Items]**](Items.md) | Application security groups in which the IP configuration is included. | [optional] 
**loadBalancerBackendAddressPools** | [**[Items]**](Items.md) | The reference of LoadBalancerBackendAddressPool resource. | [optional] 
**loadBalancerInboundNatRules** | [**[Items]**](Items.md) | A list of references of LoadBalancerInboundNatRules. | [optional] 
**primary** | **Boolean** | Whether this is a primary customer address on the network interface. | [optional] 
**privateIPAddress** | **String** | Private IP address of the IP configuration. | [optional] 
**privateIPAddressVersion** | [**PrivateIPAddressVersion**](PrivateIPAddressVersion.md) |  | [optional] 
**privateIPAllocationMethod** | [**PrivateIPAllocationMethod**](PrivateIPAllocationMethod.md) |  | [optional] 
**privateLinkConnectionProperties** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPrivateLinkConnectionProperties**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPrivateLinkConnectionProperties.md) |  | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 
**virtualNetworkTaps** | [**[Items]**](Items.md) | The reference to Virtual Network Taps. | [optional] 


