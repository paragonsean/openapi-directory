# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendIPConfigurations** | [**[DestinationNetworkInterfaceIPConfiguration]**](DestinationNetworkInterfaceIPConfiguration.md) | Gets collection of references to IP addresses defined in network interfaces. | [optional] [readonly] 
**loadBalancingRules** | [**[Model0]**](Model0.md) | Gets load balancing rules that use this backend address pool. | [optional] [readonly] 
**outboundRule** | [**Model0**](Model0.md) |  | [optional] 
**outboundRules** | [**[Model0]**](Model0.md) | Gets outbound rules that use this backend address pool. | [optional] [readonly] 
**provisioningState** | **String** | Get provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 


