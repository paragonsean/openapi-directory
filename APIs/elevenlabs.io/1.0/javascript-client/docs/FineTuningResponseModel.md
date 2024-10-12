# ElevenLabsApiDocumentation.FineTuningResponseModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fineTuningRequested** | **Boolean** |  | 
**finetuningState** | **String** |  | 
**isAllowedToFineTune** | **Boolean** |  | 
**modelId** | **String** |  | 
**sliceIds** | **[String]** |  | 
**verificationAttempts** | [**[VerificationAttemptResponseModel]**](VerificationAttemptResponseModel.md) |  | 
**verificationAttemptsCount** | **Number** |  | 
**verificationFailures** | **[String]** |  | 



## Enum: FinetuningStateEnum


* `not_started` (value: `"not_started"`)

* `is_fine_tuning` (value: `"is_fine_tuning"`)

* `fine_tuned` (value: `"fine_tuned"`)




