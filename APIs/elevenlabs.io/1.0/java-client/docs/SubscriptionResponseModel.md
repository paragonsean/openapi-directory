

# SubscriptionResponseModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedToExtendCharacterLimit** | **Boolean** |  |  |
|**availableModels** | [**List&lt;TTSModelResponseModel&gt;**](TTSModelResponseModel.md) |  |  |
|**canExtendCharacterLimit** | **Boolean** |  |  |
|**canExtendVoiceLimit** | **Boolean** |  |  |
|**canUseDelayedPaymentMethods** | **Boolean** |  |  |
|**canUseInstantVoiceCloning** | **Boolean** |  |  |
|**canUseProfessionalVoiceCloning** | **Boolean** |  |  |
|**characterCount** | **Integer** |  |  |
|**characterLimit** | **Integer** |  |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) |  |  |
|**nextCharacterCountResetUnix** | **Integer** |  |  |
|**professionalVoiceLimit** | **Integer** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**tier** | **String** |  |  |
|**voiceLimit** | **Integer** |  |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| USD | &quot;usd&quot; |
| EUR | &quot;eur&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| TRIALING | &quot;trialing&quot; |
| ACTIVE | &quot;active&quot; |
| INCOMPLETE | &quot;incomplete&quot; |
| INCOMPLETE_EXPIRED | &quot;incomplete_expired&quot; |
| PAST_DUE | &quot;past_due&quot; |
| CANCELED | &quot;canceled&quot; |
| UNPAID | &quot;unpaid&quot; |
| FREE | &quot;free&quot; |



