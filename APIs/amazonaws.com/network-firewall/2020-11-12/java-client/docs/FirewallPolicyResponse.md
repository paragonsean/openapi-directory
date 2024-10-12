

# FirewallPolicyResponse

The high-level properties of a firewall policy. This, along with the <a>FirewallPolicy</a>, define the policy. You can retrieve all objects for a firewall policy by calling <a>DescribeFirewallPolicy</a>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firewallPolicyName** | [**String**](String.md) |  |  |
|**firewallPolicyArn** | [**String**](String.md) |  |  |
|**firewallPolicyId** | [**String**](String.md) |  |  |
|**description** | [**String**](String.md) |  |  [optional] |
|**firewallPolicyStatus** | [**ResourceStatus**](ResourceStatus.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**consumedStatelessRuleCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**consumedStatefulRuleCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**numberOfAssociations** | [**Integer**](Integer.md) |  |  [optional] |
|**encryptionConfiguration** | [**FirewallPolicyResponseEncryptionConfiguration**](FirewallPolicyResponseEncryptionConfiguration.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



