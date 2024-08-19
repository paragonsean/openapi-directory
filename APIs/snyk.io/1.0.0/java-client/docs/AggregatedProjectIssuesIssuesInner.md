

# AggregatedProjectIssuesIssuesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fixInfo** | [**ListAllAggregatedIssues200ResponseIssuesInnerFixInfo**](ListAllAggregatedIssues200ResponseIssuesInnerFixInfo.md) |  |  [optional] |
|**id** | **String** | The identifier of the issue |  |
|**ignoreReasons** | **List&lt;Object&gt;** | The list of reasons why the issue was ignored |  [optional] |
|**introducedThrough** | **List&lt;Object&gt;** | The list of what introduced the issue (it is available only for container project with Dockerfile) |  [optional] |
|**isIgnored** | **Boolean** | Whether the issue has been ignored |  |
|**isPatched** | **Boolean** | Whether the issue has been patched (Non-IaC projects only) |  |
|**issueData** | [**AggregatedProjectIssuesIssuesInnerIssueData**](AggregatedProjectIssuesIssuesInnerIssueData.md) |  |  |
|**issueType** | **String** | type of the issue (&#39;vuln&#39;, &#39;license&#39; or &#39;configuration&#39;) |  |
|**links** | [**ListAllAggregatedIssues200ResponseIssuesInnerLinks**](ListAllAggregatedIssues200ResponseIssuesInnerLinks.md) |  |  [optional] |
|**pkgName** | **String** | The package name (Non-IaC projects only) |  |
|**pkgVersions** | **List&lt;String&gt;** | List of affected package versions (Non-IaC projects only) |  |
|**priority** | [**ListAllAggregatedIssues200ResponseIssuesInnerPriority**](ListAllAggregatedIssues200ResponseIssuesInnerPriority.md) |  |  [optional] |



