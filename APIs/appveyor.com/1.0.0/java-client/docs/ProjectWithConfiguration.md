

# ProjectWithConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** |  |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |
|**projectId** | **Integer** |  |  |
|**slug** | **String** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**accountId** | **Integer** |  |  [optional] [readonly] |
|**alwaysBuildClosedPullRequests** | **Boolean** |  |  [optional] |
|**builds** | [**List&lt;Build&gt;**](Build.md) | Only non-empty for response from getProjects. |  [optional] [readonly] |
|**currentBuildId** | **Integer** |  |  [optional] |
|**disablePullRequestWebhooks** | **Boolean** |  |  [optional] |
|**disablePushWebhooks** | **Boolean** |  |  [optional] |
|**enableDeploymentInPullRequests** | **Boolean** |  |  [optional] |
|**enableSecureVariablesInPullRequests** | **Boolean** |  |  [optional] |
|**enableSecureVariablesInPullRequestsFromSameRepo** | **Boolean** |  |  [optional] |
|**isGitHubApp** | **Boolean** |  |  [optional] |
|**isPrivate** | **Boolean** |  |  [optional] |
|**nuGetFeed** | [**NuGetFeed**](NuGetFeed.md) |  |  [optional] |
|**repositoryBranch** | **String** | Not present in response from addProject. |  [optional] |
|**repositoryName** | **String** |  |  |
|**repositoryScm** | **RepositoryScm** |  |  [optional] |
|**repositoryType** | **RepositoryProvider** |  |  [optional] |
|**rollingBuilds** | **Boolean** |  |  [optional] |
|**rollingBuildsDoNotCancelRunningBuilds** | **Boolean** |  |  [optional] |
|**rollingBuildsOnlyForPullRequests** | **Boolean** |  |  [optional] |
|**saveBuildCacheInPullRequests** | **Boolean** |  |  [optional] |
|**securityDescriptor** | [**SecurityDescriptor**](SecurityDescriptor.md) |  |  [optional] |
|**skipBranchesWithoutAppveyorYml** | **Boolean** |  |  [optional] |
|**tags** | **String** | Comma-separated list of project tags for dynamic grouping. Appears that any input is accepted.  The returned value only contains case-preserving but insensitive unique values where spaces around \&quot;,\&quot; are removed but otherwise preserved.  Empty values and items are allowed. |  [optional] |
|**buildPriority** | **Integer** |  |  [optional] |
|**_configuration** | [**ProjectConfiguration**](ProjectConfiguration.md) |  |  |
|**customYmlName** | **String** |  |  [optional] |
|**ignoreAppveyorYml** | **Boolean** |  |  [optional] |
|**nextBuildNumber** | **Integer** |  |  [optional] |
|**repositoryAuthentication** | **RepositoryAuthenticationType** |  |  [optional] |
|**repositoryUsername** | **String** |  |  [optional] |
|**scheduleCrontabExpression** | **String** | Build schedule as an NCrontab Expression.  See https://github.com/atifaziz/NCrontab/wiki/Crontab-Expression |  [optional] |
|**sshPublicKey** | **String** |  |  [optional] |
|**statusBadgeId** | **String** |  |  [optional] |
|**versionFormat** | **String** |  |  |
|**webhookId** | **String** |  |  [optional] |
|**webhookUrl** | **URI** |  |  [optional] |



