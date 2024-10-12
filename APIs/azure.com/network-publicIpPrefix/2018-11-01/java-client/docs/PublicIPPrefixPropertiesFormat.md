

# PublicIPPrefixPropertiesFormat

Public IP prefix properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipPrefix** | **String** | The allocated Prefix |  [optional] |
|**ipTags** | [**List&lt;IpTag&gt;**](IpTag.md) | The list of tags associated with the public IP prefix. |  [optional] |
|**loadBalancerFrontendIpConfiguration** | [**PublicIPPrefixPropertiesFormatLoadBalancerFrontendIpConfiguration**](PublicIPPrefixPropertiesFormatLoadBalancerFrontendIpConfiguration.md) |  |  [optional] |
|**prefixLength** | **Integer** | The Length of the Public IP Prefix. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the Public IP prefix resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddressVersion** | [**PublicIPAddressVersionEnum**](#PublicIPAddressVersionEnum) | The public IP address version. Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. |  [optional] |
|**publicIPAddresses** | [**List&lt;ReferencedPublicIpAddress&gt;**](ReferencedPublicIpAddress.md) | The list of all referenced PublicIPAddresses |  [optional] |
|**resourceGuid** | **String** | The resource GUID property of the public IP prefix resource. |  [optional] |



## Enum: PublicIPAddressVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



