# GitHubV3RestApi.EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowsPublicRepositories** | **Boolean** | Whether the runner group can be used by &#x60;public&#x60; repositories. | [optional] [default to false]
**name** | **String** | Name of the runner group. | 
**runners** | **[Number]** | List of runner IDs to add to the runner group. | [optional] 
**selectedOrganizationIds** | **[Number]** | List of organization IDs that can access the runner group. | [optional] 
**visibility** | **String** | Visibility of a runner group. You can select all organizations or select individual organization. | [optional] 



## Enum: VisibilityEnum


* `selected` (value: `"selected"`)

* `all` (value: `"all"`)




