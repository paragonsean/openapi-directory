

# AppVersion

This represents a single version of the app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isProduction** | **Boolean** | True if this version is a production APK. |  [optional] |
|**targetSdkVersion** | **Integer** | The SDK version this app targets, as specified in the manifest of the APK. See http://developer.android.com/guide/topics/manifest/uses-sdk-element.html |  [optional] |
|**track** | [**TrackEnum**](#TrackEnum) | Deprecated, use trackId instead. |  [optional] |
|**trackId** | **List&lt;String&gt;** | Track ids that the app version is published in. Replaces the track field (deprecated), but doesn&#39;t include the production track (see isProduction instead). |  [optional] |
|**versionCode** | **Integer** | Unique increasing identifier for the app version. |  [optional] |
|**versionString** | **String** | The string used in the Play store by the app developer to identify the version. The string is not necessarily unique or localized (for example, the string could be \&quot;1.4\&quot;). |  [optional] |



## Enum: TrackEnum

| Name | Value |
|---- | -----|
| APP_TRACK_UNSPECIFIED | &quot;appTrackUnspecified&quot; |
| PRODUCTION | &quot;production&quot; |
| BETA | &quot;beta&quot; |
| ALPHA | &quot;alpha&quot; |



