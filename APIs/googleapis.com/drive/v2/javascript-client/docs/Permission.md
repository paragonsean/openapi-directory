# GoogleDriveApi.Permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalRoles** | **[String]** | Additional roles for this user. Only &#x60;commenter&#x60; is currently allowed, though more may be supported in the future. | [optional] 
**authKey** | **String** | Output only. Deprecated. | [optional] 
**deleted** | **Boolean** | Output only. Whether the account associated with this permission has been deleted. This field only pertains to user and group permissions. | [optional] 
**domain** | **String** | Output only. The domain name of the entity this permission refers to. This is an output-only field which is present when the permission type is &#x60;user&#x60;, &#x60;group&#x60; or &#x60;domain&#x60;. | [optional] 
**emailAddress** | **String** | Output only. The email address of the user or group this permission refers to. This is an output-only field which is present when the permission type is &#x60;user&#x60; or &#x60;group&#x60;. | [optional] 
**etag** | **String** | Output only. The ETag of the permission. | [optional] 
**expirationDate** | **Date** | The time at which this permission will expire (RFC 3339 date-time). Expiration dates have the following restrictions: - They can only be set on user and group permissions - The date must be in the future - The date cannot be more than a year in the future - The date can only be set on drive.permissions.update or drive.permissions.patch requests | [optional] 
**id** | **String** | The ID of the user this permission refers to, and identical to the &#x60;permissionId&#x60; in the About and Files resources. When making a &#x60;drive.permissions.insert&#x60; request, exactly one of the &#x60;id&#x60; or &#x60;value&#x60; fields must be specified unless the permission type is &#x60;anyone&#x60;, in which case both &#x60;id&#x60; and &#x60;value&#x60; are ignored. | [optional] 
**kind** | **String** | Output only. This is always &#x60;drive#permission&#x60;. | [optional] [default to &#39;drive#permission&#39;]
**name** | **String** | Output only. The name for this permission. | [optional] 
**pendingOwner** | **Boolean** | Whether the account associated with this permission is a pending owner. Only populated for &#x60;user&#x60; type permissions for files that are not in a shared drive. | [optional] 
**permissionDetails** | [**[PermissionPermissionDetailsInner]**](PermissionPermissionDetailsInner.md) | Output only. Details of whether the permissions on this shared drive item are inherited or directly on this item. This is an output-only field which is present only for shared drive items. | [optional] [readonly] 
**photoLink** | **String** | Output only. A link to the profile photo, if available. | [optional] 
**role** | **String** | The primary role for this user. While new values may be supported in the future, the following are currently allowed: * &#x60;owner&#x60; * &#x60;organizer&#x60; * &#x60;fileOrganizer&#x60; * &#x60;writer&#x60; * &#x60;reader&#x60; | [optional] 
**selfLink** | **String** | Output only. A link back to this permission. | [optional] 
**teamDrivePermissionDetails** | [**[PermissionTeamDrivePermissionDetailsInner]**](PermissionTeamDrivePermissionDetailsInner.md) | Output only. Deprecated: Use &#x60;permissionDetails&#x60; instead. | [optional] [readonly] 
**type** | **String** | The account type. Allowed values are: * &#x60;user&#x60; * &#x60;group&#x60; * &#x60;domain&#x60; * &#x60;anyone&#x60; | [optional] 
**value** | **String** | The email address or domain name for the entity. This is used during inserts and is not populated in responses. When making a &#x60;drive.permissions.insert&#x60; request, exactly one of the &#x60;id&#x60; or &#x60;value&#x60; fields must be specified unless the permission type is &#x60;anyone&#x60;, in which case both &#x60;id&#x60; and &#x60;value&#x60; are ignored. | [optional] 
**view** | **String** | Indicates the view for this permission. Only populated for permissions that belong to a view. &#x60;published&#x60; is the only supported value. | [optional] 
**withLink** | **Boolean** | Whether the link is required for this permission. | [optional] 


