# GooglePlayAndroidDeveloperApi.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessState** | **String** | Output only. The state of the user&#39;s access to the Play Console. | [optional] [readonly] 
**developerAccountPermissions** | **[String]** | Permissions for the user which apply across the developer account. | [optional] 
**email** | **String** | Immutable. The user&#39;s email address. | [optional] 
**expirationTime** | **String** | The time at which the user&#39;s access expires, if set. When setting this value, it must always be in the future. | [optional] 
**grants** | [**[Grant]**](Grant.md) | Output only. Per-app permissions for the user. | [optional] [readonly] 
**name** | **String** | Required. Resource name for this user, following the pattern \&quot;developers/{developer}/users/{email}\&quot;. | [optional] 
**partial** | **Boolean** | Output only. Whether there are more permissions for the user that are not represented here. This can happen if the caller does not have permission to manage all apps in the account. This is also &#x60;true&#x60; if this user is the account owner. If this field is &#x60;true&#x60;, it should be taken as a signal that this user cannot be fully managed via the API. That is, the API caller is not be able to manage all of the permissions this user holds, either because it doesn&#39;t know about them or because the user is the account owner. | [optional] [readonly] 



## Enum: AccessStateEnum


* `ACCESS_STATE_UNSPECIFIED` (value: `"ACCESS_STATE_UNSPECIFIED"`)

* `INVITED` (value: `"INVITED"`)

* `INVITATION_EXPIRED` (value: `"INVITATION_EXPIRED"`)

* `ACCESS_GRANTED` (value: `"ACCESS_GRANTED"`)

* `ACCESS_EXPIRED` (value: `"ACCESS_EXPIRED"`)





## Enum: [DeveloperAccountPermissionsEnum]


* `DEVELOPER_LEVEL_PERMISSION_UNSPECIFIED` (value: `"DEVELOPER_LEVEL_PERMISSION_UNSPECIFIED"`)

* `CAN_SEE_ALL_APPS` (value: `"CAN_SEE_ALL_APPS"`)

* `CAN_VIEW_FINANCIAL_DATA_GLOBAL` (value: `"CAN_VIEW_FINANCIAL_DATA_GLOBAL"`)

* `CAN_MANAGE_PERMISSIONS_GLOBAL` (value: `"CAN_MANAGE_PERMISSIONS_GLOBAL"`)

* `CAN_EDIT_GAMES_GLOBAL` (value: `"CAN_EDIT_GAMES_GLOBAL"`)

* `CAN_PUBLISH_GAMES_GLOBAL` (value: `"CAN_PUBLISH_GAMES_GLOBAL"`)

* `CAN_REPLY_TO_REVIEWS_GLOBAL` (value: `"CAN_REPLY_TO_REVIEWS_GLOBAL"`)

* `CAN_MANAGE_PUBLIC_APKS_GLOBAL` (value: `"CAN_MANAGE_PUBLIC_APKS_GLOBAL"`)

* `CAN_MANAGE_TRACK_APKS_GLOBAL` (value: `"CAN_MANAGE_TRACK_APKS_GLOBAL"`)

* `CAN_MANAGE_TRACK_USERS_GLOBAL` (value: `"CAN_MANAGE_TRACK_USERS_GLOBAL"`)

* `CAN_MANAGE_PUBLIC_LISTING_GLOBAL` (value: `"CAN_MANAGE_PUBLIC_LISTING_GLOBAL"`)

* `CAN_MANAGE_DRAFT_APPS_GLOBAL` (value: `"CAN_MANAGE_DRAFT_APPS_GLOBAL"`)

* `CAN_CREATE_MANAGED_PLAY_APPS_GLOBAL` (value: `"CAN_CREATE_MANAGED_PLAY_APPS_GLOBAL"`)

* `CAN_CHANGE_MANAGED_PLAY_SETTING_GLOBAL` (value: `"CAN_CHANGE_MANAGED_PLAY_SETTING_GLOBAL"`)

* `CAN_MANAGE_ORDERS_GLOBAL` (value: `"CAN_MANAGE_ORDERS_GLOBAL"`)

* `CAN_MANAGE_APP_CONTENT_GLOBAL` (value: `"CAN_MANAGE_APP_CONTENT_GLOBAL"`)

* `CAN_VIEW_NON_FINANCIAL_DATA_GLOBAL` (value: `"CAN_VIEW_NON_FINANCIAL_DATA_GLOBAL"`)

* `CAN_VIEW_APP_QUALITY_GLOBAL` (value: `"CAN_VIEW_APP_QUALITY_GLOBAL"`)




