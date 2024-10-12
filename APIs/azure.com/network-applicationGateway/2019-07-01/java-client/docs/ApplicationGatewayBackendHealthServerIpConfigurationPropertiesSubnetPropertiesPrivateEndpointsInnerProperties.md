

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerProperties

Properties of the private endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**manualPrivateLinkServiceConnections** | **List&lt;Items&gt;** | A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource. |  [optional] |
|**networkInterfaces** | **List&lt;Items&gt;** | An array of references to the network interfaces created for this private endpoint. |  [optional] [readonly] |
|**privateLinkServiceConnections** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerPropertiesPrivateLinkServiceConnectionsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesPrivateEndpointsInnerPropertiesPrivateLinkServiceConnectionsInner.md) | A grouping of information about the connection to the remote resource. |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**subnet** | **Subnet** |  |  [optional] |



