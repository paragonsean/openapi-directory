# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesInterfaceEndpointsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpointService** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesInterfaceEndpointsInnerPropertiesEndpointService**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesInterfaceEndpointsInnerPropertiesEndpointService.md) |  | [optional] 
**fqdn** | **String** | A first-party service&#39;s FQDN that is mapped to the private IP allocated via this interface endpoint. | [optional] 
**networkInterfaces** | [**[Items]**](Items.md) | Gets an array of references to the network interfaces created for this interface endpoint. | [optional] [readonly] 
**owner** | **String** | A read-only property that identifies who created this interface endpoint. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the interface endpoint. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] [readonly] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 


