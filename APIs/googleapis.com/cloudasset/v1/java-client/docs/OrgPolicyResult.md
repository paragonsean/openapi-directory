

# OrgPolicyResult

The organization policy result to the query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consolidatedPolicy** | [**AnalyzerOrgPolicy**](AnalyzerOrgPolicy.md) |  |  [optional] |
|**folders** | **List&lt;String&gt;** | The folder(s) that this consolidated policy belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the consolidated policy belongs (directly or cascadingly) to one or more folders. |  [optional] |
|**organization** | **String** | The organization that this consolidated policy belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the consolidated policy belongs (directly or cascadingly) to an organization. |  [optional] |
|**policyBundle** | [**List&lt;AnalyzerOrgPolicy&gt;**](AnalyzerOrgPolicy.md) | The ordered list of all organization policies from the AnalyzeOrgPoliciesResponse.OrgPolicyResult.consolidated_policy.attached_resource. to the scope specified in the request. If the constraint is defined with default policy, it will also appear in the list. |  [optional] |
|**project** | **String** | The project that this consolidated policy belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the consolidated policy belongs to a project. |  [optional] |



