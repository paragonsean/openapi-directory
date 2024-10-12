

# RepositoryGroupPermission

A group's permission for a given repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**group** | [**Group**](Group.md) |  |  [optional] |
|**links** | [**RepositoryGroupPermissionLinks**](RepositoryGroupPermissionLinks.md) |  |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) |  |  [optional] |
|**repository** | [**Repository**](Repository.md) |  |  [optional] |
|**type** | **String** |  |  |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |
| NONE | &quot;none&quot; |



