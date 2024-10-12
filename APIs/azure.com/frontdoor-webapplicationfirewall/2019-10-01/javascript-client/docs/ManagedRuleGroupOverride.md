# WebApplicationFirewallManagement.ManagedRuleGroupOverride

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusions** | [**[ManagedRuleExclusion]**](ManagedRuleExclusion.md) | Describes the exclusions that are applied to all rules in the group. | [optional] 
**ruleGroupName** | **String** | Describes the managed rule group to override. | 
**rules** | [**[ManagedRuleOverride]**](ManagedRuleOverride.md) | List of rules that will be disabled. If none specified, all rules in the group will be disabled. | [optional] 


