

# AppIntegrity

Contains the application integrity information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appRecognitionVerdict** | [**AppRecognitionVerdictEnum**](#AppRecognitionVerdictEnum) | Required. Details about the app recognition verdict |  [optional] |
|**certificateSha256Digest** | **List&lt;String&gt;** | The SHA256 hash of the requesting app&#39;s signing certificates (base64 web-safe encoded). Set iff app_recognition_verdict !&#x3D; UNEVALUATED. |  [optional] |
|**packageName** | **String** | Package name of the application under attestation. Set iff app_recognition_verdict !&#x3D; UNEVALUATED. |  [optional] |
|**versionCode** | **String** | Version code of the application. Set iff app_recognition_verdict !&#x3D; UNEVALUATED. |  [optional] |



## Enum: AppRecognitionVerdictEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| PLAY_RECOGNIZED | &quot;PLAY_RECOGNIZED&quot; |
| UNRECOGNIZED_VERSION | &quot;UNRECOGNIZED_VERSION&quot; |
| UNEVALUATED | &quot;UNEVALUATED&quot; |



