

# User

A single user in Display & Video 360.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignedUserRoles** | [**List&lt;AssignedUserRole&gt;**](AssignedUserRole.md) | The assigned user roles. Required in CreateUser. Output only in UpdateUser. Can only be updated through BulkEditAssignedUserRoles. |  [optional] |
|**displayName** | **String** | Required. The display name of the user. Must be UTF-8 encoded with a maximum size of 240 bytes. |  [optional] |
|**email** | **String** | Required. Immutable. The email address used to identify the user. |  [optional] |
|**lastLoginTime** | **String** | Output only. The timestamp when the user last logged in DV360 UI. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the user. |  [optional] [readonly] |
|**userId** | **String** | Output only. The unique ID of the user. Assigned by the system. |  [optional] [readonly] |



