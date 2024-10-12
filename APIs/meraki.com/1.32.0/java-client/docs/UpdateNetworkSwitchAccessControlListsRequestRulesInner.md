

# UpdateNetworkSwitchAccessControlListsRequestRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | Description of the rule (optional). |  [optional] |
|**dstCidr** | **String** | Destination IP address (in IP or CIDR notation) or &#39;any&#39;. |  |
|**dstPort** | **String** | Destination port. Must be in the range of 1-65535 or &#39;any&#39;. Default is &#39;any&#39;. |  [optional] |
|**ipVersion** | [**IpVersionEnum**](#IpVersionEnum) | IP address version (must be &#39;any&#39;, &#39;ipv4&#39; or &#39;ipv6&#39;). Applicable only if network supports IPv6. Default value is &#39;ipv4&#39;. |  [optional] |
|**policy** | [**PolicyEnum**](#PolicyEnum) | &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule. |  |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The type of protocol (must be &#39;tcp&#39;, &#39;udp&#39;, or &#39;any&#39;). |  |
|**srcCidr** | **String** | Source IP address (in IP or CIDR notation) or &#39;any&#39;. |  |
|**srcPort** | **String** | Source port. Must be in the range  of 1-65535 or &#39;any&#39;. Default is &#39;any&#39;. |  [optional] |
|**vlan** | **String** | Incoming traffic VLAN. Must be in the range of 1-4095 or &#39;any&#39;. Default is &#39;any&#39;. |  [optional] |



## Enum: IpVersionEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| IPV4 | &quot;ipv4&quot; |
| IPV6 | &quot;ipv6&quot; |



## Enum: PolicyEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;allow&quot; |
| DENY | &quot;deny&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



