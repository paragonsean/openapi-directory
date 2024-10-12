

# RepositoryUserPermission

A user's direct permission for a given repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**RepositoryGroupPermissionLinks**](RepositoryGroupPermissionLinks.md) |  |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) |  |  [optional] |
|**repository** | [**Repository**](Repository.md) |  |  [optional] |
|**type** | **String** |  |  |
|**user** | [**User**](User.md) |  |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |
| NONE | &quot;none&quot; |



