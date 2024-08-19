# AdMobApi.AppLinkedAppInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**androidAppStores** | **[String]** | Optional. The app store information for published Android apps. This field is only used for apps on the Android platform and will be ignored if the PLATFORM is set to iOS. The default value is the Google Play App store. This field can be updated after app is created. If the app is not published, this field will not be included in the response. | [optional] 
**appStoreId** | **String** | The app store ID of the app; present if and only if the app is linked to an app store. If the app is added to the Google Play store, it will be the application ID of the app. For example: \&quot;com.example.myapp\&quot;. See https://developer.android.com/studio/build/application-id. If the app is added to the Apple App Store, it will be app store ID. For example \&quot;105169111\&quot;. Note that setting the app store id is considered an irreversible action. Once an app is linked, it cannot be unlinked. | [optional] 
**displayName** | **String** | Output only. Display name of the app as it appears in the app store. This is an output-only field, and may be empty if the app cannot be found in the store. | [optional] [readonly] 



## Enum: [AndroidAppStoresEnum]


* `ANDROID_APP_STORE_UNSPECIFIED` (value: `"ANDROID_APP_STORE_UNSPECIFIED"`)

* `GOOGLE_PLAY_APP_STORE` (value: `"GOOGLE_PLAY_APP_STORE"`)

* `AMAZON_APP_STORE` (value: `"AMAZON_APP_STORE"`)

* `OPPO_APP_STORE` (value: `"OPPO_APP_STORE"`)

* `SAMSUNG_APP_STORE` (value: `"SAMSUNG_APP_STORE"`)

* `VIVO_APP_STORE` (value: `"VIVO_APP_STORE"`)

* `XIAOMI_APP_STORE` (value: `"XIAOMI_APP_STORE"`)




