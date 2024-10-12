# DataLakeAnalyticsCatalogManagementClient.Acl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aceType** | **String** | the access control list (ACL) entry type. UserObj and GroupObj denote the owning user and group, respectively. | [optional] [readonly] 
**permission** | **String** | the permission type of the access control list (ACL) entry. | [optional] [readonly] 
**principalId** | **String** | the Azure AD object ID of the user or group being specified in the access control list (ACL) entry. | [optional] [readonly] 



## Enum: AceTypeEnum


* `UserObj` (value: `"UserObj"`)

* `GroupObj` (value: `"GroupObj"`)

* `Other` (value: `"Other"`)

* `User` (value: `"User"`)

* `Group` (value: `"Group"`)





## Enum: PermissionEnum


* `None` (value: `"None"`)

* `Use` (value: `"Use"`)

* `Create` (value: `"Create"`)

* `Drop` (value: `"Drop"`)

* `Alter` (value: `"Alter"`)

* `Write` (value: `"Write"`)

* `All` (value: `"All"`)




