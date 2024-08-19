# GitHubV3RestApi.RepositoryInvitation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | 
**expired** | **Boolean** | Whether or not the invitation has expired | [optional] 
**htmlUrl** | **String** |  | 
**id** | **Number** | Unique identifier of the repository invitation. | 
**invitee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**inviter** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**nodeId** | **String** |  | 
**permissions** | **String** | The permission associated with the invitation. | 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | 
**url** | **String** | URL for the repository invitation | 



## Enum: PermissionsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)

* `admin` (value: `"admin"`)

* `triage` (value: `"triage"`)

* `maintain` (value: `"maintain"`)




