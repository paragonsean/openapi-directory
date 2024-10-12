

# GuestPolicy

An OS Config resource representing a guest configuration policy. These policies represent the desired state for VM instance guest environments including packages to install or remove, package repository configurations, and software to install.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignment** | [**Assignment**](Assignment.md) |  |  [optional] |
|**createTime** | **String** | Output only. Time this guest policy was created. |  [optional] [readonly] |
|**description** | **String** | Description of the guest policy. Length of the description is limited to 1024 characters. |  [optional] |
|**etag** | **String** | The etag for this guest policy. If this is provided on update, it must match the server&#39;s etag. |  [optional] |
|**name** | **String** | Required. Unique name of the resource in this project using one of the following forms: &#x60;projects/{project_number}/guestPolicies/{guest_policy_id}&#x60;. |  [optional] |
|**packageRepositories** | [**List&lt;PackageRepository&gt;**](PackageRepository.md) | A list of package repositories to configure on the VM instance. This is done before any other configs are applied so they can use these repos. Package repositories are only configured if the corresponding package manager(s) are available. |  [optional] |
|**packages** | [**List&lt;ModelPackage&gt;**](ModelPackage.md) | The software packages to be managed by this policy. |  [optional] |
|**recipes** | [**List&lt;SoftwareRecipe&gt;**](SoftwareRecipe.md) | A list of Recipes to install on the VM instance. |  [optional] |
|**updateTime** | **String** | Output only. Last time this guest policy was updated. |  [optional] [readonly] |



