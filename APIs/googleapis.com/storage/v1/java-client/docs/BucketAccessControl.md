

# BucketAccessControl

An access-control entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucket** | **String** | The name of the bucket. |  [optional] |
|**domain** | **String** | The domain associated with the entity, if any. |  [optional] |
|**email** | **String** | The email address associated with the entity, if any. |  [optional] |
|**entity** | **String** | The entity holding the permission, in one of the following forms:  - user-userId  - user-email  - group-groupId  - group-email  - domain-domain  - project-team-projectId  - allUsers  - allAuthenticatedUsers Examples:  - The user liz@example.com would be user-liz@example.com.  - The group example@googlegroups.com would be group-example@googlegroups.com.  - To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com. |  [optional] |
|**entityId** | **String** | The ID for the entity, if any. |  [optional] |
|**etag** | **String** | HTTP 1.1 Entity tag for the access-control entry. |  [optional] |
|**id** | **String** | The ID of the access-control entry. |  [optional] |
|**kind** | **String** | The kind of item this is. For bucket access control entries, this is always storage#bucketAccessControl. |  [optional] |
|**projectTeam** | [**BucketAccessControlProjectTeam**](BucketAccessControlProjectTeam.md) |  |  [optional] |
|**role** | **String** | The access permission for the entity. |  [optional] |
|**selfLink** | **String** | The link to this access-control entry. |  [optional] |



