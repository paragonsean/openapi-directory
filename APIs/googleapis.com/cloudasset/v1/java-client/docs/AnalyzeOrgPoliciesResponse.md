

# AnalyzeOrgPoliciesResponse

The response message for AssetService.AnalyzeOrgPolicies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**constraint** | [**AnalyzerOrgPolicyConstraint**](AnalyzerOrgPolicyConstraint.md) |  |  [optional] |
|**nextPageToken** | **String** | The page token to fetch the next page for AnalyzeOrgPoliciesResponse.org_policy_results. |  [optional] |
|**orgPolicyResults** | [**List&lt;OrgPolicyResult&gt;**](OrgPolicyResult.md) | The organization policies under the AnalyzeOrgPoliciesRequest.scope with the AnalyzeOrgPoliciesRequest.constraint. |  [optional] |



