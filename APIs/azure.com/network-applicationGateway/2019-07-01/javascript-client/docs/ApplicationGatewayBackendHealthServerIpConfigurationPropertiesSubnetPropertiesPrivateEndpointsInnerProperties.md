# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manualPrivateLinkServiceConnections** | [**[Items]**](Items.md) | A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource. | [optional] 
**networkInterfaces** | [**[Items]**](Items.md) | An array of references to the network interfaces created for this private endpoint. | [optional] [readonly] 
**privateLinkServiceConnections** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerPropertiesPrivateLinkServiceConnectionsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerPropertiesPrivateLinkServiceConnectionsInner.md) | A grouping of information about the connection to the remote resource. | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 


