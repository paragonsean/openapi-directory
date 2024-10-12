# PocketSmith.Category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**[Category]**](Category.md) | The category&#39;s child categories. | [optional] 
**colour** | **String** | The colour for the category. | [optional] 
**createdAt** | **String** | When the category was created. | [optional] 
**id** | **Number** | The unique identifier of the category. | [optional] 
**isBill** | **Boolean** | Whether the category is a bill category. A bill category is when budgeted amounts are normally spent at once, instead of spread across a budgeting period. This category will be included in the bill reminder email when set to true. | [optional] 
**isTransfer** | **Boolean** | Whether this category has been marked as a transfer category. | [optional] 
**parentId** | **Number** | The unique identifier of the parent category of this category, or null if this category has no parent (i.e. is a top-level category) | [optional] 
**refundBehaviour** | **String** | How the category&#39;s refunds or deductions should be reported on. | [optional] 
**rollUp** | **Boolean** | Whether the category&#39;s budget is rolled up into its parent category, if a parent category is present. | [optional] 
**title** | **String** | The title of the category. | [optional] 
**updatedAt** | **String** | When the category was last updated. | [optional] 



## Enum: RefundBehaviourEnum


* `debits_are_deductions` (value: `"debits_are_deductions"`)

* `credits_are_refunds` (value: `"credits_are_refunds"`)




