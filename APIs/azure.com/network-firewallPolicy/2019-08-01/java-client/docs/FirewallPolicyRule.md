

# FirewallPolicyRule

Properties of the rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the rule. |  [optional] |
|**priority** | **Integer** | Priority of the Firewall Policy Rule resource. |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | The type of the rule. |  |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| FIREWALL_POLICY_NAT_RULE | &quot;FirewallPolicyNatRule&quot; |
| FIREWALL_POLICY_FILTER_RULE | &quot;FirewallPolicyFilterRule&quot; |



