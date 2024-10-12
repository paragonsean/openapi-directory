# AdyenCheckoutApi.MasterpassDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fundingSource** | **String** | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. | [optional] 
**masterpassTransactionId** | **String** | The Masterpass transaction ID. | 
**type** | **String** | **masterpass** | [optional] [default to &#39;masterpass&#39;]



## Enum: FundingSourceEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)





## Enum: TypeEnum


* `masterpass` (value: `"masterpass"`)




