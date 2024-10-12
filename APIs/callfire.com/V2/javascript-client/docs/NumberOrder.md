# CallFireApiDocumentation.NumberOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Number** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 | [optional] [readonly] 
**id** | **Number** | An id of an order | [optional] 
**keywords** | [**NumberOrderItem**](NumberOrderItem.md) |  | [optional] 
**localNumbers** | [**NumberOrderItem**](NumberOrderItem.md) |  | [optional] 
**salesTax** | **Number** | ~ | [optional] [readonly] 
**status** | **String** | A current status of an order. Available values: NEW, PROCESSING, FINISHED, ERRORED, VOID, WAIT_FOR_PAYMENT, REJECTED | [optional] [readonly] 
**summary** | **Number** | ~ | [optional] [readonly] 
**tollFreeNumbers** | [**NumberOrderItem**](NumberOrderItem.md) |  | [optional] 
**total** | **Number** | ~ | [optional] [readonly] 
**totalCost** | **Number** | A total cost of an order | [optional] [readonly] 



## Enum: StatusEnum


* `PROCESSING` (value: `"PROCESSING"`)

* `FINISHED` (value: `"FINISHED"`)

* `PAYMENT_ERROR` (value: `"PAYMENT_ERROR"`)

* `VOID` (value: `"VOID"`)

* `WAIT_FOR_PAYMENT` (value: `"WAIT_FOR_PAYMENT"`)

* `PARTIALLY_ADJUSTED` (value: `"PARTIALLY_ADJUSTED"`)

* `ADJUSTED` (value: `"ADJUSTED"`)

* `NEW` (value: `"NEW"`)

* `ERRORED` (value: `"ERRORED"`)

* `APPROVE_TIER_ONE` (value: `"APPROVE_TIER_ONE"`)

* `APPROVE_TIER_TWO` (value: `"APPROVE_TIER_TWO"`)

* `REJECTED` (value: `"REJECTED"`)




