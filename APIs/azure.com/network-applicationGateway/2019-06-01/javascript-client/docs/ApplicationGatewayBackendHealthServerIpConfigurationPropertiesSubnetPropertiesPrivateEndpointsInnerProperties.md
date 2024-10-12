# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manualPrivateLinkServiceConnections** | [**[Items]**](Items.md) | A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource. | [optional] 
**networkInterfaces** | [**[Items]**](Items.md) | Gets an array of references to the network interfaces created for this private endpoint. | [optional] [readonly] 
**privateLinkServiceConnections** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerPropertiesPrivateLinkServiceConnectionsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerPropertiesPrivateLinkServiceConnectionsInner.md) | A grouping of information about the connection to the remote resource. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




