# NetworkManagementClient.PublicIPPrefixPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipPrefix** | **String** | The allocated Prefix. | [optional] 
**ipTags** | [**[PublicIPPrefixPropertiesFormatIpTagsInner]**](PublicIPPrefixPropertiesFormatIpTagsInner.md) | The list of tags associated with the public IP prefix. | [optional] 
**loadBalancerFrontendIpConfiguration** | [**PublicIPPrefixPropertiesFormatLoadBalancerFrontendIpConfiguration**](PublicIPPrefixPropertiesFormatLoadBalancerFrontendIpConfiguration.md) |  | [optional] 
**prefixLength** | **Number** | The Length of the Public IP Prefix. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**publicIPAddressVersion** | **String** | IP address version. | [optional] 
**publicIPAddresses** | [**[ReferencedPublicIpAddress]**](ReferencedPublicIpAddress.md) | The list of all referenced PublicIPAddresses. | [optional] 
**resourceGuid** | **String** | The resource GUID property of the public IP prefix resource. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





## Enum: PublicIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)




