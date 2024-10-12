# AdyenCheckoutApi.PayWithGoogleDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fundingSource** | **String** | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. | [optional] 
**googlePayToken** | **String** | The &#x60;token&#x60; that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) &#x60;PaymentData&#x60; response. | 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **paywithgoogle** | [optional] [default to &#39;paywithgoogle&#39;]



## Enum: FundingSourceEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)





## Enum: TypeEnum


* `paywithgoogle` (value: `"paywithgoogle"`)




