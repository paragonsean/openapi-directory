# AppCenterClient.UserProfileResponseInternal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatarUrl** | **String** | The avatar URL of the user | [optional] 
**canChangePassword** | **Boolean** | User is required to send an old password in order to change the password. | [optional] 
**displayName** | **String** | The full name of the user. Might for example be first and last name | 
**email** | **String** | The email address of the user | 
**id** | **String** | The unique id (UUID) of the user | 
**name** | **String** | The unique name that is used to identify the user. | 
**origin** | **String** | The creation origin of this user | 
**permissions** | **[String]** | The permissions the user has for the app | [optional] 
**adminRole** | **String** | The new admin_role | [optional] 
**featureFlags** | **[String]** | The feature flags that are enabled for this app | [optional] 
**settings** | [**UserProfileResponseInternalAllOfSettings**](UserProfileResponseInternalAllOfSettings.md) |  | [optional] 



## Enum: OriginEnum


* `appcenter` (value: `"appcenter"`)

* `hockeyapp` (value: `"hockeyapp"`)

* `codepush` (value: `"codepush"`)





## Enum: [PermissionsEnum]


* `manager` (value: `"manager"`)

* `developer` (value: `"developer"`)

* `viewer` (value: `"viewer"`)

* `tester` (value: `"tester"`)





## Enum: AdminRoleEnum


* `superAdmin` (value: `"superAdmin"`)

* `admin` (value: `"admin"`)

* `devOps` (value: `"devOps"`)

* `customerSupport` (value: `"customerSupport"`)

* `notAdmin` (value: `"notAdmin"`)




