

# GoogleCloudAssetV1GovernedContainer

The organization/folder/project resource governed by organization policies of AnalyzeOrgPolicyGovernedContainersRequest.constraint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consolidatedPolicy** | [**AnalyzerOrgPolicy**](AnalyzerOrgPolicy.md) |  |  [optional] |
|**effectiveTags** | [**List&lt;EffectiveTagDetails&gt;**](EffectiveTagDetails.md) | The effective tags on this resource. |  [optional] |
|**folders** | **List&lt;String&gt;** | The folder(s) that this resource belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to one or more folders. |  [optional] |
|**fullResourceName** | **String** | The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource. |  [optional] |
|**organization** | **String** | The organization that this resource belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to an organization. |  [optional] |
|**parent** | **String** | The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of the parent of AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.full_resource_name. |  [optional] |
|**policyBundle** | [**List&lt;AnalyzerOrgPolicy&gt;**](AnalyzerOrgPolicy.md) | The ordered list of all organization policies from the AnalyzeOrgPoliciesResponse.OrgPolicyResult.consolidated_policy.attached_resource. to the scope specified in the request. If the constraint is defined with default policy, it will also appear in the list. |  [optional] |
|**project** | **String** | The project that this resource belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project. |  [optional] |



