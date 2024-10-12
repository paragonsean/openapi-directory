# AccountingApi.CreditNoteAllocationsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Amount of payment that should be attributed to this allocation. If null, the total_amount will be used. | [optional] 
**code** | **String** |  | [optional] [readonly] 
**id** | **String** | Unique identifier of entity this payment should be attributed to. | [optional] 
**type** | **String** | Type of entity this payment should be attributed to. | [optional] 



## Enum: TypeEnum


* `invoice` (value: `"invoice"`)

* `order` (value: `"order"`)

* `expense` (value: `"expense"`)

* `credit_memo` (value: `"credit_memo"`)

* `over_payment` (value: `"over_payment"`)

* `pre_payment` (value: `"pre_payment"`)




