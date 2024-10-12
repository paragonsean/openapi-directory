

# CreateOrganizationAdaptivePolicyAclRequestRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dstPort** | **String** | Destination port. Must be in the format of single port: &#39;1&#39;, port list: &#39;1,2&#39; or port range: &#39;1-10&#39;, and in the range of 1-65535, or &#39;any&#39;. Default is &#39;any&#39;. |  [optional] |
|**policy** | [**PolicyEnum**](#PolicyEnum) | &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule. |  |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The type of protocol (must be &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp&#39; or &#39;any&#39;). |  |
|**srcPort** | **String** | Source port. Must be in the format of single port: &#39;1&#39;, port list: &#39;1,2&#39; or port range: &#39;1-10&#39;, and in the range of 1-65535, or &#39;any&#39;. Default is &#39;any&#39;. |  [optional] |



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
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



