# MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequestRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | Description of the rule (optional) | [optional] 
**destCidr** | **String** | Comma-separated list of destination IP address(es) (in IP or CIDR notation), fully-qualified domain names (FQDN) or &#39;any&#39; | 
**destPort** | **String** | Comma-separated list of destination port(s) (integer in the range 1-65535), or &#39;any&#39; | [optional] 
**policy** | **String** | &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule | 
**protocol** | **String** | The type of protocol (must be &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp&#39;, &#39;icmp6&#39; or &#39;any&#39;) | 



## Enum: PolicyEnum


* `allow` (value: `"allow"`)

* `deny` (value: `"deny"`)





## Enum: ProtocolEnum


* `any` (value: `"any"`)

* `icmp` (value: `"icmp"`)

* `icmp6` (value: `"icmp6"`)

* `tcp` (value: `"tcp"`)

* `udp` (value: `"udp"`)




