

# ListAllAggregatedIssues200ResponseIssuesInnerIssueData

The details of the issue

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cvSSv3** | **String** | The CVSS v3 string that signifies how the CVSS score was calculated (Non-IaC projects only) |  |
|**credit** | **List&lt;Object&gt;** | The list of people responsible for first uncovering or reporting the issue (Non-IaC projects only) |  |
|**cvssScore** | **BigDecimal** | The CVSS score that results from running the CVSSv3 string (Non-IaC projects only) |  |
|**description** | **String** |  |  |
|**disclosureTime** | **String** | The date that the vulnerability was first disclosed |  |
|**exploitMaturity** | **String** | The exploit maturity of the issue |  |
|**id** | **String** | The identifier of the issue |  |
|**identifiers** | [**ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers**](ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers.md) |  |  |
|**isMaliciousPackage** | **Boolean** | Whether the issue is intentional, indicating a malicious package |  |
|**language** | **String** | The language of the issue (Non-IaC projects only) |  |
|**nearestFixedInVersion** | **String** | Nearest version which includes a fix for the issue. This is populated for container projects only. (Non-IaC projects only) |  |
|**originalSeverity** | **String** | The original severity status of the issue, as retrieved from Snyk Vulnerability database, before policies are applied |  |
|**patches** | **List&lt;Object&gt;** | A list of patches available for the given issue (Non-IaC projects only) |  |
|**path** | **String** | Path to the resource property violating the policy within the scanned project. (IaC projects only) |  |
|**publicationTime** | **String** | The date that the vulnerability was first published by Snyk (Non-IaC projects only) |  |
|**semver** | [**ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver**](ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver.md) |  |  |
|**severity** | **String** | The severity status of the issue, after policies are applied |  |
|**title** | **String** | The issue title |  |
|**url** | **String** | URL to a page containing information about the issue |  |
|**violatedPolicyPublicId** | **String** | The ID of the violated policy in the issue (IaC projects only) |  |



