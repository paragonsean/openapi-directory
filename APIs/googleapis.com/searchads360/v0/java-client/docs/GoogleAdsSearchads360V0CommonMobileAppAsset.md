

# GoogleAdsSearchads360V0CommonMobileAppAsset

An asset representing a mobile app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Required. A string that uniquely identifies a mobile application. It should just contain the platform native id, like \&quot;com.android.ebay\&quot; for Android or \&quot;12345689\&quot; for iOS. |  [optional] |
|**appStore** | [**AppStoreEnum**](#AppStoreEnum) | Required. The application store that distributes this specific app. |  [optional] |



## Enum: AppStoreEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| APPLE_APP_STORE | &quot;APPLE_APP_STORE&quot; |
| GOOGLE_APP_STORE | &quot;GOOGLE_APP_STORE&quot; |



