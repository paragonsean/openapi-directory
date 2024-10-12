# AdyenCheckoutApi.VisaCheckoutDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fundingSource** | **String** | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. | [optional] 
**type** | **String** | **visacheckout** | [optional] [default to &#39;visacheckout&#39;]
**visaCheckoutCallId** | **String** | The Visa Click to Pay Call ID value. When your shopper selects a payment and/or a shipping address from Visa Click to Pay, you will receive a Visa Click to Pay Call ID. | 



## Enum: FundingSourceEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)





## Enum: TypeEnum


* `visacheckout` (value: `"visacheckout"`)




