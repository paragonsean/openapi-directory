

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInnerProperties

Properties of the backend address pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendIPConfigurations** | **List&lt;Items&gt;** | Gets collection of references to IP addresses defined in network interfaces. |  [optional] [readonly] |
|**loadBalancingRules** | **List&lt;Model0&gt;** | Gets load balancing rules that use this backend address pool. |  [optional] [readonly] |
|**outboundNatRule** | **Model0** |  |  [optional] |
|**provisioningState** | **String** | Get provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |



