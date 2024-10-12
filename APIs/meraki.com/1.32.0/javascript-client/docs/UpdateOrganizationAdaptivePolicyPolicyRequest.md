# MerakiDashboardApi.UpdateOrganizationAdaptivePolicyPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acls** | [**[CreateOrganizationAdaptivePolicyPolicyRequestAclsInner]**](CreateOrganizationAdaptivePolicyPolicyRequestAclsInner.md) | An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy | [optional] 
**destinationGroup** | [**CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup**](CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup.md) |  | [optional] 
**lastEntryRule** | **String** | The rule to apply if there is no matching ACL | [optional] 
**sourceGroup** | [**CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup**](CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup.md) |  | [optional] 



## Enum: LastEntryRuleEnum


* `allow` (value: `"allow"`)

* `default` (value: `"default"`)

* `deny` (value: `"deny"`)




