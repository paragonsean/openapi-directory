

# AppLinkedAppInfo

Information from the app store if the app is linked to an app store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidAppStores** | [**List&lt;AndroidAppStoresEnum&gt;**](#List&lt;AndroidAppStoresEnum&gt;) | Optional. The app store information for published Android apps. This field is only used for apps on the Android platform and will be ignored if the PLATFORM is set to iOS. The default value is the Google Play App store. This field can be updated after app is created. If the app is not published, this field will not be included in the response. |  [optional] |
|**appStoreId** | **String** | The app store ID of the app; present if and only if the app is linked to an app store. If the app is added to the Google Play store, it will be the application ID of the app. For example: \&quot;com.example.myapp\&quot;. See https://developer.android.com/studio/build/application-id. If the app is added to the Apple App Store, it will be app store ID. For example \&quot;105169111\&quot;. Note that setting the app store id is considered an irreversible action. Once an app is linked, it cannot be unlinked. |  [optional] |
|**displayName** | **String** | Output only. Display name of the app as it appears in the app store. This is an output-only field, and may be empty if the app cannot be found in the store. |  [optional] [readonly] |



## Enum: List&lt;AndroidAppStoresEnum&gt;

| Name | Value |
|---- | -----|
| ANDROID_APP_STORE_UNSPECIFIED | &quot;ANDROID_APP_STORE_UNSPECIFIED&quot; |
| GOOGLE_PLAY_APP_STORE | &quot;GOOGLE_PLAY_APP_STORE&quot; |
| AMAZON_APP_STORE | &quot;AMAZON_APP_STORE&quot; |
| OPPO_APP_STORE | &quot;OPPO_APP_STORE&quot; |
| SAMSUNG_APP_STORE | &quot;SAMSUNG_APP_STORE&quot; |
| VIVO_APP_STORE | &quot;VIVO_APP_STORE&quot; |
| XIAOMI_APP_STORE | &quot;XIAOMI_APP_STORE&quot; |



