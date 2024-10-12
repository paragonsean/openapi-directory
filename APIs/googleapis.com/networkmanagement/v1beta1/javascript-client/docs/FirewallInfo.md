# NetworkManagementApi.FirewallInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Possible values: ALLOW, DENY, APPLY_SECURITY_PROFILE_GROUP | [optional] 
**direction** | **String** | Possible values: INGRESS, EGRESS | [optional] 
**displayName** | **String** | The display name of the VPC firewall rule. This field is not applicable to hierarchical firewall policy rules. | [optional] 
**firewallRuleType** | **String** | The firewall rule&#39;s type. | [optional] 
**networkUri** | **String** | The URI of the VPC network that the firewall rule is associated with. This field is not applicable to hierarchical firewall policy rules. | [optional] 
**policy** | **String** | The hierarchical firewall policy that this rule is associated with. This field is not applicable to VPC firewall rules. | [optional] 
**priority** | **Number** | The priority of the firewall rule. | [optional] 
**targetServiceAccounts** | **[String]** | The target service accounts specified by the firewall rule. | [optional] 
**targetTags** | **[String]** | The target tags defined by the VPC firewall rule. This field is not applicable to hierarchical firewall policy rules. | [optional] 
**uri** | **String** | The URI of the VPC firewall rule. This field is not applicable to implied firewall rules or hierarchical firewall policy rules. | [optional] 



## Enum: FirewallRuleTypeEnum


* `FIREWALL_RULE_TYPE_UNSPECIFIED` (value: `"FIREWALL_RULE_TYPE_UNSPECIFIED"`)

* `HIERARCHICAL_FIREWALL_POLICY_RULE` (value: `"HIERARCHICAL_FIREWALL_POLICY_RULE"`)

* `VPC_FIREWALL_RULE` (value: `"VPC_FIREWALL_RULE"`)

* `IMPLIED_VPC_FIREWALL_RULE` (value: `"IMPLIED_VPC_FIREWALL_RULE"`)

* `SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE` (value: `"SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE"`)

* `NETWORK_FIREWALL_POLICY_RULE` (value: `"NETWORK_FIREWALL_POLICY_RULE"`)

* `NETWORK_REGIONAL_FIREWALL_POLICY_RULE` (value: `"NETWORK_REGIONAL_FIREWALL_POLICY_RULE"`)

* `UNSUPPORTED_FIREWALL_POLICY_RULE` (value: `"UNSUPPORTED_FIREWALL_POLICY_RULE"`)

* `TRACKING_STATE` (value: `"TRACKING_STATE"`)




