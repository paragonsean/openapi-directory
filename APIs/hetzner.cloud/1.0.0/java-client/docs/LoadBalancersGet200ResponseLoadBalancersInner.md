

# LoadBalancersGet200ResponseLoadBalancersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm**](LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm.md) |  |  |
|**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) |  |
|**id** | **Integer** | ID of the Resource |  |
|**includedTraffic** | **Integer** | Free Traffic for the current billing period in bytes |  |
|**ingoingTraffic** | **Integer** | Inbound Traffic for the current billing period in bytes |  |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels (key-value pairs) |  |
|**loadBalancerType** | [**LoadBalancerTypesGet200ResponseLoadBalancerTypesInner**](LoadBalancerTypesGet200ResponseLoadBalancerTypesInner.md) |  |  |
|**location** | [**DatacentersGet200ResponseDatacentersInnerLocation**](DatacentersGet200ResponseDatacentersInnerLocation.md) |  |  |
|**name** | **String** | Name of the Resource. Must be unique per Project. |  |
|**outgoingTraffic** | **Integer** | Outbound Traffic for the current billing period in bytes |  |
|**privateNet** | [**List&lt;LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner&gt;**](LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner.md) | Private networks information |  |
|**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  |  |
|**publicNet** | [**LoadBalancersGet200ResponseLoadBalancersInnerPublicNet**](LoadBalancersGet200ResponseLoadBalancersInnerPublicNet.md) |  |  |
|**services** | [**List&lt;LoadBalancerService&gt;**](LoadBalancerService.md) | List of services that belong to this Load Balancer |  |
|**targets** | [**List&lt;LoadBalancerTarget&gt;**](LoadBalancerTarget.md) | List of targets that belong to this Load Balancer |  |



