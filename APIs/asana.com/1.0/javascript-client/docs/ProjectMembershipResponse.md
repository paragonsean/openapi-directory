# Asana.ProjectMembershipResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 
**project** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**writeAccess** | **String** | Whether the user has full access to the project or has comment-only access. | [optional] [readonly] 



## Enum: WriteAccessEnum


* `full_write` (value: `"full_write"`)

* `comment_only` (value: `"comment_only"`)




