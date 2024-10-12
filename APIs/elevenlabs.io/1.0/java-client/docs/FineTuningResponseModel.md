

# FineTuningResponseModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fineTuningRequested** | **Boolean** |  |  |
|**finetuningState** | [**FinetuningStateEnum**](#FinetuningStateEnum) |  |  |
|**isAllowedToFineTune** | **Boolean** |  |  |
|**modelId** | **String** |  |  |
|**sliceIds** | **List&lt;String&gt;** |  |  |
|**verificationAttempts** | [**List&lt;VerificationAttemptResponseModel&gt;**](VerificationAttemptResponseModel.md) |  |  |
|**verificationAttemptsCount** | **Integer** |  |  |
|**verificationFailures** | **List&lt;String&gt;** |  |  |



## Enum: FinetuningStateEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;not_started&quot; |
| IS_FINE_TUNING | &quot;is_fine_tuning&quot; |
| FINE_TUNED | &quot;fine_tuned&quot; |



