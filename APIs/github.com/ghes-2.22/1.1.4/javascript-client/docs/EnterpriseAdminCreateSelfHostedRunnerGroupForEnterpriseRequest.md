# GitHubV3RestApi.EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of the runner group. | 
**runners** | **[Number]** | List of runner IDs to add to the runner group. | [optional] 
**selectedOrganizationIds** | **[Number]** | List of organization IDs that can access the runner group. | [optional] 
**visibility** | **String** | Visibility of a runner group. You can select all organizations or select individual organization. Can be one of: &#x60;all&#x60; or &#x60;selected&#x60; | [optional] 



## Enum: VisibilityEnum


* `selected` (value: `"selected"`)

* `all` (value: `"all"`)




