

# VisaCheckoutDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkoutAttemptId** | **String** | The checkout attempt identifier. |  [optional] |
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **visacheckout** |  [optional] |
|**visaCheckoutCallId** | **String** | The Visa Click to Pay Call ID value. When your shopper selects a payment and/or a shipping address from Visa Click to Pay, you will receive a Visa Click to Pay Call ID. |  |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VISACHECKOUT | &quot;visacheckout&quot; |



