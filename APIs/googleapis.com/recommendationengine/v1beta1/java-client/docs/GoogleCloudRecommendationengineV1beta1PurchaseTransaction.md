

# GoogleCloudRecommendationengineV1beta1PurchaseTransaction

A transaction represents the entire purchase transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costs** | **Map&lt;String, Float&gt;** | Optional. All the costs associated with the product. These can be manufacturing costs, shipping expenses not borne by the end user, or any other costs. Total product cost such that profit &#x3D; revenue - (sum(taxes) + sum(costs)) If product_cost is not set, then profit &#x3D; revenue - tax - shipping - sum(CatalogItem.costs). If CatalogItem.cost is not specified for one of the items, CatalogItem.cost based profit *cannot* be calculated for this Transaction. |  [optional] |
|**currencyCode** | **String** | Required. Currency code. Use three-character ISO-4217 code. This field is not required if the event type is &#x60;refund&#x60;. |  [optional] |
|**id** | **String** | Optional. The transaction ID with a length limit of 128 bytes. |  [optional] |
|**revenue** | **Float** | Required. Total revenue or grand total associated with the transaction. This value include shipping, tax, or other adjustments to total revenue that you want to include as part of your revenue calculations. This field is not required if the event type is &#x60;refund&#x60;. |  [optional] |
|**taxes** | **Map&lt;String, Float&gt;** | Optional. All the taxes associated with the transaction. |  [optional] |



