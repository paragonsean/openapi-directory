

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerPropertiesDestinationLoadBalancerFrontEndIPConfigurationProperties

Properties of Frontend IP Configuration of the load balancer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inboundNatPools** | **List&lt;Model0&gt;** | An array of references to inbound pools that use this frontend IP. |  [optional] [readonly] |
|**inboundNatRules** | **List&lt;Model0&gt;** | An array of references to inbound rules that use this frontend IP. |  [optional] [readonly] |
|**loadBalancingRules** | **List&lt;Model0&gt;** | An array of references to load balancing rules that use this frontend IP. |  [optional] [readonly] |
|**outboundRules** | **List&lt;Model0&gt;** | An array of references to outbound rules that use this frontend IP. |  [optional] [readonly] |
|**privateIPAddress** | **String** | The private IP address of the IP configuration. |  [optional] |
|**privateIPAddressVersion** | **PrivateIPAddressVersion** |  |  [optional] |
|**privateIPAllocationMethod** | **PrivateIPAllocationMethod** |  |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**publicIPAddress** | **PublicIPAddress** |  |  [optional] |
|**publicIPPrefix** | **Model0** |  |  [optional] |
|**subnet** | **Subnet** |  |  [optional] |



