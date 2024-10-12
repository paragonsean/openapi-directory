# MerakiDashboardApi.CreateOrganizationSamlRoleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**networks** | [**[CreateOrganizationSamlRoleRequestNetworksInner]**](CreateOrganizationSamlRoleRequestNetworksInner.md) | The list of networks that the SAML administrator has privileges on | [optional] 
**orgAccess** | **String** | The privilege of the SAML administrator on the organization. Can be one of &#39;none&#39;, &#39;read-only&#39;, &#39;full&#39; or &#39;enterprise&#39; | 
**role** | **String** | The role of the SAML administrator | 
**tags** | [**[CreateOrganizationSamlRoleRequestTagsInner]**](CreateOrganizationSamlRoleRequestTagsInner.md) | The list of tags that the SAML administrator has privleges on | [optional] 



## Enum: OrgAccessEnum


* `enterprise` (value: `"enterprise"`)

* `full` (value: `"full"`)

* `none` (value: `"none"`)

* `read-only` (value: `"read-only"`)




