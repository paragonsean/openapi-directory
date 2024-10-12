

# PutV3ProjectsIdRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the project |  [optional] |
|**defaultBranch** | **String** | The default branch of the project |  [optional] |
|**path** | **String** | The path of the repository |  [optional] |
|**description** | **String** | The description of the project |  [optional] |
|**issuesEnabled** | **Boolean** | Flag indication if the issue tracker is enabled |  [optional] |
|**mergeRequestsEnabled** | **Boolean** | Flag indication if merge requests are enabled |  [optional] |
|**wikiEnabled** | **Boolean** | Flag indication if the wiki is enabled |  [optional] |
|**buildsEnabled** | **Boolean** | Flag indication if builds are enabled |  [optional] |
|**snippetsEnabled** | **Boolean** | Flag indication if snippets are enabled |  [optional] |
|**sharedRunnersEnabled** | **Boolean** | Flag indication if shared runners are enabled for that project |  [optional] |
|**containerRegistryEnabled** | **Boolean** | Flag indication if the container registry is enabled for that project |  [optional] |
|**lfsEnabled** | **Boolean** | Flag indication if Git LFS is enabled for that project |  [optional] |
|**_public** | **Boolean** | Create a public project. The same as visibility_level &#x3D; 20. |  [optional] |
|**visibilityLevel** | [**VisibilityLevelEnum**](#VisibilityLevelEnum) | Create a public project. The same as visibility_level &#x3D; 20. |  [optional] |
|**publicBuilds** | **Boolean** | Perform public builds |  [optional] |
|**requestAccessEnabled** | **Boolean** | Allow users to request member access |  [optional] |
|**onlyAllowMergeIfBuildSucceeds** | **Boolean** | Only allow to merge if builds succeed |  [optional] |
|**onlyAllowMergeIfAllDiscussionsAreResolved** | **Boolean** | Only allow to merge if all discussions are resolved |  [optional] |



## Enum: VisibilityLevelEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_10 | 10 |
| NUMBER_20 | 20 |



