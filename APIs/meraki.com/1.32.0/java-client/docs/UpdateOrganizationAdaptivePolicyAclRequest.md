

# UpdateOrganizationAdaptivePolicyAclRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the adaptive policy ACL |  [optional] |
|**ipVersion** | [**IpVersionEnum**](#IpVersionEnum) | IP version of adpative policy ACL. One of: &#39;any&#39;, &#39;ipv4&#39; or &#39;ipv6&#39; |  [optional] |
|**name** | **String** | Name of the adaptive policy ACL |  [optional] |
|**rules** | [**List&lt;CreateOrganizationAdaptivePolicyAclRequestRulesInner&gt;**](CreateOrganizationAdaptivePolicyAclRequestRulesInner.md) | An ordered array of the adaptive policy ACL rules. An empty array will clear the rules. |  [optional] |



## Enum: IpVersionEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| IPV4 | &quot;ipv4&quot; |
| IPV6 | &quot;ipv6&quot; |



