

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerPropertiesDestinationLoadBalancerFrontEndIPConfigurationProperties

Properties of Frontend IP Configuration of the load balancer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inboundNatPools** | **List&lt;Model0&gt;** | Read only. Inbound pools URIs that use this frontend IP. |  [optional] [readonly] |
|**inboundNatRules** | **List&lt;Model0&gt;** | Read only. Inbound rules URIs that use this frontend IP. |  [optional] [readonly] |
|**loadBalancingRules** | **List&lt;Model0&gt;** | Gets load balancing rules URIs that use this frontend IP. |  [optional] [readonly] |
|**outboundRules** | **List&lt;Model0&gt;** | Read only. Outbound rules URIs that use this frontend IP. |  [optional] [readonly] |
|**privateIPAddress** | **String** | The private IP address of the IP configuration. |  [optional] |
|**privateIPAddressVersion** | **PrivateIPAddressVersion** |  |  [optional] |
|**privateIPAllocationMethod** | **PrivateIPAllocationMethod** |  |  [optional] |
|**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddress** | **PublicIPAddress** |  |  [optional] |
|**publicIPPrefix** | **Model0** |  |  [optional] |
|**subnet** | **Subnet** |  |  [optional] |



