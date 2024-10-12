# WebAppsApiClient.PrivateAccessVirtualNetwork

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **Number** | The key (ID) of the Virtual Network. | [optional] 
**name** | **String** | The name of the Virtual Network. | [optional] 
**resourceId** | **String** | The ARM uri of the Virtual Network | [optional] 
**subnets** | [**[PrivateAccessSubnet]**](PrivateAccessSubnet.md) | A List of subnets that access is allowed to on this Virtual Network. An empty array (but not null) is interpreted to mean that all subnets are allowed within this Virtual Network. | [optional] 


