

# PromotionEditFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beginsAt** | **String** | Creation date of the promotion (requires &#39;lasts&#39; param - &#39;date&#39;) |  [optional] |
|**buysAtLeast** | **String** | Controls the promotion&#39;s condition (&#39;none&#39;, &#39;price&#39;, &#39;qty&#39;) |  [optional] |
|**categories** | [**List&lt;Id&gt;**](Id.md) | Products Categories where the promotion will be applied (requires &#39;discount_target&#39; param - &#39;categories&#39;) |  [optional] |
|**code** | **String** | Code of the promotion |  [optional] |
|**conditionPrice** | **Float** | Minimum order amount to validate the promotion (requires &#39;buys_at_least&#39; param - &#39;price&#39;) |  [optional] |
|**conditionQty** | **Integer** | Minimum quantity of ordered itens to validate the promotion (requires &#39;buys_at_least&#39; param - &#39;qty&#39;) |  [optional] |
|**cumulative** | **Boolean** | True if the promotion can be acumulated with others |  [optional] |
|**customerCategories** | [**List&lt;Id&gt;**](Id.md) | Customer Categories to whom the promotion will be applied (requires &#39;customers&#39; param - &#39;categories&#39;) |  [optional] |
|**customers** | **String** | Controls to which customers the promotion will be applied (&#39;all&#39;, &#39;loggedin&#39;, &#39;categories&#39;, &#39;guests&#39;) |  [optional] |
|**discountAmountFix** | **Float** | Fixed discount amount of the promotion (requires &#39;type&#39; param - &#39;fix&#39;) |  [optional] |
|**discountAmountPercent** | **Float** | Percentual discount amount of the promotion (requires &#39;type&#39; param - &#39;percentage&#39;) |  [optional] |
|**discountTarget** | **String** | Where the promotion will be applied (&#39;order&#39;, &#39;shipping&#39;, &#39;categories&#39;, &#39;buy_x_get_y) |  [optional] |
|**enabled** | **Boolean** | If the promotion is to be temporarily disabled |  [optional] |
|**expiresAt** | **String** | Expiration date of the promotion (requires &#39;lasts&#39; param - &#39;date&#39;) |  [optional] |
|**lasts** | **String** | Controls when the promotion will expire (&#39;none&#39;, &#39;date&#39;, &#39;max_times_used&#39;) |  [optional] |
|**maxTimesUsed** | **Integer** | Maximum amount a promotion can be used (requires &#39;lasts&#39; param - &#39;max_times_used&#39;) |  [optional] |
|**name** | **String** | Name of the product |  [optional] |
|**products** | [**List&lt;Id&gt;**](Id.md) | Products where the promotion will be applied (requires &#39;discount_target&#39; param - &#39;categories&#39; or &#39;buy_x_get_y&#39;) |  [optional] |
|**productsX** | [**List&lt;Id&gt;**](Id.md) | Products required to apply the promotion (requires &#39;discount_target&#39; param - &#39;buy_x_get_y&#39;) |  [optional] |
|**quantityX** | **Integer** | Number of sets of products_x needed to be able to apply the promotion (requires &#39;discount_target&#39; param - &#39;buy_x_get_y&#39;) |  [optional] |
|**type** | **String** | Controls if the discount will be a fixed area (&#39;fix&#39;, &#39;percentage&#39;) |  [optional] |



