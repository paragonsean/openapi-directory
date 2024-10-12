

# ProjectMembershipResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gid** | **String** | Globally unique identifier of the resource, as a string. |  [optional] [readonly] |
|**resourceType** | **String** | The base type of this resource. |  [optional] [readonly] |
|**user** | [**UserCompact**](UserCompact.md) |  |  [optional] |
|**project** | [**ProjectCompact**](ProjectCompact.md) |  |  [optional] |
|**writeAccess** | [**WriteAccessEnum**](#WriteAccessEnum) | Whether the user has full access to the project or has comment-only access. |  [optional] [readonly] |



## Enum: WriteAccessEnum

| Name | Value |
|---- | -----|
| FULL_WRITE | &quot;full_write&quot; |
| COMMENT_ONLY | &quot;comment_only&quot; |



