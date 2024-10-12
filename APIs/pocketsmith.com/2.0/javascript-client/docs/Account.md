# PocketSmith.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | When the account was created. | [optional] 
**currencyCode** | **String** | The currency code for the account. | [optional] 
**currentBalance** | **Number** | The current balance of the account. | [optional] 
**currentBalanceDate** | **String** | The date of the current balance. | [optional] 
**currentBalanceExchangeRate** | **Number** | The exchange rate between the account&#39;s currency and the user&#39;s base currency, when different. If the currencies are the same, null is returned. | [optional] 
**currentBalanceInBaseCurrency** | **Number** | The current balance of the account in the user&#39;s base currency. | [optional] 
**id** | **Number** | The unique identifier of the account. | [optional] 
**isNetWorth** | **Boolean** | Whether the account is a net worth asset. | [optional] 
**primaryScenario** | [**Scenario**](Scenario.md) |  | [optional] 
**primaryTransactionAccount** | [**TransactionAccount**](TransactionAccount.md) |  | [optional] 
**safeBalance** | **Number** | The current safe balance, if safe balance is activated on the account. If safe balance is not activated, then null is returned. | [optional] 
**safeBalanceInBaseCurrency** | **Number** | The current safe balance in the user&#39;s base currency, if safe balance is activated on the account. If safe balance is not activated, then null is returned. | [optional] 
**scenarios** | [**[Scenario]**](Scenario.md) | All scenarios that compose the account, including the primary. | [optional] 
**title** | **String** | The title of the account. | [optional] 
**transactionAccounts** | [**[TransactionAccount]**](TransactionAccount.md) | All transaction accounts that compose the account, including the primary. | [optional] 
**type** | **String** | The type of the account. | [optional] 
**updatedAt** | **String** | When the account was last updated. | [optional] 



## Enum: TypeEnum


* `bank` (value: `"bank"`)

* `credits` (value: `"credits"`)

* `cash` (value: `"cash"`)

* `stocks` (value: `"stocks"`)

* `mortgage` (value: `"mortgage"`)

* `loans` (value: `"loans"`)

* `vehicle` (value: `"vehicle"`)

* `property` (value: `"property"`)

* `insurance` (value: `"insurance"`)

* `other_asset` (value: `"other_asset"`)

* `other_liability` (value: `"other_liability"`)




