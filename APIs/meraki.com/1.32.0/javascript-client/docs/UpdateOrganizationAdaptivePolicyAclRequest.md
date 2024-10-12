# MerakiDashboardApi.UpdateOrganizationAdaptivePolicyAclRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the adaptive policy ACL | [optional] 
**ipVersion** | **String** | IP version of adpative policy ACL. One of: &#39;any&#39;, &#39;ipv4&#39; or &#39;ipv6&#39; | [optional] 
**name** | **String** | Name of the adaptive policy ACL | [optional] 
**rules** | [**[CreateOrganizationAdaptivePolicyAclRequestRulesInner]**](CreateOrganizationAdaptivePolicyAclRequestRulesInner.md) | An ordered array of the adaptive policy ACL rules. An empty array will clear the rules. | [optional] 



## Enum: IpVersionEnum


* `any` (value: `"any"`)

* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)




