

# NetworksGet200ResponseNetworksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** | Point in time when the Network was created (in ISO-8601 format) |  |
|**id** | **Integer** | ID of the Network |  |
|**ipRange** | **String** | IPv4 prefix of the whole Network |  |
|**labels** | **Object** | User-defined labels (key-value pairs) |  |
|**loadBalancers** | **List&lt;Integer&gt;** | Array of IDs of Load Balancers attached to this Network |  [optional] |
|**name** | **String** | Name of the Network |  |
|**protection** | [**NetworksGet200ResponseNetworksInnerProtection**](NetworksGet200ResponseNetworksInnerProtection.md) |  |  |
|**routes** | [**List&lt;NetworksGet200ResponseNetworksInnerRoutesInner&gt;**](NetworksGet200ResponseNetworksInnerRoutesInner.md) | Array of routes set in this Network |  |
|**servers** | **List&lt;Integer&gt;** | Array of IDs of Servers attached to this Network |  |
|**subnets** | [**List&lt;NetworksGet200ResponseNetworksInnerSubnetsInner&gt;**](NetworksGet200ResponseNetworksInnerSubnetsInner.md) | Array subnets allocated in this Network |  |



