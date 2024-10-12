

# UpdateOrganizationAdaptivePolicyPolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acls** | [**List&lt;CreateOrganizationAdaptivePolicyPolicyRequestAclsInner&gt;**](CreateOrganizationAdaptivePolicyPolicyRequestAclsInner.md) | An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy |  [optional] |
|**destinationGroup** | [**CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup**](CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup.md) |  |  [optional] |
|**lastEntryRule** | [**LastEntryRuleEnum**](#LastEntryRuleEnum) | The rule to apply if there is no matching ACL |  [optional] |
|**sourceGroup** | [**CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup**](CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup.md) |  |  [optional] |



## Enum: LastEntryRuleEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;allow&quot; |
| DEFAULT | &quot;default&quot; |
| DENY | &quot;deny&quot; |



