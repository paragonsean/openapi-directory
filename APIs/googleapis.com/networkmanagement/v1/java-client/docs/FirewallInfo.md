

# FirewallInfo

For display only. Metadata associated with a VPC firewall rule, an implied VPC firewall rule, or a hierarchical firewall policy rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | Possible values: ALLOW, DENY, APPLY_SECURITY_PROFILE_GROUP |  [optional] |
|**direction** | **String** | Possible values: INGRESS, EGRESS |  [optional] |
|**displayName** | **String** | The display name of the VPC firewall rule. This field is not applicable to hierarchical firewall policy rules. |  [optional] |
|**firewallRuleType** | [**FirewallRuleTypeEnum**](#FirewallRuleTypeEnum) | The firewall rule&#39;s type. |  [optional] |
|**networkUri** | **String** | The URI of the VPC network that the firewall rule is associated with. This field is not applicable to hierarchical firewall policy rules. |  [optional] |
|**policy** | **String** | The hierarchical firewall policy that this rule is associated with. This field is not applicable to VPC firewall rules. |  [optional] |
|**priority** | **Integer** | The priority of the firewall rule. |  [optional] |
|**targetServiceAccounts** | **List&lt;String&gt;** | The target service accounts specified by the firewall rule. |  [optional] |
|**targetTags** | **List&lt;String&gt;** | The target tags defined by the VPC firewall rule. This field is not applicable to hierarchical firewall policy rules. |  [optional] |
|**uri** | **String** | The URI of the VPC firewall rule. This field is not applicable to implied firewall rules or hierarchical firewall policy rules. |  [optional] |



## Enum: FirewallRuleTypeEnum

| Name | Value |
|---- | -----|
| FIREWALL_RULE_TYPE_UNSPECIFIED | &quot;FIREWALL_RULE_TYPE_UNSPECIFIED&quot; |
| HIERARCHICAL_FIREWALL_POLICY_RULE | &quot;HIERARCHICAL_FIREWALL_POLICY_RULE&quot; |
| VPC_FIREWALL_RULE | &quot;VPC_FIREWALL_RULE&quot; |
| IMPLIED_VPC_FIREWALL_RULE | &quot;IMPLIED_VPC_FIREWALL_RULE&quot; |
| SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE | &quot;SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE&quot; |
| NETWORK_FIREWALL_POLICY_RULE | &quot;NETWORK_FIREWALL_POLICY_RULE&quot; |
| NETWORK_REGIONAL_FIREWALL_POLICY_RULE | &quot;NETWORK_REGIONAL_FIREWALL_POLICY_RULE&quot; |
| UNSUPPORTED_FIREWALL_POLICY_RULE | &quot;UNSUPPORTED_FIREWALL_POLICY_RULE&quot; |
| TRACKING_STATE | &quot;TRACKING_STATE&quot; |



