# AdyenCheckoutApi.SamsungPayDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkoutAttemptId** | **String** | The checkout attempt identifier. | [optional] 
**fundingSource** | **String** | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. | [optional] 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**samsungPayToken** | **String** | The payload you received from the Samsung Pay SDK response. | 
**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **samsungpay** | [optional] [default to &#39;samsungpay&#39;]



## Enum: FundingSourceEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)





## Enum: TypeEnum


* `samsungpay` (value: `"samsungpay"`)




