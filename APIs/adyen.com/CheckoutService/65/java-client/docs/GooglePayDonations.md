

# GooglePayDonations


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |  [optional] |
|**googlePayCardNetwork** | **String** | The selected payment card network.  |  [optional] |
|**googlePayToken** | **String** | The &#x60;token&#x60; that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) &#x60;PaymentData&#x60; response. |  |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **googlepay**, **paywithgoogle** |  [optional] |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GOOGLEPAY | &quot;googlepay&quot; |



