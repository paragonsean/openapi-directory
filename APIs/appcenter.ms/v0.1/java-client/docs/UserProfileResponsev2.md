

# UserProfileResponsev2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminRole** | [**AdminRoleEnum**](#AdminRoleEnum) | The new admin_role |  [optional] |
|**avatarUrl** | **String** | The avatar URL of the user |  [optional] |
|**canChangePassword** | **Boolean** | User is required to send an old password in order to change the password. |  [optional] |
|**createdAt** | **String** | The created date of the user |  [optional] |
|**displayName** | **String** | The full name of the user. Might for example be first and last name |  |
|**email** | **String** | The email address of the user |  |
|**featureFlags** | **List&lt;String&gt;** | The feature flags that are enabled for this user |  [optional] |
|**id** | **UUID** | The unique id (UUID) of the user |  |
|**name** | **String** | The unique name that is used to identify the user. |  |
|**nextNpsSurveyDate** | **String** | The date in the future when the user should be checked again for NPS eligibility |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this user |  |
|**sessionHash** | **String** | The session hash of the user |  [optional] |
|**settings** | **Object** | The user&#39;s settings |  [optional] |



## Enum: AdminRoleEnum

| Name | Value |
|---- | -----|
| SUPER_ADMIN | &quot;superAdmin&quot; |
| ADMIN | &quot;admin&quot; |
| DEV_OPS | &quot;devOps&quot; |
| CUSTOMER_SUPPORT | &quot;customerSupport&quot; |
| NOT_ADMIN | &quot;notAdmin&quot; |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |
| CODEPUSH | &quot;codepush&quot; |



