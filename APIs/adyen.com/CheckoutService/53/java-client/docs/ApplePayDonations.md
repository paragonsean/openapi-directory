

# ApplePayDonations


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applePayToken** | **String** | The stringified and base64 encoded &#x60;paymentData&#x60; you retrieved from the Apple framework. |  |
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **applepay** |  [optional] |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APPLEPAY | &quot;applepay&quot; |



