# Gitlab.PostV3ProjectsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the project | 
**path** | **String** | The path of the repository | [optional] 
**description** | **String** | The description of the project | [optional] 
**issuesEnabled** | **Boolean** | Flag indication if the issue tracker is enabled | [optional] 
**mergeRequestsEnabled** | **Boolean** | Flag indication if merge requests are enabled | [optional] 
**wikiEnabled** | **Boolean** | Flag indication if the wiki is enabled | [optional] 
**buildsEnabled** | **Boolean** | Flag indication if builds are enabled | [optional] 
**snippetsEnabled** | **Boolean** | Flag indication if snippets are enabled | [optional] 
**sharedRunnersEnabled** | **Boolean** | Flag indication if shared runners are enabled for that project | [optional] 
**containerRegistryEnabled** | **Boolean** | Flag indication if the container registry is enabled for that project | [optional] 
**lfsEnabled** | **Boolean** | Flag indication if Git LFS is enabled for that project | [optional] 
**_public** | **Boolean** | Create a public project. The same as visibility_level &#x3D; 20. | [optional] 
**visibilityLevel** | **Number** | Create a public project. The same as visibility_level &#x3D; 20. | [optional] 
**publicBuilds** | **Boolean** | Perform public builds | [optional] 
**requestAccessEnabled** | **Boolean** | Allow users to request member access | [optional] 
**onlyAllowMergeIfBuildSucceeds** | **Boolean** | Only allow to merge if builds succeed | [optional] 
**onlyAllowMergeIfAllDiscussionsAreResolved** | **Boolean** | Only allow to merge if all discussions are resolved | [optional] 
**namespaceId** | **Number** | Namespace ID for the new project. Default to the user namespace. | [optional] 
**importUrl** | **String** | URL from which the project is imported | [optional] 



## Enum: VisibilityLevelEnum


* `0` (value: `0`)

* `10` (value: `10`)

* `20` (value: `20`)




