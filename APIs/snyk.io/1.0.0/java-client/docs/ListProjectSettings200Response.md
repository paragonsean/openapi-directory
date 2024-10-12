

# ListProjectSettings200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoDepUpgradeEnabled** | **Boolean** | If set to &#x60;true&#x60;, Snyk will raise dependency upgrade PRs automatically. |  [optional] |
|**autoDepUpgradeIgnoredDependencies** | **List&lt;Object&gt;** | An array of comma-separated strings with names of dependencies you wish Snyk to ignore to upgrade. |  [optional] |
|**autoDepUpgradeLimit** | **BigDecimal** | The limit on auto dependency upgrade PRs. |  [optional] |
|**autoDepUpgradeMinAge** | **BigDecimal** | The age (in days) that an automatic dependency check is valid for |  [optional] |
|**autoRemediationPrs** | [**ListProjectSettings200ResponseAutoRemediationPrs**](ListProjectSettings200ResponseAutoRemediationPrs.md) |  |  [optional] |
|**pullRequestAssignment** | [**Retrieve200ResponsePullRequestAssignment**](Retrieve200ResponsePullRequestAssignment.md) |  |  [optional] |
|**pullRequestFailOnAnyVulns** | **Boolean** | If set to &#x60;true&#x60;, fail Snyk Test if the repo has any vulnerabilities. Otherwise, fail only when the PR is adding a vulnerable dependency. |  [optional] |
|**pullRequestFailOnlyForHighSeverity** | **Boolean** | If set to &#x60;true&#x60;, fail Snyk Test only for high and critical severity vulnerabilities |  [optional] |
|**pullRequestTestEnabled** | **Boolean** | If set to &#x60;true&#x60;, Snyk Test checks PRs for vulnerabilities.:cq |  [optional] |



