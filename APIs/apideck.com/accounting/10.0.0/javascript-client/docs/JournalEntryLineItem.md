# AccountingApi.JournalEntryLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**departmentId** | **String** | A unique identifier for an object. | [optional] [readonly] 
**description** | **String** | User defined description | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**ledgerAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | 
**locationId** | **String** | A unique identifier for an object. | [optional] [readonly] 
**subTotal** | **Number** | Sub-total amount, normally before tax. | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**taxAmount** | **Number** | Tax amount | [optional] 
**taxRate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**totalAmount** | **Number** | Debit entries are considered positive, and credit entries are considered negative. | [optional] 
**trackingCategory** | [**LinkedTrackingCategory**](LinkedTrackingCategory.md) |  | [optional] 
**type** | **String** | Debit entries are considered positive, and credit entries are considered negative. | 



## Enum: TypeEnum


* `debit` (value: `"debit"`)

* `credit` (value: `"credit"`)




