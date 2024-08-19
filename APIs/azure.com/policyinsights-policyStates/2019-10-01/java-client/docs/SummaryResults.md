

# SummaryResults

Compliance summary on a particular summary level.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nonCompliantPolicies** | **Integer** | Number of non-compliant policies. |  [optional] |
|**nonCompliantResources** | **Integer** | Number of non-compliant resources. |  [optional] |
|**policyDetails** | [**List&lt;ComplianceDetail&gt;**](ComplianceDetail.md) | The policy artifact summary at this level. For query scope level, it represents policy assignment summary. For policy assignment level, it represents policy definitions summary. |  [optional] |
|**policyGroupDetails** | [**List&lt;ComplianceDetail&gt;**](ComplianceDetail.md) | The policy definition group summary at this level. |  [optional] |
|**queryResultsUri** | **String** | HTTP POST URI for queryResults action on Microsoft.PolicyInsights to retrieve raw results for the compliance summary. This property will not be available by default in future API versions, but could be queried explicitly. |  [optional] |
|**resourceDetails** | [**List&lt;ComplianceDetail&gt;**](ComplianceDetail.md) | The resources summary at this level. |  [optional] |



