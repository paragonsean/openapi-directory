

# FirewallRules

The inbound and outbound access rules to apply to the Firewall.  A Firewall may have up to 25 rules across its inbound and outbound rulesets. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inbound** | [**List&lt;FirewallRuleConfig&gt;**](FirewallRuleConfig.md) | The inbound rules for the firewall, as a JSON array.  |  [optional] |
|**inboundPolicy** | [**InboundPolicyEnum**](#InboundPolicyEnum) | The default behavior for inbound traffic. This setting can be overridden by [updating](/docs/api/networking/#firewall-rules-update) the &#x60;inbound.action&#x60; property of the Firewall Rule.  |  [optional] |
|**outbound** | [**List&lt;FirewallRuleConfig&gt;**](FirewallRuleConfig.md) | The outbound rules for the firewall, as a JSON array.  |  [optional] |
|**outboundPolicy** | [**OutboundPolicyEnum**](#OutboundPolicyEnum) | The default behavior for outbound traffic. This setting can be overridden by [updating](/docs/api/networking/#firewall-rules-update) the &#x60;outbound.action&#x60; property of the Firewall Rule.  |  [optional] |



## Enum: InboundPolicyEnum

| Name | Value |
|---- | -----|
| ACCEPT | &quot;ACCEPT&quot; |
| DROP | &quot;DROP&quot; |



## Enum: OutboundPolicyEnum

| Name | Value |
|---- | -----|
| ACCEPT | &quot;ACCEPT&quot; |
| DROP | &quot;DROP&quot; |



