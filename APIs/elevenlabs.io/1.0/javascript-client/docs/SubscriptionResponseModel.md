# ElevenLabsApiDocumentation.SubscriptionResponseModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedToExtendCharacterLimit** | **Boolean** |  | 
**availableModels** | [**[TTSModelResponseModel]**](TTSModelResponseModel.md) |  | 
**canExtendCharacterLimit** | **Boolean** |  | 
**canExtendVoiceLimit** | **Boolean** |  | 
**canUseDelayedPaymentMethods** | **Boolean** |  | 
**canUseInstantVoiceCloning** | **Boolean** |  | 
**canUseProfessionalVoiceCloning** | **Boolean** |  | 
**characterCount** | **Number** |  | 
**characterLimit** | **Number** |  | 
**currency** | **String** |  | 
**nextCharacterCountResetUnix** | **Number** |  | 
**professionalVoiceLimit** | **Number** |  | 
**status** | **String** |  | 
**tier** | **String** |  | 
**voiceLimit** | **Number** |  | 



## Enum: CurrencyEnum


* `usd` (value: `"usd"`)

* `eur` (value: `"eur"`)





## Enum: StatusEnum


* `trialing` (value: `"trialing"`)

* `active` (value: `"active"`)

* `incomplete` (value: `"incomplete"`)

* `incomplete_expired` (value: `"incomplete_expired"`)

* `past_due` (value: `"past_due"`)

* `canceled` (value: `"canceled"`)

* `unpaid` (value: `"unpaid"`)

* `free` (value: `"free"`)




