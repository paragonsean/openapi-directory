

# CreateCardPaymentRequest

The Payment Request Payload

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | amount in pence |  [readonly] |
|**delayedCapture** | **Boolean** | delayed capture flag |  [optional] [readonly] |
|**description** | **String** | payment description |  [readonly] |
|**email** | **String** | email |  [optional] [readonly] |
|**language** | [**LanguageEnum**](#LanguageEnum) | ISO-639-1 Alpha-2 code of a supported language to use on the payment pages |  [optional] [readonly] |
|**metadata** | **Map&lt;String, Object&gt;** | Additional metadata - up to 10 name/value pairs - on the payment. Each key must be between 1 and 30 characters long. The value, if a string, must be no greater than 50 characters long. Other permissible value types: boolean, number. |  [optional] [readonly] |
|**moto** | **Boolean** | Mail Order / Telephone Order (MOTO) payment flag |  [optional] [readonly] |
|**prefilledCardholderDetails** | [**PrefilledCardholderDetails**](PrefilledCardholderDetails.md) |  |  [optional] |
|**reference** | **String** | payment reference |  [readonly] |
|**returnUrl** | **String** | service return url |  [readonly] |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| EN | &quot;en&quot; |
| CY | &quot;cy&quot; |



