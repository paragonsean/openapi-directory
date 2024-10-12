

# User

A user resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessState** | [**AccessStateEnum**](#AccessStateEnum) | Output only. The state of the user&#39;s access to the Play Console. |  [optional] [readonly] |
|**developerAccountPermissions** | [**List&lt;DeveloperAccountPermissionsEnum&gt;**](#List&lt;DeveloperAccountPermissionsEnum&gt;) | Permissions for the user which apply across the developer account. |  [optional] |
|**email** | **String** | Immutable. The user&#39;s email address. |  [optional] |
|**expirationTime** | **String** | The time at which the user&#39;s access expires, if set. When setting this value, it must always be in the future. |  [optional] |
|**grants** | [**List&lt;Grant&gt;**](Grant.md) | Output only. Per-app permissions for the user. |  [optional] [readonly] |
|**name** | **String** | Required. Resource name for this user, following the pattern \&quot;developers/{developer}/users/{email}\&quot;. |  [optional] |
|**partial** | **Boolean** | Output only. Whether there are more permissions for the user that are not represented here. This can happen if the caller does not have permission to manage all apps in the account. This is also &#x60;true&#x60; if this user is the account owner. If this field is &#x60;true&#x60;, it should be taken as a signal that this user cannot be fully managed via the API. That is, the API caller is not be able to manage all of the permissions this user holds, either because it doesn&#39;t know about them or because the user is the account owner. |  [optional] [readonly] |



## Enum: AccessStateEnum

| Name | Value |
|---- | -----|
| ACCESS_STATE_UNSPECIFIED | &quot;ACCESS_STATE_UNSPECIFIED&quot; |
| INVITED | &quot;INVITED&quot; |
| INVITATION_EXPIRED | &quot;INVITATION_EXPIRED&quot; |
| ACCESS_GRANTED | &quot;ACCESS_GRANTED&quot; |
| ACCESS_EXPIRED | &quot;ACCESS_EXPIRED&quot; |



## Enum: List&lt;DeveloperAccountPermissionsEnum&gt;

| Name | Value |
|---- | -----|
| DEVELOPER_LEVEL_PERMISSION_UNSPECIFIED | &quot;DEVELOPER_LEVEL_PERMISSION_UNSPECIFIED&quot; |
| CAN_SEE_ALL_APPS | &quot;CAN_SEE_ALL_APPS&quot; |
| CAN_VIEW_FINANCIAL_DATA_GLOBAL | &quot;CAN_VIEW_FINANCIAL_DATA_GLOBAL&quot; |
| CAN_MANAGE_PERMISSIONS_GLOBAL | &quot;CAN_MANAGE_PERMISSIONS_GLOBAL&quot; |
| CAN_EDIT_GAMES_GLOBAL | &quot;CAN_EDIT_GAMES_GLOBAL&quot; |
| CAN_PUBLISH_GAMES_GLOBAL | &quot;CAN_PUBLISH_GAMES_GLOBAL&quot; |
| CAN_REPLY_TO_REVIEWS_GLOBAL | &quot;CAN_REPLY_TO_REVIEWS_GLOBAL&quot; |
| CAN_MANAGE_PUBLIC_APKS_GLOBAL | &quot;CAN_MANAGE_PUBLIC_APKS_GLOBAL&quot; |
| CAN_MANAGE_TRACK_APKS_GLOBAL | &quot;CAN_MANAGE_TRACK_APKS_GLOBAL&quot; |
| CAN_MANAGE_TRACK_USERS_GLOBAL | &quot;CAN_MANAGE_TRACK_USERS_GLOBAL&quot; |
| CAN_MANAGE_PUBLIC_LISTING_GLOBAL | &quot;CAN_MANAGE_PUBLIC_LISTING_GLOBAL&quot; |
| CAN_MANAGE_DRAFT_APPS_GLOBAL | &quot;CAN_MANAGE_DRAFT_APPS_GLOBAL&quot; |
| CAN_CREATE_MANAGED_PLAY_APPS_GLOBAL | &quot;CAN_CREATE_MANAGED_PLAY_APPS_GLOBAL&quot; |
| CAN_CHANGE_MANAGED_PLAY_SETTING_GLOBAL | &quot;CAN_CHANGE_MANAGED_PLAY_SETTING_GLOBAL&quot; |
| CAN_MANAGE_ORDERS_GLOBAL | &quot;CAN_MANAGE_ORDERS_GLOBAL&quot; |
| CAN_MANAGE_APP_CONTENT_GLOBAL | &quot;CAN_MANAGE_APP_CONTENT_GLOBAL&quot; |
| CAN_VIEW_NON_FINANCIAL_DATA_GLOBAL | &quot;CAN_VIEW_NON_FINANCIAL_DATA_GLOBAL&quot; |
| CAN_VIEW_APP_QUALITY_GLOBAL | &quot;CAN_VIEW_APP_QUALITY_GLOBAL&quot; |



