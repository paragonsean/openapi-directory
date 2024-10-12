

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetProperties

Properties of the subnet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressPrefix** | **String** | The address prefix for the subnet. |  [optional] |
|**addressPrefixes** | **List&lt;String&gt;** | List of  address prefixes for the subnet. |  [optional] |
|**delegations** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesDelegationsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesDelegationsInner.md) | Gets an array of references to the delegations on the subnet. |  [optional] |
|**interfaceEndpoints** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesInterfaceEndpointsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesInterfaceEndpointsInner.md) | An array of references to interface endpoints  |  [optional] [readonly] |
|**ipConfigurationProfiles** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationProfilesInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationProfilesInner.md) | Array of IP configuration profiles which reference this subnet. |  [optional] [readonly] |
|**ipConfigurations** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationsInner.md) | Gets an array of references to the network interface IP configurations using subnet. |  [optional] [readonly] |
|**natGateway** | **Model0** |  |  [optional] |
|**networkSecurityGroup** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroup**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroup.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning state of the resource. |  [optional] |
|**purpose** | **String** | A read-only string identifying the intention of use for this subnet based on delegations and other user-defined properties. |  [optional] [readonly] |
|**resourceNavigationLinks** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesResourceNavigationLinksInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesResourceNavigationLinksInner.md) | Gets an array of references to the external resources using subnet. |  [optional] |
|**routeTable** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTable**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTable.md) |  |  [optional] |
|**serviceAssociationLinks** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceAssociationLinksInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceAssociationLinksInner.md) | Gets an array of references to services injecting into this subnet. |  [optional] |
|**serviceEndpointPolicies** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointPoliciesInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointPoliciesInner.md) | An array of service endpoint policies. |  [optional] |
|**serviceEndpoints** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointsInner.md) | An array of service endpoints. |  [optional] |



