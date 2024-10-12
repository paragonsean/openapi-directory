# AnthosOnPremApi.BareMetalBgpLbConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPools** | [**[BareMetalLoadBalancerAddressPool]**](BareMetalLoadBalancerAddressPool.md) | Required. AddressPools is a list of non-overlapping IP pools used by load balancer typed services. All addresses must be routable to load balancer nodes. IngressVIP must be included in the pools. | [optional] 
**asn** | **String** | Required. BGP autonomous system number (ASN) of the cluster. This field can be updated after cluster creation. | [optional] 
**bgpPeerConfigs** | [**[BareMetalBgpPeerConfig]**](BareMetalBgpPeerConfig.md) | Required. The list of BGP peers that the cluster will connect to. At least one peer must be configured for each control plane node. Control plane nodes will connect to these peers to advertise the control plane VIP. The Services load balancer also uses these peers by default. This field can be updated after cluster creation. | [optional] 
**loadBalancerNodePoolConfig** | [**BareMetalLoadBalancerNodePoolConfig**](BareMetalLoadBalancerNodePoolConfig.md) |  | [optional] 


