

# Account


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | When the account was created. |  [optional] |
|**currencyCode** | **String** | The currency code for the account. |  [optional] |
|**currentBalance** | **BigDecimal** | The current balance of the account. |  [optional] |
|**currentBalanceDate** | **String** | The date of the current balance. |  [optional] |
|**currentBalanceExchangeRate** | **BigDecimal** | The exchange rate between the account&#39;s currency and the user&#39;s base currency, when different. If the currencies are the same, null is returned. |  [optional] |
|**currentBalanceInBaseCurrency** | **BigDecimal** | The current balance of the account in the user&#39;s base currency. |  [optional] |
|**id** | **Integer** | The unique identifier of the account. |  [optional] |
|**isNetWorth** | **Boolean** | Whether the account is a net worth asset. |  [optional] |
|**primaryScenario** | [**Scenario**](Scenario.md) |  |  [optional] |
|**primaryTransactionAccount** | [**TransactionAccount**](TransactionAccount.md) |  |  [optional] |
|**safeBalance** | **BigDecimal** | The current safe balance, if safe balance is activated on the account. If safe balance is not activated, then null is returned. |  [optional] |
|**safeBalanceInBaseCurrency** | **BigDecimal** | The current safe balance in the user&#39;s base currency, if safe balance is activated on the account. If safe balance is not activated, then null is returned. |  [optional] |
|**scenarios** | [**List&lt;Scenario&gt;**](Scenario.md) | All scenarios that compose the account, including the primary. |  [optional] |
|**title** | **String** | The title of the account. |  [optional] |
|**transactionAccounts** | [**List&lt;TransactionAccount&gt;**](TransactionAccount.md) | All transaction accounts that compose the account, including the primary. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the account. |  [optional] |
|**updatedAt** | **String** | When the account was last updated. |  [optional] |



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



