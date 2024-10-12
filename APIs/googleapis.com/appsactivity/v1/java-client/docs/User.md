

# User

A representation of a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isDeleted** | **Boolean** | A boolean which indicates whether the specified User was deleted. If true, name, photo and permission_id will be omitted. |  [optional] |
|**isMe** | **Boolean** | Whether the user is the authenticated user. |  [optional] |
|**name** | **String** | The displayable name of the user. |  [optional] |
|**permissionId** | **String** | The permission ID associated with this user. Equivalent to the Drive API&#39;s permission ID for this user, returned as part of the Drive Permissions resource. |  [optional] |
|**photo** | [**Photo**](Photo.md) |  |  [optional] |



