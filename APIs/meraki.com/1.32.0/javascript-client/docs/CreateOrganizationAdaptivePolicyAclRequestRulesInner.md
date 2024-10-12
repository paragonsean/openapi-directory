# MerakiDashboardApi.CreateOrganizationAdaptivePolicyAclRequestRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dstPort** | **String** | Destination port. Must be in the format of single port: &#39;1&#39;, port list: &#39;1,2&#39; or port range: &#39;1-10&#39;, and in the range of 1-65535, or &#39;any&#39;. Default is &#39;any&#39;. | [optional] 
**policy** | **String** | &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule. | 
**protocol** | **String** | The type of protocol (must be &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp&#39; or &#39;any&#39;). | 
**srcPort** | **String** | Source port. Must be in the format of single port: &#39;1&#39;, port list: &#39;1,2&#39; or port range: &#39;1-10&#39;, and in the range of 1-65535, or &#39;any&#39;. Default is &#39;any&#39;. | [optional] 



## Enum: PolicyEnum


* `allow` (value: `"allow"`)

* `deny` (value: `"deny"`)





## Enum: ProtocolEnum


* `any` (value: `"any"`)

* `icmp` (value: `"icmp"`)

* `tcp` (value: `"tcp"`)

* `udp` (value: `"udp"`)




