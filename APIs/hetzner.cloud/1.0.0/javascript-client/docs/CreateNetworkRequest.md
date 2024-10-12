# HetznerCloudApi.CreateNetworkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipRange** | **String** | IP range of the whole network which must span all included subnets. Must be one of the private IPv4 ranges of RFC1918. Minimum network size is /24. We highly recommend that you pick a larger network with a /16 netmask. | 
**labels** | [**CreateLoadBalancerRequestLabels**](CreateLoadBalancerRequestLabels.md) |  | [optional] 
**name** | **String** | Name of the network | 
**routes** | [**[NetworksGet200ResponseNetworksInnerRoutesInner]**](NetworksGet200ResponseNetworksInnerRoutesInner.md) | Array of routes set in this network. The destination of the route must be one of the private IPv4 ranges of RFC1918. The gateway must be a subnet/IP of the ip_range of the network object. The destination must not overlap with an existing ip_range in any subnets or with any destinations in other routes or with the first IP of the networks ip_range or with 172.31.1.1. The gateway cannot be the first IP of the networks ip_range and also cannot be 172.31.1.1. | [optional] 
**subnets** | [**[CreateNetworkRequestSubnetsInner]**](CreateNetworkRequestSubnetsInner.md) | Array of subnets allocated. | [optional] 


