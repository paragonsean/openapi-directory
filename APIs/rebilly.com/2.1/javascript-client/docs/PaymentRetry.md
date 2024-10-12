# RebillyRestApi.PaymentRetry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterAttemptPolicy** | **String** | The policy on the attempt finishes. | 
**afterRetryEndPolicy** | **String** | The policy on the retry ends. | 
**attempts** | [**[PaymentRetryAttemptsInner]**](PaymentRetryAttemptsInner.md) |  | 



## Enum: AfterAttemptPolicyEnum


* `none` (value: `"none"`)

* `change-subscription-renewal-time` (value: `"change-subscription-renewal-time"`)





## Enum: AfterRetryEndPolicyEnum


* `none` (value: `"none"`)

* `cancel-subscription` (value: `"cancel-subscription"`)




