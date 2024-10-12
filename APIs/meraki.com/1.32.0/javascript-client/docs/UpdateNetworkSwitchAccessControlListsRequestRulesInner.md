# MerakiDashboardApi.UpdateNetworkSwitchAccessControlListsRequestRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | Description of the rule (optional). | [optional] 
**dstCidr** | **String** | Destination IP address (in IP or CIDR notation) or &#39;any&#39;. | 
**dstPort** | **String** | Destination port. Must be in the range of 1-65535 or &#39;any&#39;. Default is &#39;any&#39;. | [optional] 
**ipVersion** | **String** | IP address version (must be &#39;any&#39;, &#39;ipv4&#39; or &#39;ipv6&#39;). Applicable only if network supports IPv6. Default value is &#39;ipv4&#39;. | [optional] 
**policy** | **String** | &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule. | 
**protocol** | **String** | The type of protocol (must be &#39;tcp&#39;, &#39;udp&#39;, or &#39;any&#39;). | 
**srcCidr** | **String** | Source IP address (in IP or CIDR notation) or &#39;any&#39;. | 
**srcPort** | **String** | Source port. Must be in the range  of 1-65535 or &#39;any&#39;. Default is &#39;any&#39;. | [optional] 
**vlan** | **String** | Incoming traffic VLAN. Must be in the range of 1-4095 or &#39;any&#39;. Default is &#39;any&#39;. | [optional] 



## Enum: IpVersionEnum


* `any` (value: `"any"`)

* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)





## Enum: PolicyEnum


* `allow` (value: `"allow"`)

* `deny` (value: `"deny"`)





## Enum: ProtocolEnum


* `any` (value: `"any"`)

* `tcp` (value: `"tcp"`)

* `udp` (value: `"udp"`)




