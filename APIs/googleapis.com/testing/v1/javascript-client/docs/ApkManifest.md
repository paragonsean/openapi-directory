# CloudTestingApi.ApkManifest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationLabel** | **String** | User-readable name for the application. | [optional] 
**intentFilters** | [**[IntentFilter]**](IntentFilter.md) |  | [optional] 
**maxSdkVersion** | **Number** | Maximum API level on which the application is designed to run. | [optional] 
**metadata** | [**[Metadata]**](Metadata.md) | Meta-data tags defined in the manifest. | [optional] 
**minSdkVersion** | **Number** | Minimum API level required for the application to run. | [optional] 
**packageName** | **String** | Full Java-style package name for this application, e.g. \&quot;com.example.foo\&quot;. | [optional] 
**services** | [**[Service]**](Service.md) | Services contained in the tag. | [optional] 
**targetSdkVersion** | **Number** | Specifies the API Level on which the application is designed to run. | [optional] 
**usesFeature** | [**[UsesFeature]**](UsesFeature.md) | Feature usage tags defined in the manifest. | [optional] 
**usesPermission** | **[String]** | Permissions declared to be used by the application | [optional] 
**versionCode** | **String** | Version number used internally by the app. | [optional] 
**versionName** | **String** | Version number shown to users. | [optional] 


