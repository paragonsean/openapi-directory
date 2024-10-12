

# PaymentRetry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afterAttemptPolicy** | [**AfterAttemptPolicyEnum**](#AfterAttemptPolicyEnum) | The policy on the attempt finishes. |  |
|**afterRetryEndPolicy** | [**AfterRetryEndPolicyEnum**](#AfterRetryEndPolicyEnum) | The policy on the retry ends. |  |
|**attempts** | [**List&lt;PaymentRetryAttemptsInner&gt;**](PaymentRetryAttemptsInner.md) |  |  |



## Enum: AfterAttemptPolicyEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| CHANGE_SUBSCRIPTION_RENEWAL_TIME | &quot;change-subscription-renewal-time&quot; |



## Enum: AfterRetryEndPolicyEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| CANCEL_SUBSCRIPTION | &quot;cancel-subscription&quot; |



