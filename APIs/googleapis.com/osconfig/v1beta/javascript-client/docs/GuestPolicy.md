# OsConfigApi.GuestPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | [**Assignment**](Assignment.md) |  | [optional] 
**createTime** | **String** | Output only. Time this guest policy was created. | [optional] [readonly] 
**description** | **String** | Description of the guest policy. Length of the description is limited to 1024 characters. | [optional] 
**etag** | **String** | The etag for this guest policy. If this is provided on update, it must match the server&#39;s etag. | [optional] 
**name** | **String** | Required. Unique name of the resource in this project using one of the following forms: &#x60;projects/{project_number}/guestPolicies/{guest_policy_id}&#x60;. | [optional] 
**packageRepositories** | [**[PackageRepository]**](PackageRepository.md) | A list of package repositories to configure on the VM instance. This is done before any other configs are applied so they can use these repos. Package repositories are only configured if the corresponding package manager(s) are available. | [optional] 
**packages** | [**[Package]**](Package.md) | The software packages to be managed by this policy. | [optional] 
**recipes** | [**[SoftwareRecipe]**](SoftwareRecipe.md) | A list of Recipes to install on the VM instance. | [optional] 
**updateTime** | **String** | Output only. Last time this guest policy was updated. | [optional] [readonly] 


