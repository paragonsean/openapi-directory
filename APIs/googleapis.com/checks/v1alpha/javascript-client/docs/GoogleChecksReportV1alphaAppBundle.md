# ChecksApi.GoogleChecksReportV1alphaAppBundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundleId** | **String** | Unique id of the bundle. For example: \&quot;com.google.Gmail\&quot;. | [optional] 
**codeReferenceId** | **String** | Git commit hash or changelist number associated with the release. | [optional] 
**releaseType** | **String** | Identifies the type of release. | [optional] 
**version** | **String** | The user-visible version of the bundle such as the Android &#x60;versionName&#x60; or iOS &#x60;CFBundleShortVersionString&#x60;. For example: \&quot;7.21.1\&quot;. | [optional] 
**versionId** | **String** | The version used throughout the operating system and store to identify the build such as the Android &#x60;versionCode&#x60; or iOS &#x60;CFBundleVersion&#x60;. | [optional] 



## Enum: ReleaseTypeEnum


* `APP_BUNDLE_RELEASE_TYPE_UNSPECIFIED` (value: `"APP_BUNDLE_RELEASE_TYPE_UNSPECIFIED"`)

* `PUBLIC` (value: `"PUBLIC"`)

* `PRE_RELEASE` (value: `"PRE_RELEASE"`)




