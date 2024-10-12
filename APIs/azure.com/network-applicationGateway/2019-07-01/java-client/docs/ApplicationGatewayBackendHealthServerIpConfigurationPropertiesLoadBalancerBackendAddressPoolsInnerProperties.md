

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesLoadBalancerBackendAddressPoolsInnerProperties

Properties of the backend address pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendIPConfigurations** | **List&lt;DestinationNetworkInterfaceIPConfiguration&gt;** | An array of references to IP addresses defined in network interfaces. |  [optional] [readonly] |
|**loadBalancingRules** | **List&lt;Model0&gt;** | An array of references to load balancing rules that use this backend address pool. |  [optional] [readonly] |
|**outboundRule** | **Model0** |  |  [optional] |
|**outboundRules** | **List&lt;Model0&gt;** | An array of references to outbound rules that use this backend address pool. |  [optional] [readonly] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |



