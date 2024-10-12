

# SalesOrderDiscountDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discountAmount** | **Double** | The amount of the discount |  [optional] |
|**discountId** | **String** | The identifier of the discount applied to the order |  [optional] |
|**discountPercent** | **Double** | The discount percent, if the discount is defined to be calculated as a percentage |  [optional] |
|**discountSequenceId** | **String** | The identifier of the discount sequence of the discount ID applied to the order |  [optional] |
|**discountableAmount** | **Double** | The amount used as a base for discount calculation if the discount is based on amount. |  [optional] |
|**discountableQuantity** | **Double** | The quantity used as a base for discount calculation if the discount is based on quantity. |  [optional] |
|**freeItem** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |
|**freeItemQuantity** | **Double** | The quantity of the free item. Used to set the quantity for the order line generate by a free item discount |  [optional] |
|**isManual** | **Boolean** | Indicates that the discount has been applied manually |  [optional] |
|**manualOrderIndex** | **Integer** | The number of discount line set for the order |  [optional] |
|**skipDiscount** | **Boolean** | Indicates if the discount has been cancelled for the order and is not applicable |  [optional] |
|**type** | **String** | The type of discount whose sequence was applied to the document(Group or Document) |  [optional] |



