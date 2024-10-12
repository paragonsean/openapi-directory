# HetznerCloudApi.NetworksGet200ResponseNetworksInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **String** | Point in time when the Network was created (in ISO-8601 format) | 
**id** | **Number** | ID of the Network | 
**ipRange** | **String** | IPv4 prefix of the whole Network | 
**labels** | **Object** | User-defined labels (key-value pairs) | 
**loadBalancers** | **[Number]** | Array of IDs of Load Balancers attached to this Network | [optional] 
**name** | **String** | Name of the Network | 
**protection** | [**NetworksGet200ResponseNetworksInnerProtection**](NetworksGet200ResponseNetworksInnerProtection.md) |  | 
**routes** | [**[NetworksGet200ResponseNetworksInnerRoutesInner]**](NetworksGet200ResponseNetworksInnerRoutesInner.md) | Array of routes set in this Network | 
**servers** | **[Number]** | Array of IDs of Servers attached to this Network | 
**subnets** | [**[NetworksGet200ResponseNetworksInnerSubnetsInner]**](NetworksGet200ResponseNetworksInnerSubnetsInner.md) | Array subnets allocated in this Network | 


