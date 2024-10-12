# AppCenterClient.UserProfileResponsev2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminRole** | **String** | The new admin_role | [optional] 
**avatarUrl** | **String** | The avatar URL of the user | [optional] 
**canChangePassword** | **Boolean** | User is required to send an old password in order to change the password. | [optional] 
**createdAt** | **String** | The created date of the user | [optional] 
**displayName** | **String** | The full name of the user. Might for example be first and last name | 
**email** | **String** | The email address of the user | 
**featureFlags** | **[String]** | The feature flags that are enabled for this user | [optional] 
**id** | **String** | The unique id (UUID) of the user | 
**name** | **String** | The unique name that is used to identify the user. | 
**nextNpsSurveyDate** | **String** | The date in the future when the user should be checked again for NPS eligibility | [optional] 
**origin** | **String** | The creation origin of this user | 
**sessionHash** | **String** | The session hash of the user | [optional] 
**settings** | **Object** | The user&#39;s settings | [optional] 



## Enum: AdminRoleEnum


* `superAdmin` (value: `"superAdmin"`)

* `admin` (value: `"admin"`)

* `devOps` (value: `"devOps"`)

* `customerSupport` (value: `"customerSupport"`)

* `notAdmin` (value: `"notAdmin"`)





## Enum: OriginEnum


* `appcenter` (value: `"appcenter"`)

* `hockeyapp` (value: `"hockeyapp"`)

* `codepush` (value: `"codepush"`)




