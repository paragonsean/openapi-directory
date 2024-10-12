

# GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAsset

Represents a Google Cloud asset(resource or IAM policy) governed by the organization policies of the AnalyzeOrgPolicyGovernedAssetsRequest.constraint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consolidatedPolicy** | [**AnalyzerOrgPolicy**](AnalyzerOrgPolicy.md) |  |  [optional] |
|**governedIamPolicy** | [**GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicy**](GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicy.md) |  |  [optional] |
|**governedResource** | [**GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResource**](GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResource.md) |  |  [optional] |
|**policyBundle** | [**List&lt;AnalyzerOrgPolicy&gt;**](AnalyzerOrgPolicy.md) | The ordered list of all organization policies from the AnalyzeOrgPoliciesResponse.OrgPolicyResult.consolidated_policy.attached_resource to the scope specified in the request. If the constraint is defined with default policy, it will also appear in the list. |  [optional] |



