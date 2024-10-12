

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInnerProperties

Properties of IP configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationGatewayBackendAddressPools** | **List&lt;Items&gt;** | The reference of ApplicationGatewayBackendAddressPool resource. |  [optional] |
|**applicationSecurityGroups** | **List&lt;Items&gt;** | Application security groups in which the IP configuration is included. |  [optional] |
|**loadBalancerBackendAddressPools** | **List&lt;Items&gt;** | The reference of LoadBalancerBackendAddressPool resource. |  [optional] |
|**loadBalancerInboundNatRules** | **List&lt;Items&gt;** | A list of references of LoadBalancerInboundNatRules. |  [optional] |
|**primary** | **Boolean** | Gets whether this is a primary customer address on the network interface. |  [optional] |
|**privateIPAddress** | **String** | Private IP address of the IP configuration. |  [optional] |
|**privateIPAddressVersion** | **PrivateIPAddressVersion** |  |  [optional] |
|**privateIPAllocationMethod** | **PrivateIPAllocationMethod** |  |  [optional] |
|**provisioningState** | **String** | The provisioning state of the network interface IP configuration. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddress** | **PublicIPAddress** |  |  [optional] |
|**subnet** | **Subnet** |  |  [optional] |
|**virtualNetworkTaps** | **List&lt;Items&gt;** | The reference to Virtual Network Taps. |  [optional] |



