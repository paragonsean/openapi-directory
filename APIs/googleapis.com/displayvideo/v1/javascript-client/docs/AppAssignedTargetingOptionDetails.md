# DisplayVideo360Api.AppAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | Required. The ID of the app. Android&#39;s Play store app uses bundle ID, for example &#x60;com.google.android.gm&#x60;. Apple&#39;s App store app ID uses 9 digit string, for example &#x60;422689480&#x60;. | [optional] 
**appPlatform** | **String** | Indicates the platform of the targeted app. If this field is not specified, the app platform will be assumed to be mobile (i.e., Android or iOS), and we will derive the appropriate mobile platform from the app ID. | [optional] 
**displayName** | **String** | Output only. The display name of the app. | [optional] [readonly] 
**negative** | **Boolean** | Indicates if this option is being negatively targeted. | [optional] 



## Enum: AppPlatformEnum


* `UNSPECIFIED` (value: `"APP_PLATFORM_UNSPECIFIED"`)

* `IOS` (value: `"APP_PLATFORM_IOS"`)

* `ANDROID` (value: `"APP_PLATFORM_ANDROID"`)

* `ROKU` (value: `"APP_PLATFORM_ROKU"`)

* `AMAZON_FIRETV` (value: `"APP_PLATFORM_AMAZON_FIRETV"`)

* `PLAYSTATION` (value: `"APP_PLATFORM_PLAYSTATION"`)

* `APPLE_TV` (value: `"APP_PLATFORM_APPLE_TV"`)

* `XBOX` (value: `"APP_PLATFORM_XBOX"`)

* `SAMSUNG_TV` (value: `"APP_PLATFORM_SAMSUNG_TV"`)

* `ANDROID_TV` (value: `"APP_PLATFORM_ANDROID_TV"`)

* `GENERIC_CTV` (value: `"APP_PLATFORM_GENERIC_CTV"`)




