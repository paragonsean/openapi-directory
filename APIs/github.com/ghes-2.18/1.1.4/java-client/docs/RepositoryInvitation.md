

# RepositoryInvitation

Repository invitations let you manage who you collaborate with.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  |
|**expired** | **Boolean** | Whether or not the invitation has expired |  [optional] |
|**htmlUrl** | **String** |  |  |
|**id** | **Integer** | Unique identifier of the repository invitation. |  |
|**invitee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**inviter** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**nodeId** | **String** |  |  |
|**permissions** | [**PermissionsEnum**](#PermissionsEnum) | The permission associated with the invitation. |  |
|**repository** | [**MinimalRepository**](MinimalRepository.md) |  |  |
|**url** | **String** | URL for the repository invitation |  |



## Enum: PermissionsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |
| TRIAGE | &quot;triage&quot; |
| MAINTAIN | &quot;maintain&quot; |



