

# NumberOrder

Represents an order created on the CallFire platform

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **Long** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 |  [optional] [readonly] |
|**id** | **Long** | An id of an order |  [optional] |
|**keywords** | [**NumberOrderItem**](NumberOrderItem.md) |  |  [optional] |
|**localNumbers** | [**NumberOrderItem**](NumberOrderItem.md) |  |  [optional] |
|**salesTax** | **Float** | ~ |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | A current status of an order. Available values: NEW, PROCESSING, FINISHED, ERRORED, VOID, WAIT_FOR_PAYMENT, REJECTED |  [optional] [readonly] |
|**summary** | **Float** | ~ |  [optional] [readonly] |
|**tollFreeNumbers** | [**NumberOrderItem**](NumberOrderItem.md) |  |  [optional] |
|**total** | **Float** | ~ |  [optional] [readonly] |
|**totalCost** | **Float** | A total cost of an order |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PROCESSING | &quot;PROCESSING&quot; |
| FINISHED | &quot;FINISHED&quot; |
| PAYMENT_ERROR | &quot;PAYMENT_ERROR&quot; |
| VOID | &quot;VOID&quot; |
| WAIT_FOR_PAYMENT | &quot;WAIT_FOR_PAYMENT&quot; |
| PARTIALLY_ADJUSTED | &quot;PARTIALLY_ADJUSTED&quot; |
| ADJUSTED | &quot;ADJUSTED&quot; |
| NEW | &quot;NEW&quot; |
| ERRORED | &quot;ERRORED&quot; |
| APPROVE_TIER_ONE | &quot;APPROVE_TIER_ONE&quot; |
| APPROVE_TIER_TWO | &quot;APPROVE_TIER_TWO&quot; |
| REJECTED | &quot;REJECTED&quot; |



