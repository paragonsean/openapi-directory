# CodatExpenseApi.AccountMappingInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | Type of the account. | [optional] 
**currency** | **String** | Currency of the account. | [optional] 
**id** | **String** | Unique identifier of account. | [optional] 
**name** | **String** | Name of the account as it appears in the companies accounting software. | [optional] 
**validTransactionTypes** | **[String]** | Supported transaction types for the account. | [optional] 



## Enum: AccountTypeEnum


* `Asset` (value: `"Asset"`)

* `Liability` (value: `"Liability"`)

* `Income` (value: `"Income"`)

* `Expense` (value: `"Expense"`)

* `Equity` (value: `"Equity"`)





## Enum: [ValidTransactionTypesEnum]


* `Payment` (value: `"Payment"`)

* `Refund` (value: `"Refund"`)

* `Reward` (value: `"Reward"`)

* `Chargeback` (value: `"Chargeback"`)

* `TransferIn` (value: `"TransferIn"`)

* `TransferOut` (value: `"TransferOut"`)

* `AdjustmentIn` (value: `"AdjustmentIn"`)

* `AdjustmentOut` (value: `"AdjustmentOut"`)




