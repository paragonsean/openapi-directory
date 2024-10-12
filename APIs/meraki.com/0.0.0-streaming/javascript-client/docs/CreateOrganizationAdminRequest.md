# MerakiDashboardApi.CreateOrganizationAdminRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationMethod** | **String** | The method of authentication the user will use to sign in to the Meraki dashboard. Can be one of &#39;Email&#39; or &#39;Cisco SecureX Sign-On&#39;. The default is Email authentication | [optional] 
**email** | **String** | The email of the dashboard administrator. This attribute can not be updated. | 
**name** | **String** | The name of the dashboard administrator | 
**networks** | [**[CreateOrganizationAdminRequestNetworksInner]**](CreateOrganizationAdminRequestNetworksInner.md) | The list of networks that the dashboard administrator has privileges on | [optional] 
**orgAccess** | **String** | The privilege of the dashboard administrator on the organization. Can be one of &#39;full&#39;, &#39;read-only&#39;, &#39;enterprise&#39; or &#39;none&#39; | 
**tags** | [**[CreateOrganizationAdminRequestTagsInner]**](CreateOrganizationAdminRequestTagsInner.md) | The list of tags that the dashboard administrator has privileges on | [optional] 



## Enum: AuthenticationMethodEnum


* `Cisco SecureX Sign-On` (value: `"Cisco SecureX Sign-On"`)

* `Email` (value: `"Email"`)





## Enum: OrgAccessEnum


* `enterprise` (value: `"enterprise"`)

* `full` (value: `"full"`)

* `none` (value: `"none"`)

* `read-only` (value: `"read-only"`)




