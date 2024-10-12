# GooglePlayIntegrityApi.AppIntegrity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appRecognitionVerdict** | **String** | Required. Details about the app recognition verdict | [optional] 
**certificateSha256Digest** | **[String]** | The SHA256 hash of the requesting app&#39;s signing certificates (base64 web-safe encoded). Set iff app_recognition_verdict !&#x3D; UNEVALUATED. | [optional] 
**packageName** | **String** | Package name of the application under attestation. Set iff app_recognition_verdict !&#x3D; UNEVALUATED. | [optional] 
**versionCode** | **String** | Version code of the application. Set iff app_recognition_verdict !&#x3D; UNEVALUATED. | [optional] 



## Enum: AppRecognitionVerdictEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `PLAY_RECOGNIZED` (value: `"PLAY_RECOGNIZED"`)

* `UNRECOGNIZED_VERSION` (value: `"UNRECOGNIZED_VERSION"`)

* `UNEVALUATED` (value: `"UNEVALUATED"`)




