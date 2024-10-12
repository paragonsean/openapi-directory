# LinodeApi.FirewallRules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound** | [**[FirewallRuleConfig]**](FirewallRuleConfig.md) | The inbound rules for the firewall, as a JSON array.  | [optional] 
**inboundPolicy** | **String** | The default behavior for inbound traffic. This setting can be overridden by [updating](/docs/api/networking/#firewall-rules-update) the &#x60;inbound.action&#x60; property of the Firewall Rule.  | [optional] 
**outbound** | [**[FirewallRuleConfig]**](FirewallRuleConfig.md) | The outbound rules for the firewall, as a JSON array.  | [optional] 
**outboundPolicy** | **String** | The default behavior for outbound traffic. This setting can be overridden by [updating](/docs/api/networking/#firewall-rules-update) the &#x60;outbound.action&#x60; property of the Firewall Rule.  | [optional] 



## Enum: InboundPolicyEnum


* `ACCEPT` (value: `"ACCEPT"`)

* `DROP` (value: `"DROP"`)





## Enum: OutboundPolicyEnum


* `ACCEPT` (value: `"ACCEPT"`)

* `DROP` (value: `"DROP"`)




