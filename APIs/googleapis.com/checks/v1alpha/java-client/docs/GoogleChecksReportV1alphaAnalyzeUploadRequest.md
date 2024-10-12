

# GoogleChecksReportV1alphaAnalyzeUploadRequest

The request message for ReportService.AnalyzeUpload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appBinaryFileType** | [**AppBinaryFileTypeEnum**](#AppBinaryFileTypeEnum) | Optional. The type of the uploaded app binary. If not provided, the server assumes APK file for Android and IPA file for iOS. |  [optional] |
|**codeReferenceId** | **String** | Optional. Git commit hash or changelist number associated with the upload. |  [optional] |



## Enum: AppBinaryFileTypeEnum

| Name | Value |
|---- | -----|
| APP_BINARY_FILE_TYPE_UNSPECIFIED | &quot;APP_BINARY_FILE_TYPE_UNSPECIFIED&quot; |
| ANDROID_APK | &quot;ANDROID_APK&quot; |
| ANDROID_AAB | &quot;ANDROID_AAB&quot; |
| IOS_IPA | &quot;IOS_IPA&quot; |



