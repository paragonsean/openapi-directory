# CodatExpenseApi.TaxRateMappingInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Code for the tax rate from the accounting platform. | [optional] 
**effectiveTaxRate** | **Number** | Effective tax rate. | [optional] 
**id** | **String** | Unique identifier of tax rate. | [optional] 
**name** | **String** | Name of the tax rate in the accounting platform. | [optional] 
**totalTaxRate** | **Number** | Total (not compounded) sum of the components of a tax rate. | [optional] 
**validTransactionTypes** | **[String]** | Supported transaction types for the account. | [optional] 



## Enum: [ValidTransactionTypesEnum]


* `Payment` (value: `"Payment"`)

* `Refund` (value: `"Refund"`)

* `Reward` (value: `"Reward"`)

* `Chargeback` (value: `"Chargeback"`)

* `TransferIn` (value: `"TransferIn"`)

* `TransferOut` (value: `"TransferOut"`)

* `AdjustmentIn` (value: `"AdjustmentIn"`)

* `AdjustmentOut` (value: `"AdjustmentOut"`)




