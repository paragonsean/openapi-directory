# AnthosOnPremApi.BareMetalMetalLbConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPools** | [**[BareMetalLoadBalancerAddressPool]**](BareMetalLoadBalancerAddressPool.md) | Required. AddressPools is a list of non-overlapping IP pools used by load balancer typed services. All addresses must be routable to load balancer nodes. IngressVIP must be included in the pools. | [optional] 
**loadBalancerNodePoolConfig** | [**BareMetalLoadBalancerNodePoolConfig**](BareMetalLoadBalancerNodePoolConfig.md) |  | [optional] 


