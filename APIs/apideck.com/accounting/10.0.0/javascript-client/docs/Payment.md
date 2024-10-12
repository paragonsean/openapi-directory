# AccountingApi.Payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**accountsReceivableAccountId** | **String** | Unique identifier for the account to allocate payment to. | [optional] 
**accountsReceivableAccountType** | **String** | Type of accounts receivable account. | [optional] 
**allocations** | [**[PaymentAllocationsInner]**](PaymentAllocationsInner.md) |  | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currencyRate** | **Number** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**displayId** | **String** | Payment id to be displayed. | [optional] 
**downstreamId** | **String** | The third-party API ID of original entity | [optional] [readonly] 
**id** | **String** | Unique identifier representing the entity | [readonly] 
**note** | **String** | Optional note to be associated with the payment. | [optional] 
**paymentMethod** | **String** | Payment method name | [optional] 
**paymentMethodId** | **String** | Unique identifier for the payment method. | [optional] 
**paymentMethodReference** | **String** | Optional reference message returned by payment method on processing | [optional] 
**reconciled** | **Boolean** | Payment has been reconciled | [optional] 
**reference** | **String** | Optional payment reference message ie: Debit remittance detail. | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**status** | **String** | Status of payment | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**totalAmount** | **Number** | Amount of payment | 
**transactionDate** | **Date** | Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD | 
**type** | **String** | Type of payment | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: StatusEnum


* `authorised` (value: `"authorised"`)

* `paid` (value: `"paid"`)

* `voided` (value: `"voided"`)

* `deleted` (value: `"deleted"`)





## Enum: TypeEnum


* `receivable` (value: `"accounts_receivable"`)

* `payable` (value: `"accounts_payable"`)

* `receivable_credit` (value: `"accounts_receivable_credit"`)

* `payable_credit` (value: `"accounts_payable_credit"`)

* `receivable_overpayment` (value: `"accounts_receivable_overpayment"`)

* `payable_overpayment` (value: `"accounts_payable_overpayment"`)

* `receivable_prepayment` (value: `"accounts_receivable_prepayment"`)

* `payable_prepayment` (value: `"accounts_payable_prepayment"`)




