# AdyenCheckoutApi.ApplePayDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applePayToken** | **String** | The stringified and base64 encoded &#x60;paymentData&#x60; you retrieved from the Apple framework. | 
**checkoutAttemptId** | **String** | The checkout attempt identifier. | [optional] 
**fundingSource** | **String** | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. | [optional] 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **applepay** | [optional] [default to &#39;applepay&#39;]



## Enum: FundingSourceEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)





## Enum: TypeEnum


* `applepay` (value: `"applepay"`)




