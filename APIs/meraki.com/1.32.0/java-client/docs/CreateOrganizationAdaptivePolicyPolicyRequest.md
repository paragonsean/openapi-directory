

# CreateOrganizationAdaptivePolicyPolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acls** | [**List&lt;CreateOrganizationAdaptivePolicyPolicyRequestAclsInner&gt;**](CreateOrganizationAdaptivePolicyPolicyRequestAclsInner.md) | An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: []) |  [optional] |
|**destinationGroup** | [**CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup**](CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup.md) |  |  |
|**lastEntryRule** | [**LastEntryRuleEnum**](#LastEntryRuleEnum) | The rule to apply if there is no matching ACL (default: \&quot;default\&quot;) |  [optional] |
|**sourceGroup** | [**CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup**](CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup.md) |  |  |



## Enum: LastEntryRuleEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;allow&quot; |
| DEFAULT | &quot;default&quot; |
| DENY | &quot;deny&quot; |



