# YnabApiEndpoints.TransactionSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** |  | 
**amount** | **Number** | The transaction amount in milliunits format | 
**approved** | **Boolean** | Whether or not the transaction is approved | 
**categoryId** | **String** |  | [optional] 
**cleared** | **String** | The cleared status of the transaction | 
**date** | **Date** | The transaction date in ISO format (e.g. 2016-12-01) | 
**debtTransactionType** | **String** | If the transaction is a debt/loan account transaction, the type of transaction | [optional] 
**deleted** | **Boolean** | Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests. | 
**flagColor** | **String** | The transaction flag | [optional] 
**id** | **String** |  | 
**importId** | **String** | If the transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: &#39;YNAB:[milliunit_amount]:[iso_date]:[occurrence]&#39;.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of &#39;YNAB:-294230:2015-12-30:1&#39;.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be &#39;YNAB:-294230:2015-12-30:2&#39;. | [optional] 
**importPayeeName** | **String** | If the transaction was imported, the payee name that was used when importing and before applying any payee rename rules | [optional] 
**importPayeeNameOriginal** | **String** | If the transaction was imported, the original payee name as it appeared on the statement | [optional] 
**matchedTransactionId** | **String** | If transaction is matched, the id of the matched transaction | [optional] 
**memo** | **String** |  | [optional] 
**payeeId** | **String** |  | [optional] 
**transferAccountId** | **String** | If a transfer transaction, the account to which it transfers | [optional] 
**transferTransactionId** | **String** | If a transfer transaction, the id of transaction on the other side of the transfer | [optional] 



## Enum: ClearedEnum


* `cleared` (value: `"cleared"`)

* `uncleared` (value: `"uncleared"`)

* `reconciled` (value: `"reconciled"`)





## Enum: DebtTransactionTypeEnum


* `payment` (value: `"payment"`)

* `refund` (value: `"refund"`)

* `fee` (value: `"fee"`)

* `interest` (value: `"interest"`)

* `escrow` (value: `"escrow"`)

* `balancedAdjustment` (value: `"balancedAdjustment"`)

* `credit` (value: `"credit"`)

* `charge` (value: `"charge"`)





## Enum: FlagColorEnum


* `red` (value: `"red"`)

* `orange` (value: `"orange"`)

* `yellow` (value: `"yellow"`)

* `green` (value: `"green"`)

* `blue` (value: `"blue"`)

* `purple` (value: `"purple"`)




