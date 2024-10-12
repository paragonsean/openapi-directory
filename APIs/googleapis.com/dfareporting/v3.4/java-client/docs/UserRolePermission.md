

# UserRolePermission

Contains properties of a user role permission.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**AvailabilityEnum**](#AvailabilityEnum) | Levels of availability for a user role permission. |  [optional] |
|**id** | **String** | ID of this user role permission. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#userRolePermission\&quot;. |  [optional] |
|**name** | **String** | Name of this user role permission. |  [optional] |
|**permissionGroupId** | **String** | ID of the permission group that this user role permission belongs to. |  [optional] |



## Enum: AvailabilityEnum

| Name | Value |
|---- | -----|
| NOT_AVAILABLE_BY_DEFAULT | &quot;NOT_AVAILABLE_BY_DEFAULT&quot; |
| ACCOUNT_BY_DEFAULT | &quot;ACCOUNT_BY_DEFAULT&quot; |
| SUBACCOUNT_AND_ACCOUNT_BY_DEFAULT | &quot;SUBACCOUNT_AND_ACCOUNT_BY_DEFAULT&quot; |
| ACCOUNT_ALWAYS | &quot;ACCOUNT_ALWAYS&quot; |
| SUBACCOUNT_AND_ACCOUNT_ALWAYS | &quot;SUBACCOUNT_AND_ACCOUNT_ALWAYS&quot; |
| USER_PROFILE_ONLY | &quot;USER_PROFILE_ONLY&quot; |



