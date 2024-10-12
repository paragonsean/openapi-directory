

# ManagedRuleGroupOverride

Defines a managed rule group override setting.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exclusions** | [**List&lt;ManagedRuleExclusion&gt;**](ManagedRuleExclusion.md) | Describes the exclusions that are applied to all rules in the group. |  [optional] |
|**ruleGroupName** | **String** | Describes the managed rule group to override. |  |
|**rules** | [**List&lt;ManagedRuleOverride&gt;**](ManagedRuleOverride.md) | List of rules that will be disabled. If none specified, all rules in the group will be disabled. |  [optional] |



