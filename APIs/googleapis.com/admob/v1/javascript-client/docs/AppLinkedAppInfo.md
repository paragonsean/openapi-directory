# AdMobApi.AppLinkedAppInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appStoreId** | **String** | The app store ID of the app; present if and only if the app is linked to an app store. If the app is added to the Google Play store, it will be the application ID of the app. For example: \&quot;com.example.myapp\&quot;. See https://developer.android.com/studio/build/application-id. If the app is added to the Apple App Store, it will be app store ID. For example \&quot;105169111\&quot;. Note that setting the app store id is considered an irreversible action. Once an app is linked, it cannot be unlinked. | [optional] 
**displayName** | **String** | Output only. Display name of the app as it appears in the app store. This is an output-only field, and may be empty if the app cannot be found in the store. | [optional] [readonly] 


