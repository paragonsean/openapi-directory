# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPrefix** | **String** | The address prefix for the subnet. | [optional] 
**addressPrefixes** | **[String]** | List of address prefixes for the subnet. | [optional] 
**delegations** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesDelegationsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesDelegationsInner.md) | Gets an array of references to the delegations on the subnet. | [optional] 
**ipConfigurationProfiles** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationProfilesInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationProfilesInner.md) | Array of IP configuration profiles which reference this subnet. | [optional] [readonly] 
**ipConfigurations** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationsInner.md) | Gets an array of references to the network interface IP configurations using subnet. | [optional] [readonly] 
**natGateway** | [**Model0**](Model0.md) |  | [optional] 
**networkSecurityGroup** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroup**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroup.md) |  | [optional] 
**privateEndpointNetworkPolicies** | **String** | Enable or Disable private end point on the subnet. | [optional] 
**privateEndpoints** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInner.md) | An array of references to private endpoints. | [optional] [readonly] 
**privateLinkServiceNetworkPolicies** | **String** | Enable or Disable private link service on the subnet. | [optional] 
**provisioningState** | **String** | The provisioning state of the resource. | [optional] 
**purpose** | **String** | A read-only string identifying the intention of use for this subnet based on delegations and other user-defined properties. | [optional] [readonly] 
**resourceNavigationLinks** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesResourceNavigationLinksInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesResourceNavigationLinksInner.md) | Gets an array of references to the external resources using subnet. | [optional] 
**routeTable** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTable**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTable.md) |  | [optional] 
**serviceAssociationLinks** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceAssociationLinksInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceAssociationLinksInner.md) | Gets an array of references to services injecting into this subnet. | [optional] 
**serviceEndpointPolicies** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointPoliciesInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointPoliciesInner.md) | An array of service endpoint policies. | [optional] 
**serviceEndpoints** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointsInner.md) | An array of service endpoints. | [optional] 


