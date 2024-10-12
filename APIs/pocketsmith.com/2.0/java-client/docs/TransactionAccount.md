

# TransactionAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** |  |  [optional] |
|**currencyCode** | **String** | The currency that the account is in. This is determined by the account that the transaction account belongs to. |  [optional] |
|**currentBalance** | **BigDecimal** |  |  [optional] |
|**currentBalanceDate** | **String** |  |  [optional] |
|**currentBalanceExchangeRate** | **BigDecimal** | The exchange rate between the transaction account&#39;s currency and the user&#39;s base currency, when different. If the currencies are the same, null is returned. |  [optional] |
|**currentBalanceInBaseCurrency** | **BigDecimal** | The current balance of the transaction account in the user&#39;s base currency. |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**institution** | [**Institution**](Institution.md) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**number** | **String** |  |  [optional] |
|**safeBalance** | **BigDecimal** | The current safe balance, if safe balance is activated and available for the transaction account. If safe balance is not available, then null is returned. |  [optional] |
|**safeBalanceInBaseCurrency** | **BigDecimal** | The current safe balance in the user&#39;s base currency, if safe balance is activated and available for the transaction account. If safe balance is not available, then null is returned. |  [optional] |
|**startingBalance** | **BigDecimal** |  |  [optional] |
|**startingBalanceDate** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the transaction account. |  [optional] |
|**updatedAt** | **String** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| CREDITS | &quot;credits&quot; |
| CASH | &quot;cash&quot; |
| STOCKS | &quot;stocks&quot; |
| MORTGAGE | &quot;mortgage&quot; |
| LOANS | &quot;loans&quot; |
| VEHICLE | &quot;vehicle&quot; |
| PROPERTY | &quot;property&quot; |
| INSURANCE | &quot;insurance&quot; |
| OTHER_ASSET | &quot;other_asset&quot; |
| OTHER_LIABILITY | &quot;other_liability&quot; |



