# PocketSmith.CategoriesIdPutRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colour** | **String** | A new CSS-style hex colour for the category. | [optional] 
**isBill** | **Boolean** | Set the category as a bill category. | [optional] 
**isTransfer** | **Boolean** | Set the category as a transfer category. | [optional] 
**parentId** | **Number** | The unique identifier of a parent category for the category, making this category a child of that category. | [optional] 
**refundBehaviour** | **String** | Set the refund behaviour of the category. | [optional] 
**rollUp** | **Boolean** | Set the category to be rolled up into its parent category. | [optional] 
**title** | **String** | A new title for the category. | [optional] 



## Enum: RefundBehaviourEnum


* `debits_are_deductions` (value: `"debits_are_deductions"`)

* `credits_are_refunds` (value: `"credits_are_refunds"`)




