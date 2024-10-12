# PocketSmith.Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** |  | [optional] 
**amountInBaseCurrency** | **Number** | The amount of the transaction in the user&#39;s base currency. | [optional] 
**category** | [**Category**](Category.md) |  | [optional] 
**chequeNumber** | **String** |  | [optional] 
**closingBalance** | **Number** | The closing balance of the account at the transaction. | [optional] 
**createdAt** | **String** | When the transaction was created. | [optional] 
**date** | **String** | The date the transaction took place. | [optional] 
**id** | **Number** | The unique identifier of the transaction. | [optional] 
**isTransfer** | **Boolean** | Whether the transaction is a transfer. | [optional] 
**labels** | **[String]** |  | [optional] 
**memo** | **String** |  | [optional] 
**needsReview** | **Boolean** | Whether the transaction needs to be reviewed. | [optional] 
**note** | **String** |  | [optional] 
**originalPayee** | **String** | The payee the transaction was created with. | [optional] 
**payee** | **String** | The payee/merchant of the transaction. | [optional] 
**status** | **String** | The status of the transaction. Pending transactions are temporary and may be superseded later by their posted counterparts, which are permanent. | [optional] 
**transactionAccount** | [**TransactionAccount**](TransactionAccount.md) |  | [optional] 
**type** | **String** | Whether the transaction is a debit or a credit | [optional] 
**updatedAt** | **String** | When the transaction was last updated. | [optional] 
**uploadSource** | **String** | Where the transaction came from. | [optional] 



## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `posted` (value: `"posted"`)





## Enum: TypeEnum


* `debit` (value: `"debit"`)

* `credit` (value: `"credit"`)




