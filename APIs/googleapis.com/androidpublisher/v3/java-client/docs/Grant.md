

# Grant

An access grant resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appLevelPermissions** | [**List&lt;AppLevelPermissionsEnum&gt;**](#List&lt;AppLevelPermissionsEnum&gt;) | The permissions granted to the user for this app. |  [optional] |
|**name** | **String** | Required. Resource name for this grant, following the pattern \&quot;developers/{developer}/users/{email}/grants/{package_name}\&quot;. If this grant is for a draft app, the app ID will be used in this resource name instead of the package name. |  [optional] |
|**packageName** | **String** | Immutable. The package name of the app. This will be empty for draft apps. |  [optional] |



## Enum: List&lt;AppLevelPermissionsEnum&gt;

| Name | Value |
|---- | -----|
| APP_LEVEL_PERMISSION_UNSPECIFIED | &quot;APP_LEVEL_PERMISSION_UNSPECIFIED&quot; |
| CAN_ACCESS_APP | &quot;CAN_ACCESS_APP&quot; |
| CAN_VIEW_FINANCIAL_DATA | &quot;CAN_VIEW_FINANCIAL_DATA&quot; |
| CAN_MANAGE_PERMISSIONS | &quot;CAN_MANAGE_PERMISSIONS&quot; |
| CAN_REPLY_TO_REVIEWS | &quot;CAN_REPLY_TO_REVIEWS&quot; |
| CAN_MANAGE_PUBLIC_APKS | &quot;CAN_MANAGE_PUBLIC_APKS&quot; |
| CAN_MANAGE_TRACK_APKS | &quot;CAN_MANAGE_TRACK_APKS&quot; |
| CAN_MANAGE_TRACK_USERS | &quot;CAN_MANAGE_TRACK_USERS&quot; |
| CAN_MANAGE_PUBLIC_LISTING | &quot;CAN_MANAGE_PUBLIC_LISTING&quot; |
| CAN_MANAGE_DRAFT_APPS | &quot;CAN_MANAGE_DRAFT_APPS&quot; |
| CAN_MANAGE_ORDERS | &quot;CAN_MANAGE_ORDERS&quot; |
| CAN_MANAGE_APP_CONTENT | &quot;CAN_MANAGE_APP_CONTENT&quot; |
| CAN_VIEW_NON_FINANCIAL_DATA | &quot;CAN_VIEW_NON_FINANCIAL_DATA&quot; |
| CAN_VIEW_APP_QUALITY | &quot;CAN_VIEW_APP_QUALITY&quot; |



