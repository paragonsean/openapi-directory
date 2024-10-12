

# PublicIPPrefixPropertiesFormat

Public IP prefix properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipPrefix** | **String** | The allocated Prefix. |  [optional] |
|**ipTags** | [**List&lt;PublicIPPrefixPropertiesFormatIpTagsInner&gt;**](PublicIPPrefixPropertiesFormatIpTagsInner.md) | The list of tags associated with the public IP prefix. |  [optional] |
|**loadBalancerFrontendIpConfiguration** | [**PublicIPPrefixPropertiesFormatLoadBalancerFrontendIpConfiguration**](PublicIPPrefixPropertiesFormatLoadBalancerFrontendIpConfiguration.md) |  |  [optional] |
|**prefixLength** | **Integer** | The Length of the Public IP Prefix. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**publicIPAddressVersion** | [**PublicIPAddressVersionEnum**](#PublicIPAddressVersionEnum) | IP address version. |  [optional] |
|**publicIPAddresses** | [**List&lt;ReferencedPublicIpAddress&gt;**](ReferencedPublicIpAddress.md) | The list of all referenced PublicIPAddresses. |  [optional] |
|**resourceGuid** | **String** | The resource GUID property of the public IP prefix resource. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: PublicIPAddressVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



