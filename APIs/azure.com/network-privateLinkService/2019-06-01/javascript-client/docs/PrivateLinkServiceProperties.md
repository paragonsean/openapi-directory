# NetworkManagementClient.PrivateLinkServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **String** | The alias of the private link service. | [optional] [readonly] 
**autoApproval** | [**ResourceSet**](ResourceSet.md) | The auto-approval list of the private link service. | [optional] 
**fqdns** | **[String]** | The list of Fqdn. | [optional] 
**ipConfigurations** | [**[PrivateLinkServiceIpConfiguration]**](PrivateLinkServiceIpConfiguration.md) | An array of references to the private link service IP configuration. | [optional] 
**loadBalancerFrontendIpConfigurations** | [**[PrivateLinkServicePropertiesLoadBalancerFrontendIpConfigurationsInner]**](PrivateLinkServicePropertiesLoadBalancerFrontendIpConfigurationsInner.md) | An array of references to the load balancer IP configurations. | [optional] 
**networkInterfaces** | [**[PrivateLinkServicePropertiesNetworkInterfacesInner]**](PrivateLinkServicePropertiesNetworkInterfacesInner.md) | Gets an array of references to the network interfaces created for this private link service. | [optional] [readonly] 
**privateEndpointConnections** | [**[PrivateEndpointConnection]**](PrivateEndpointConnection.md) | An array of list about connections to the private endpoint. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**visibility** | [**ResourceSet**](ResourceSet.md) | The visibility list of the private link service. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




