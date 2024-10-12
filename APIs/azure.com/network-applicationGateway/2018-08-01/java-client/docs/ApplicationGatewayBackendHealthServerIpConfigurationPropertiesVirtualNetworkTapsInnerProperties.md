

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerProperties

Virtual Network Tap properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationLoadBalancerFrontEndIPConfiguration** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerPropertiesDestinationLoadBalancerFrontEndIPConfiguration**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerPropertiesDestinationLoadBalancerFrontEndIPConfiguration.md) |  |  [optional] |
|**destinationNetworkInterfaceIPConfiguration** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInner**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInner.md) |  |  [optional] |
|**destinationPort** | **Integer** | The VXLAN destination port that will receive the tapped traffic. |  [optional] |
|**networkInterfaceTapConfigurations** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesTapConfigurationsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesTapConfigurationsInner.md) | Specifies the list of resource IDs for the network interface IP configuration that needs to be tapped. |  [optional] [readonly] |
|**provisioningState** | **String** | The provisioning state of the virtual network tap. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resourceGuid property of the virtual network tap. |  [optional] [readonly] |



