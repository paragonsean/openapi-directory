

# ApkManifest

An Android app manifest. See http://developer.android.com/guide/topics/manifest/manifest-intro.html

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationLabel** | **String** | User-readable name for the application. |  [optional] |
|**intentFilters** | [**List&lt;IntentFilter&gt;**](IntentFilter.md) |  |  [optional] |
|**maxSdkVersion** | **Integer** | Maximum API level on which the application is designed to run. |  [optional] |
|**metadata** | [**List&lt;Metadata&gt;**](Metadata.md) | Meta-data tags defined in the manifest. |  [optional] |
|**minSdkVersion** | **Integer** | Minimum API level required for the application to run. |  [optional] |
|**packageName** | **String** | Full Java-style package name for this application, e.g. \&quot;com.example.foo\&quot;. |  [optional] |
|**services** | [**List&lt;Service&gt;**](Service.md) | Services contained in the tag. |  [optional] |
|**targetSdkVersion** | **Integer** | Specifies the API Level on which the application is designed to run. |  [optional] |
|**usesFeature** | [**List&lt;UsesFeature&gt;**](UsesFeature.md) | Feature usage tags defined in the manifest. |  [optional] |
|**usesPermission** | **List&lt;String&gt;** | Permissions declared to be used by the application |  [optional] |
|**versionCode** | **String** | Version number used internally by the app. |  [optional] |
|**versionName** | **String** | Version number shown to users. |  [optional] |



