# MerakiDashboardApi.UpdateOrganizationAdminRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the dashboard administrator | [optional] 
**networks** | [**[CreateOrganizationAdminRequestNetworksInner]**](CreateOrganizationAdminRequestNetworksInner.md) | The list of networks that the dashboard administrator has privileges on | [optional] 
**orgAccess** | **String** | The privilege of the dashboard administrator on the organization. Can be one of &#39;full&#39;, &#39;read-only&#39;, &#39;enterprise&#39; or &#39;none&#39; | [optional] 
**tags** | [**[CreateOrganizationAdminRequestTagsInner]**](CreateOrganizationAdminRequestTagsInner.md) | The list of tags that the dashboard administrator has privileges on | [optional] 



## Enum: OrgAccessEnum


* `enterprise` (value: `"enterprise"`)

* `full` (value: `"full"`)

* `none` (value: `"none"`)

* `read-only` (value: `"read-only"`)




