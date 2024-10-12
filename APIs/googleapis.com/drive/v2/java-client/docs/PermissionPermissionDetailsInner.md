

# PermissionPermissionDetailsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalRoles** | **List&lt;String&gt;** | Output only. Additional roles for this user. Only &#x60;commenter&#x60; is currently possible, though more may be supported in the future. |  [optional] |
|**inherited** | **Boolean** | Output only. Whether this permission is inherited. This field is always populated. This is an output-only field. |  [optional] |
|**inheritedFrom** | **String** | Output only. The ID of the item from which this permission is inherited. This is an output-only field. |  [optional] |
|**permissionType** | **String** | Output only. The permission type for this user. While new values may be added in future, the following are currently possible: * &#x60;file&#x60; * &#x60;member&#x60; |  [optional] |
|**role** | **String** | Output only. The primary role for this user. While new values may be added in the future, the following are currently possible: * &#x60;organizer&#x60; * &#x60;fileOrganizer&#x60; * &#x60;writer&#x60; * &#x60;reader&#x60; |  [optional] |



