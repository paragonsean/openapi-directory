

# UserProfileResponseInternal


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avatarUrl** | **String** | The avatar URL of the user |  [optional] |
|**canChangePassword** | **Boolean** | User is required to send an old password in order to change the password. |  [optional] |
|**displayName** | **String** | The full name of the user. Might for example be first and last name |  |
|**email** | **String** | The email address of the user |  |
|**id** | **UUID** | The unique id (UUID) of the user |  |
|**name** | **String** | The unique name that is used to identify the user. |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this user |  |
|**permissions** | [**List&lt;PermissionsEnum&gt;**](#List&lt;PermissionsEnum&gt;) | The permissions the user has for the app |  [optional] |
|**adminRole** | [**AdminRoleEnum**](#AdminRoleEnum) | The new admin_role |  [optional] |
|**featureFlags** | **List&lt;String&gt;** | The feature flags that are enabled for this app |  [optional] |
|**settings** | [**UserProfileResponseInternalAllOfSettings**](UserProfileResponseInternalAllOfSettings.md) |  |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |
| CODEPUSH | &quot;codepush&quot; |



## Enum: List&lt;PermissionsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGER | &quot;manager&quot; |
| DEVELOPER | &quot;developer&quot; |
| VIEWER | &quot;viewer&quot; |
| TESTER | &quot;tester&quot; |



## Enum: AdminRoleEnum

| Name | Value |
|---- | -----|
| SUPER_ADMIN | &quot;superAdmin&quot; |
| ADMIN | &quot;admin&quot; |
| DEV_OPS | &quot;devOps&quot; |
| CUSTOMER_SUPPORT | &quot;customerSupport&quot; |
| NOT_ADMIN | &quot;notAdmin&quot; |



