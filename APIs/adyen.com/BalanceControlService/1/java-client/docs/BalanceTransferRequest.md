

# BalanceTransferRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The amount of the transfer in [minor units](https://docs.adyen.com/development-resources/currency-codes). |  |
|**description** | **String** | A human-readable description for the transfer. You can use alphanumeric characters and hyphens. We recommend sending a maximum of 140 characters, otherwise the description may be truncated. |  [optional] |
|**fromMerchant** | **String** | The unique identifier of the source merchant account from which funds are deducted. |  |
|**reference** | **String** | A reference for the balance transfer. If you don&#39;t provide this in the request, Adyen generates a unique reference. Maximum length: 80 characters. |  [optional] |
|**toMerchant** | **String** | The unique identifier of the destination merchant account from which funds are transferred. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of balance transfer. Possible values: **tax**, **fee**, **terminalSale**, **credit**, **debit**, and **adjustment**. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TAX | &quot;tax&quot; |
| FEE | &quot;fee&quot; |
| TERMINAL_SALE | &quot;terminalSale&quot; |
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |
| ADJUSTMENT | &quot;adjustment&quot; |



