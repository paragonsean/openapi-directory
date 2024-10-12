# ChecksApi.GoogleChecksReportV1alphaAnalyzeUploadRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appBinaryFileType** | **String** | Optional. The type of the uploaded app binary. If not provided, the server assumes APK file for Android and IPA file for iOS. | [optional] 
**codeReferenceId** | **String** | Optional. Git commit hash or changelist number associated with the upload. | [optional] 



## Enum: AppBinaryFileTypeEnum


* `APP_BINARY_FILE_TYPE_UNSPECIFIED` (value: `"APP_BINARY_FILE_TYPE_UNSPECIFIED"`)

* `ANDROID_APK` (value: `"ANDROID_APK"`)

* `ANDROID_AAB` (value: `"ANDROID_AAB"`)

* `IOS_IPA` (value: `"IOS_IPA"`)




