

# CreditNoteAllocationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | Amount of payment that should be attributed to this allocation. If null, the total_amount will be used. |  [optional] |
|**code** | **String** |  |  [optional] [readonly] |
|**id** | **String** | Unique identifier of entity this payment should be attributed to. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of entity this payment should be attributed to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INVOICE | &quot;invoice&quot; |
| ORDER | &quot;order&quot; |
| EXPENSE | &quot;expense&quot; |
| CREDIT_MEMO | &quot;credit_memo&quot; |
| OVER_PAYMENT | &quot;over_payment&quot; |
| PRE_PAYMENT | &quot;pre_payment&quot; |



