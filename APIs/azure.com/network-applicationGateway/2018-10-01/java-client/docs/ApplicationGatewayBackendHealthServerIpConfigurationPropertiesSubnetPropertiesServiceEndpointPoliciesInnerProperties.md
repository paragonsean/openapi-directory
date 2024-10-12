

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointPoliciesInnerProperties

Service Endpoint Policy resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | The provisioning state of the service endpoint policy. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the service endpoint policy resource. |  [optional] [readonly] |
|**serviceEndpointPolicyDefinitions** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointPoliciesInnerPropertiesServiceEndpointPolicyDefinitionsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesServiceEndpointPoliciesInnerPropertiesServiceEndpointPolicyDefinitionsInner.md) | A collection of service endpoint policy definitions of the service endpoint policy. |  [optional] |
|**subnets** | **List&lt;Subnet&gt;** | A collection of references to subnets. |  [optional] [readonly] |



