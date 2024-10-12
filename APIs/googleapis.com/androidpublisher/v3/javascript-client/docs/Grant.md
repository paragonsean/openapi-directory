# GooglePlayAndroidDeveloperApi.Grant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appLevelPermissions** | **[String]** | The permissions granted to the user for this app. | [optional] 
**name** | **String** | Required. Resource name for this grant, following the pattern \&quot;developers/{developer}/users/{email}/grants/{package_name}\&quot;. If this grant is for a draft app, the app ID will be used in this resource name instead of the package name. | [optional] 
**packageName** | **String** | Immutable. The package name of the app. This will be empty for draft apps. | [optional] 



## Enum: [AppLevelPermissionsEnum]


* `APP_LEVEL_PERMISSION_UNSPECIFIED` (value: `"APP_LEVEL_PERMISSION_UNSPECIFIED"`)

* `CAN_ACCESS_APP` (value: `"CAN_ACCESS_APP"`)

* `CAN_VIEW_FINANCIAL_DATA` (value: `"CAN_VIEW_FINANCIAL_DATA"`)

* `CAN_MANAGE_PERMISSIONS` (value: `"CAN_MANAGE_PERMISSIONS"`)

* `CAN_REPLY_TO_REVIEWS` (value: `"CAN_REPLY_TO_REVIEWS"`)

* `CAN_MANAGE_PUBLIC_APKS` (value: `"CAN_MANAGE_PUBLIC_APKS"`)

* `CAN_MANAGE_TRACK_APKS` (value: `"CAN_MANAGE_TRACK_APKS"`)

* `CAN_MANAGE_TRACK_USERS` (value: `"CAN_MANAGE_TRACK_USERS"`)

* `CAN_MANAGE_PUBLIC_LISTING` (value: `"CAN_MANAGE_PUBLIC_LISTING"`)

* `CAN_MANAGE_DRAFT_APPS` (value: `"CAN_MANAGE_DRAFT_APPS"`)

* `CAN_MANAGE_ORDERS` (value: `"CAN_MANAGE_ORDERS"`)

* `CAN_MANAGE_APP_CONTENT` (value: `"CAN_MANAGE_APP_CONTENT"`)

* `CAN_VIEW_NON_FINANCIAL_DATA` (value: `"CAN_VIEW_NON_FINANCIAL_DATA"`)

* `CAN_VIEW_APP_QUALITY` (value: `"CAN_VIEW_APP_QUALITY"`)




