

# CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping

    The firewall and traffic shaping rules and settings for your policy. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**l3FirewallRules** | [**List&lt;CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL3FirewallRulesInner&gt;**](CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL3FirewallRulesInner.md) | An ordered array of the L3 firewall rules |  [optional] |
|**l7FirewallRules** | [**List&lt;CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner&gt;**](CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner.md) | An ordered array of L7 firewall rules |  [optional] |
|**settings** | [**SettingsEnum**](#SettingsEnum) | How firewall and traffic shaping rules are enforced. Can be &#39;network default&#39;, &#39;ignore&#39; or &#39;custom&#39;. |  [optional] |
|**trafficShapingRules** | [**List&lt;CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner&gt;**](CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.md) |     An array of traffic shaping rules. Rules are applied in the order that     they are specified in. An empty list (or null) means no rules. Note that     you are allowed a maximum of 8 rules.  |  [optional] |



## Enum: SettingsEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;custom&quot; |
| IGNORE | &quot;ignore&quot; |
| NETWORK_DEFAULT | &quot;network default&quot; |



