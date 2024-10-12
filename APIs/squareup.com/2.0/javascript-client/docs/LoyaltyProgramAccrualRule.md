# SquareConnectApi.LoyaltyProgramAccrualRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrualType** | **String** | The type of the accrual rule that defines how buyers can earn points. | 
**catalogObjectId** | **String** | When the accrual rule is item-based or category-based, this field specifies the ID  of the [catalog object](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) that buyers can purchase to earn points.  If &#x60;accrual_type&#x60; is &#x60;ITEM_VARIATION&#x60;, the object is an item variation.  If &#x60;accrual_type&#x60; is &#x60;CATEGORY&#x60;, the object is a category. | [optional] 
**excludedCategoryIds** | **[String]** | When the accrual rule is spend-based (&#x60;accrual_type&#x60; is &#x60;SPEND&#x60;), this field  lists the IDs of any &#x60;CATEGORY&#x60; catalog objects that are excluded from points accrual.   You can use the [BatchRetrieveCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/batch-retrieve-catalog-objects)  endpoint to retrieve information about the excluded categories. | [optional] 
**excludedItemVariationIds** | **[String]** | When the accrual rule is spend-based (&#x60;accrual_type&#x60; is &#x60;SPEND&#x60;), this field  lists the IDs of any &#x60;ITEM_VARIATION&#x60; catalog objects that are excluded from points accrual.   You can use the [BatchRetrieveCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/batch-retrieve-catalog-objects)  endpoint to retrieve information about the excluded item variations. | [optional] 
**points** | **Number** | The number of points that  buyers earn based on the &#x60;accrual_type&#x60;. | [optional] 
**spendAmountMoney** | [**Money**](Money.md) |  | [optional] 
**visitMinimumAmountMoney** | [**Money**](Money.md) |  | [optional] 


