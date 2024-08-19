

# GetListOfIssues200ResponseResultsInnerIssue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cvSSv3** | **String** | The CVSS v3 string that signifies how the CVSS score was calculated (not applicable to licenses) |  [optional] |
|**credit** | **List&lt;Object&gt;** | The list of people responsible for first uncovering or reporting the issue (not applicable to licenses) |  [optional] |
|**cvssScore** | **BigDecimal** | The CVSS score that results from running the CVSSv3 string (not applicable to licenses) |  [optional] |
|**disclosureTime** | **String** | The date that the vulnerability was first disclosed (not applicable to licenses) |  [optional] |
|**exploitMaturity** | **String** | The exploit maturity of the issue |  |
|**id** | **String** | The identifier of the issue |  |
|**identifiers** | [**GetListOfIssues200ResponseResultsInnerIssueIdentifiers**](GetListOfIssues200ResponseResultsInnerIssueIdentifiers.md) |  |  [optional] |
|**ignored** | **List&lt;Object&gt;** | The list of ignore rules that were applied to the issue (only present if issue was ignored and no &#x60;groupBy&#x60; in the API request) |  [optional] |
|**isIgnored** | **Boolean** | Whether the issue has been ignored (only present if there is no &#x60;groupBy&#x60; in the API request) |  [optional] |
|**isPatchable** | **Boolean** | Whether the issue can be patched |  [optional] |
|**isPatched** | **Boolean** | Whether the issue has been patched (not applicable to licenses and only present if there is no &#x60;groupBy&#x60; in the API request) |  [optional] |
|**isPinnable** | **Boolean** | Whether the issue can be pinned |  [optional] |
|**isUpgradable** | **Boolean** | Whether the issue can be fixed by upgrading to a later version of the dependency |  [optional] |
|**jiraIssueUrl** | **String** | The link to the Jira issue attached to the vulnerability |  [optional] |
|**language** | **String** | The language of the issue |  [optional] |
|**originalSeverity** | **String** | The original severity status of the issue, as retrieved from Snyk Vulnerability database, before policies are applied |  |
|**_package** | **String** | The name of the package that the issue relates to |  |
|**packageManager** | **String** | The package manager of the issue |  [optional] |
|**patches** | **List&lt;Object&gt;** | A list of patches available for the given issue (not applicable to licenses) |  [optional] |
|**priorityScore** | **BigDecimal** | The priority score ranging between 0-1000 |  [optional] |
|**publicationTime** | **String** | The date that the vulnerability was first published by Snyk (not applicable to licenses) |  [optional] |
|**semver** | [**GetListOfIssues200ResponseResultsInnerIssueSemver**](GetListOfIssues200ResponseResultsInnerIssueSemver.md) |  |  [optional] |
|**severity** | **String** | The severity status of the issue, after policies are applied |  |
|**title** | **String** | The issue title |  |
|**type** | **String** | The issue type, can be \&quot;vuln\&quot;, \&quot;license\&quot; |  |
|**uniqueSeveritiesList** | **List&lt;Object&gt;** | A list of all severities in issue per projects |  [optional] |
|**url** | **String** | URL to a page containing information about the issue |  |
|**version** | **String** | The version of the package that the issue relates to |  |



