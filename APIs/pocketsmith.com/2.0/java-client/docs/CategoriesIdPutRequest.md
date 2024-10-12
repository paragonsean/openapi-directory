

# CategoriesIdPutRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**colour** | **String** | A new CSS-style hex colour for the category. |  [optional] |
|**isBill** | **Boolean** | Set the category as a bill category. |  [optional] |
|**isTransfer** | **Boolean** | Set the category as a transfer category. |  [optional] |
|**parentId** | **Integer** | The unique identifier of a parent category for the category, making this category a child of that category. |  [optional] |
|**refundBehaviour** | [**RefundBehaviourEnum**](#RefundBehaviourEnum) | Set the refund behaviour of the category. |  [optional] |
|**rollUp** | **Boolean** | Set the category to be rolled up into its parent category. |  [optional] |
|**title** | **String** | A new title for the category. |  [optional] |



## Enum: RefundBehaviourEnum

| Name | Value |
|---- | -----|
| DEBITS_ARE_DEDUCTIONS | &quot;debits_are_deductions&quot; |
| CREDITS_ARE_REFUNDS | &quot;credits_are_refunds&quot; |



