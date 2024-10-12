

# BatchGetEffectiveIamPoliciesResponse

A response message for AssetService.BatchGetEffectiveIamPolicies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policyResults** | [**List&lt;EffectiveIamPolicy&gt;**](EffectiveIamPolicy.md) | The effective policies for a batch of resources. Note that the results order is the same as the order of BatchGetEffectiveIamPoliciesRequest.names. When a resource does not have any effective IAM policies, its corresponding policy_result will contain empty EffectiveIamPolicy.policies. |  [optional] |



