# NetworkManagementClient.ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsSettings** | [**ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesDnsSettings**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesDnsSettings.md) |  | [optional] 
**enableIPForwarding** | **Boolean** | Indicates whether IP forwarding is enabled on this network interface. | [optional] 
**ipConfigurations** | [**[ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesLoadBalancerBackendAddressPoolsInnerPropertiesBackendIPConfigurationsInner]**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesLoadBalancerBackendAddressPoolsInnerPropertiesBackendIPConfigurationsInner.md) | A list of IPConfigurations of the network interface. | [optional] 
**macAddress** | **String** | The MAC address of the network interface. | [optional] 
**networkSecurityGroup** | [**NetworkSecurityGroup**](NetworkSecurityGroup.md) |  | [optional] 
**primary** | **Boolean** | Gets whether this is a primary network interface on a virtual machine. | [optional] 
**provisioningState** | **String** | The provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**resourceGuid** | **String** | The resource GUID property of the network interface resource. | [optional] 
**virtualMachine** | [**Model0**](Model0.md) |  | [optional] 


