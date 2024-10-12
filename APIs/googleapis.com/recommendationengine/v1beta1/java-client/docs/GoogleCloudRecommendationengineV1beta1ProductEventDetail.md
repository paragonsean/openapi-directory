

# GoogleCloudRecommendationengineV1beta1ProductEventDetail

ProductEventDetail captures user event information specific to retail products.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cartId** | **String** | Optional. The id or name of the associated shopping cart. This id is used to associate multiple items added or present in the cart before purchase. This can only be set for &#x60;add-to-cart&#x60;, &#x60;remove-from-cart&#x60;, &#x60;checkout-start&#x60;, &#x60;purchase-complete&#x60;, or &#x60;shopping-cart-page-view&#x60; events. |  [optional] |
|**listId** | **String** | Required for &#x60;add-to-list&#x60; and &#x60;remove-from-list&#x60; events. The id or name of the list that the item is being added to or removed from. Other event types should not set this field. |  [optional] |
|**pageCategories** | [**List&lt;GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy&gt;**](GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy.md) | Required for &#x60;category-page-view&#x60; events. At least one of search_query or page_categories is required for &#x60;search&#x60; events. Other event types should not set this field. The categories associated with a category page. Category pages include special pages such as sales or promotions. For instance, a special sale page may have the category hierarchy: categories : [\&quot;Sales\&quot;, \&quot;2017 Black Friday Deals\&quot;]. |  [optional] |
|**productDetails** | [**List&lt;GoogleCloudRecommendationengineV1beta1ProductDetail&gt;**](GoogleCloudRecommendationengineV1beta1ProductDetail.md) | The main product details related to the event. This field is required for the following event types: * &#x60;add-to-cart&#x60; * &#x60;add-to-list&#x60; * &#x60;checkout-start&#x60; * &#x60;detail-page-view&#x60; * &#x60;purchase-complete&#x60; * &#x60;refund&#x60; * &#x60;remove-from-cart&#x60; * &#x60;remove-from-list&#x60; This field is optional for the following event types: * &#x60;page-visit&#x60; * &#x60;shopping-cart-page-view&#x60; - note that &#39;product_details&#39; should be set for this unless the shopping cart is empty. * &#x60;search&#x60; (highly encouraged) In a &#x60;search&#x60; event, this field represents the products returned to the end user on the current page (the end user may have not finished broswing the whole page yet). When a new page is returned to the end user, after pagination/filtering/ordering even for the same query, a new SEARCH event with different product_details is desired. The end user may have not finished broswing the whole page yet. This field is not allowed for the following event types: * &#x60;category-page-view&#x60; * &#x60;home-page-view&#x60; |  [optional] |
|**purchaseTransaction** | [**GoogleCloudRecommendationengineV1beta1PurchaseTransaction**](GoogleCloudRecommendationengineV1beta1PurchaseTransaction.md) |  |  [optional] |
|**searchQuery** | **String** | At least one of search_query or page_categories is required for &#x60;search&#x60; events. Other event types should not set this field. The user&#39;s search query as UTF-8 encoded text with a length limit of 5 KiB. |  [optional] |



