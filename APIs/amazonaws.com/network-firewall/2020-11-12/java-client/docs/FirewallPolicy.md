

# FirewallPolicy

<p>The firewall policy defines the behavior of a firewall using a collection of stateless and stateful rule groups and other settings. You can use one firewall policy for multiple firewalls. </p> <p>This, along with <a>FirewallPolicyResponse</a>, define the policy. You can retrieve all objects for a firewall policy by calling <a>DescribeFirewallPolicy</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**statelessRuleGroupReferences** | [**List**](List.md) |  |  [optional] |
|**statelessDefaultActions** | [**List**](List.md) |  |  |
|**statelessFragmentDefaultActions** | [**List**](List.md) |  |  |
|**statelessCustomActions** | [**List**](List.md) |  |  [optional] |
|**statefulRuleGroupReferences** | [**List**](List.md) |  |  [optional] |
|**statefulDefaultActions** | [**List**](List.md) |  |  [optional] |
|**statefulEngineOptions** | [**FirewallPolicyStatefulEngineOptions**](FirewallPolicyStatefulEngineOptions.md) |  |  [optional] |
|**tlSInspectionConfigurationArn** | [**String**](String.md) |  |  [optional] |
|**policyVariables** | [**FirewallPolicyPolicyVariables**](FirewallPolicyPolicyVariables.md) |  |  [optional] |



