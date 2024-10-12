# GitHubV3RestApi.ActionsUpdateSelfHostedRunnerGroupForOrgRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowsPublicRepositories** | **Boolean** | Whether the runner group can be used by &#x60;public&#x60; repositories. | [optional] [default to false]
**name** | **String** | Name of the runner group. | 
**visibility** | **String** | Visibility of a runner group. You can select all repositories, select individual repositories, or all private repositories. Can be one of: &#x60;all&#x60;, &#x60;selected&#x60;, or &#x60;private&#x60;. | [optional] 



## Enum: VisibilityEnum


* `selected` (value: `"selected"`)

* `all` (value: `"all"`)

* `private` (value: `"private"`)




