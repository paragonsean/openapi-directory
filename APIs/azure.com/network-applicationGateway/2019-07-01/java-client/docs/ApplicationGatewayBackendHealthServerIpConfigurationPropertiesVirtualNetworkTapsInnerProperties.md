

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerProperties

Virtual Network Tap properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationLoadBalancerFrontEndIPConfiguration** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerPropertiesDestinationLoadBalancerFrontEndIPConfiguration**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerPropertiesDestinationLoadBalancerFrontEndIPConfiguration.md) |  |  [optional] |
|**destinationNetworkInterfaceIPConfiguration** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInner**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInner.md) |  |  [optional] |
|**destinationPort** | **Integer** | The VXLAN destination port that will receive the tapped traffic. |  [optional] |
|**networkInterfaceTapConfigurations** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesTapConfigurationsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesTapConfigurationsInner.md) | Specifies the list of resource IDs for the network interface IP configuration that needs to be tapped. |  [optional] [readonly] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**resourceGuid** | **String** | The resource GUID property of the virtual network tap resource. |  [optional] [readonly] |



