# GitHubV3RestApi.EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowsPublicRepositories** | **Boolean** | Whether the runner group can be used by &#x60;public&#x60; repositories. | [optional] [default to false]
**name** | **String** | Name of the runner group. | [optional] 
**visibility** | **String** | Visibility of a runner group. You can select all organizations or select individual organizations. Can be one of: &#x60;all&#x60; or &#x60;selected&#x60; | [optional] [default to &#39;all&#39;]



## Enum: VisibilityEnum


* `selected` (value: `"selected"`)

* `all` (value: `"all"`)




