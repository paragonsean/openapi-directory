

# UpdateOrganizationVpnFirewallRulesRequestRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | Description of the rule (optional) |  [optional] |
|**destCidr** | **String** | Comma-separated list of destination IP address(es) (in IP or CIDR notation) or &#39;any&#39; (FQDN not supported) |  |
|**destPort** | **String** | Comma-separated list of destination port(s) (integer in the range 1-65535), or &#39;any&#39; |  [optional] |
|**policy** | [**PolicyEnum**](#PolicyEnum) | &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule |  |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The type of protocol (must be &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp&#39;, &#39;icmp6&#39; or &#39;any&#39;) |  |
|**srcCidr** | **String** | Comma-separated list of source IP address(es) (in IP or CIDR notation), or &#39;any&#39; (FQDN not supported) |  |
|**srcPort** | **String** | Comma-separated list of source port(s) (integer in the range 1-65535), or &#39;any&#39; |  [optional] |
|**syslogEnabled** | **Boolean** | Log this rule to syslog (true or false, boolean value) - only applicable if a syslog has been configured (optional) |  [optional] |



## Enum: PolicyEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;allow&quot; |
| DENY | &quot;deny&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| ICMP | &quot;icmp&quot; |
| ICMP6 | &quot;icmp6&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



