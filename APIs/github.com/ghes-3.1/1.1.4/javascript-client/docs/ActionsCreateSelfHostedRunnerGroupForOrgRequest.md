# GitHubV3RestApi.ActionsCreateSelfHostedRunnerGroupForOrgRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowsPublicRepositories** | **Boolean** | Whether the runner group can be used by &#x60;public&#x60; repositories. | [optional] [default to false]
**name** | **String** | Name of the runner group. | 
**runners** | **[Number]** | List of runner IDs to add to the runner group. | [optional] 
**selectedRepositoryIds** | **[Number]** | List of repository IDs that can access the runner group. | [optional] 
**visibility** | **String** | Visibility of a runner group. You can select all repositories, select individual repositories, or limit access to private repositories. | [optional] [default to &#39;all&#39;]



## Enum: VisibilityEnum


* `selected` (value: `"selected"`)

* `all` (value: `"all"`)

* `private` (value: `"private"`)




