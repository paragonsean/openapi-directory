

# App

Describes an AdMob app for a specific platform (For example: Android or iOS).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appApprovalState** | [**AppApprovalStateEnum**](#AppApprovalStateEnum) | Output only. The approval state for the app. The field is read-only. |  [optional] [readonly] |
|**appId** | **String** | The externally visible ID of the app which can be used to integrate with the AdMob SDK. This is a read only property. Example: ca-app-pub-9876543210987654~0123456789 |  [optional] |
|**linkedAppInfo** | [**AppLinkedAppInfo**](AppLinkedAppInfo.md) |  |  [optional] |
|**manualAppInfo** | [**AppManualAppInfo**](AppManualAppInfo.md) |  |  [optional] |
|**name** | **String** | Resource name for this app. Format is accounts/{publisher_id}/apps/{app_id_fragment} Example: accounts/pub-9876543210987654/apps/0123456789 |  [optional] |
|**platform** | **String** | Describes the platform of the app. Limited to \&quot;IOS\&quot; and \&quot;ANDROID\&quot;. |  [optional] |



## Enum: AppApprovalStateEnum

| Name | Value |
|---- | -----|
| APP_APPROVAL_STATE_UNSPECIFIED | &quot;APP_APPROVAL_STATE_UNSPECIFIED&quot; |
| ACTION_REQUIRED | &quot;ACTION_REQUIRED&quot; |
| IN_REVIEW | &quot;IN_REVIEW&quot; |
| APPROVED | &quot;APPROVED&quot; |



