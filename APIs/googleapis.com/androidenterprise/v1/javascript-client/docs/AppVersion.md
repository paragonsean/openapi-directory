# GooglePlayEmmApi.AppVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isProduction** | **Boolean** | True if this version is a production APK. | [optional] 
**targetSdkVersion** | **Number** | The SDK version this app targets, as specified in the manifest of the APK. See http://developer.android.com/guide/topics/manifest/uses-sdk-element.html | [optional] 
**track** | **String** | Deprecated, use trackId instead. | [optional] 
**trackId** | **[String]** | Track ids that the app version is published in. Replaces the track field (deprecated), but doesn&#39;t include the production track (see isProduction instead). | [optional] 
**versionCode** | **Number** | Unique increasing identifier for the app version. | [optional] 
**versionString** | **String** | The string used in the Play store by the app developer to identify the version. The string is not necessarily unique or localized (for example, the string could be \&quot;1.4\&quot;). | [optional] 



## Enum: TrackEnum


* `appTrackUnspecified` (value: `"appTrackUnspecified"`)

* `production` (value: `"production"`)

* `beta` (value: `"beta"`)

* `alpha` (value: `"alpha"`)




