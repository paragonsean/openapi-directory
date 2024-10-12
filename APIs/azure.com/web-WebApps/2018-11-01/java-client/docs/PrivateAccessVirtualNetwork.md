

# PrivateAccessVirtualNetwork

Description of a Virtual Network that is useable for private site access.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **Integer** | The key (ID) of the Virtual Network. |  [optional] |
|**name** | **String** | The name of the Virtual Network. |  [optional] |
|**resourceId** | **String** | The ARM uri of the Virtual Network |  [optional] |
|**subnets** | [**List&lt;PrivateAccessSubnet&gt;**](PrivateAccessSubnet.md) | A List of subnets that access is allowed to on this Virtual Network. An empty array (but not null) is interpreted to mean that all subnets are allowed within this Virtual Network. |  [optional] |



