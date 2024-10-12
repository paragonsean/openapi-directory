# HetznerCloudApi.LoadBalancersGet200ResponseLoadBalancersInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm**](LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm.md) |  | 
**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) | 
**id** | **Number** | ID of the Resource | 
**includedTraffic** | **Number** | Free Traffic for the current billing period in bytes | 
**ingoingTraffic** | **Number** | Inbound Traffic for the current billing period in bytes | 
**labels** | **{String: String}** | User-defined labels (key-value pairs) | 
**loadBalancerType** | [**LoadBalancerTypesGet200ResponseLoadBalancerTypesInner**](LoadBalancerTypesGet200ResponseLoadBalancerTypesInner.md) |  | 
**location** | [**DatacentersGet200ResponseDatacentersInnerLocation**](DatacentersGet200ResponseDatacentersInnerLocation.md) |  | 
**name** | **String** | Name of the Resource. Must be unique per Project. | 
**outgoingTraffic** | **Number** | Outbound Traffic for the current billing period in bytes | 
**privateNet** | [**[LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner]**](LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner.md) | Private networks information | 
**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  | 
**publicNet** | [**LoadBalancersGet200ResponseLoadBalancersInnerPublicNet**](LoadBalancersGet200ResponseLoadBalancersInnerPublicNet.md) |  | 
**services** | [**[LoadBalancerService]**](LoadBalancerService.md) | List of services that belong to this Load Balancer | 
**targets** | [**[LoadBalancerTarget]**](LoadBalancerTarget.md) | List of targets that belong to this Load Balancer | 


