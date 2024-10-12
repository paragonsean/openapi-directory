# PocketSmith.TransactionAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** |  | [optional] 
**currencyCode** | **String** | The currency that the account is in. This is determined by the account that the transaction account belongs to. | [optional] 
**currentBalance** | **Number** |  | [optional] 
**currentBalanceDate** | **String** |  | [optional] 
**currentBalanceExchangeRate** | **Number** | The exchange rate between the transaction account&#39;s currency and the user&#39;s base currency, when different. If the currencies are the same, null is returned. | [optional] 
**currentBalanceInBaseCurrency** | **Number** | The current balance of the transaction account in the user&#39;s base currency. | [optional] 
**id** | **Number** |  | [optional] 
**institution** | [**Institution**](Institution.md) |  | [optional] 
**name** | **String** |  | [optional] 
**number** | **String** |  | [optional] 
**safeBalance** | **Number** | The current safe balance, if safe balance is activated and available for the transaction account. If safe balance is not available, then null is returned. | [optional] 
**safeBalanceInBaseCurrency** | **Number** | The current safe balance in the user&#39;s base currency, if safe balance is activated and available for the transaction account. If safe balance is not available, then null is returned. | [optional] 
**startingBalance** | **Number** |  | [optional] 
**startingBalanceDate** | **String** |  | [optional] 
**type** | **String** | The type of the transaction account. | [optional] 
**updatedAt** | **String** |  | [optional] 



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




