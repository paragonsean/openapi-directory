

# PrivateLinkServiceProperties

Properties of the private link service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | The alias of the private link service. |  [optional] [readonly] |
|**autoApproval** | [**ResourceSet**](ResourceSet.md) | The auto-approval list of the private link service. |  [optional] |
|**fqdns** | **List&lt;String&gt;** | The list of Fqdn. |  [optional] |
|**ipConfigurations** | [**List&lt;PrivateLinkServiceIpConfiguration&gt;**](PrivateLinkServiceIpConfiguration.md) | An array of private link service IP configurations. |  [optional] |
|**loadBalancerFrontendIpConfigurations** | [**List&lt;PrivateLinkServicePropertiesLoadBalancerFrontendIpConfigurationsInner&gt;**](PrivateLinkServicePropertiesLoadBalancerFrontendIpConfigurationsInner.md) | An array of references to the load balancer IP configurations. |  [optional] |
|**networkInterfaces** | [**List&lt;PrivateLinkServicePropertiesNetworkInterfacesInner&gt;**](PrivateLinkServicePropertiesNetworkInterfacesInner.md) | An array of references to the network interfaces created for this private link service. |  [optional] [readonly] |
|**privateEndpointConnections** | [**List&lt;PrivateEndpointConnection&gt;**](PrivateEndpointConnection.md) | An array of list about connections to the private endpoint. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**visibility** | [**ResourceSet**](ResourceSet.md) | The visibility list of the private link service. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



