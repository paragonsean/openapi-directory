# MerakiDashboardApi.CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**l3FirewallRules** | [**[CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL3FirewallRulesInner]**](CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL3FirewallRulesInner.md) | An ordered array of the L3 firewall rules | [optional] 
**l7FirewallRules** | [**[CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner]**](CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner.md) | An ordered array of L7 firewall rules | [optional] 
**settings** | **String** | How firewall and traffic shaping rules are enforced. Can be &#39;network default&#39;, &#39;ignore&#39; or &#39;custom&#39;. | [optional] 
**trafficShapingRules** | [**[CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner]**](CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.md) |     An array of traffic shaping rules. Rules are applied in the order that     they are specified in. An empty list (or null) means no rules. Note that     you are allowed a maximum of 8 rules.  | [optional] 



## Enum: SettingsEnum


* `custom` (value: `"custom"`)

* `ignore` (value: `"ignore"`)

* `network default` (value: `"network default"`)




