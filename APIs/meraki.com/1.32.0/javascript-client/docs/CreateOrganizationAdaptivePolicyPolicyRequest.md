# MerakiDashboardApi.CreateOrganizationAdaptivePolicyPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acls** | [**[CreateOrganizationAdaptivePolicyPolicyRequestAclsInner]**](CreateOrganizationAdaptivePolicyPolicyRequestAclsInner.md) | An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: []) | [optional] 
**destinationGroup** | [**CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup**](CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup.md) |  | 
**lastEntryRule** | **String** | The rule to apply if there is no matching ACL (default: \&quot;default\&quot;) | [optional] 
**sourceGroup** | [**CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup**](CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup.md) |  | 



## Enum: LastEntryRuleEnum


* `allow` (value: `"allow"`)

* `default` (value: `"default"`)

* `deny` (value: `"deny"`)




