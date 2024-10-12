

# SetcampaignconfigurationRequestTargetConfigurationsInner

Object with information about the target audience.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affiliates** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestAffiliatesInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestAffiliatesInner.md) | Marketplace order identifier. The discount will apply to selected affiliates. |  [optional] |
|**areSalesChannelIdsExclusive** | **Boolean** | Shows if the trade policy IDs are exclusive. |  [optional] |
|**brands** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestBrandsInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestBrandsInner.md) | Object composed by the brands that will activate or deactivate the campaign audience. |  [optional] |
|**brandsAreInclusive** | **Boolean** | If set to &#x60;true&#x60;, this campaign audience will be applied to any brand present on the &#x60;brands&#x60; field. If set to &#x60;false&#x60;, brands present on that field will make this campaign audience not to be applied. |  [optional] |
|**campaigns** | **List&lt;Object&gt;** | Campaign Audiences that activate this promotion. |  [optional] |
|**cardIssuers** | **List&lt;Object&gt;** |  |  [optional] |
|**categories** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestCategoriesInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestCategoriesInner.md) | Object composed by the categories that will activate or deactivate the campaign audience. |  [optional] |
|**categoriesAreInclusive** | **Boolean** | If set to &#x60;true&#x60;, this campaign audience will be applied to any category present on the &#x60;categories&#x60; field. If set to &#x60;false&#x60;, categories present on that field will make this campaign audience not to be applied. |  [optional] |
|**clusterExpressions** | **List&lt;String&gt;** | An expression to use with clusters. |  [optional] |
|**clusterOperator** | **String** |  |  [optional] |
|**collections** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestCollectionsInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestCollectionsInner.md) | Object composed by the collections that will activate or deactivate the campaign audience. |  [optional] |
|**collections1BuyTogether** | **List&lt;String&gt;** | Collections that will generate the promotion, type **Buy Together**, **More for less**, **Progressive Discount**, **Buy One Get One**. |  [optional] |
|**collections2BuyTogether** | **List&lt;Object&gt;** |  |  [optional] |
|**collectionsIsInclusive** | **Boolean** | If set to &#x60;true&#x60;, this campaign audience will be applied to any collection present on the &#x60;collections&#x60; field. If set to &#x60;false&#x60;, collections present on that field will make this campaign audience not to be applied. |  [optional] |
|**compareListPriceAndPrice** | **Boolean** | If the **List Price** and **Price** are the same. |  [optional] |
|**coupon** | **List&lt;Object&gt;** |  |  [optional] |
|**daysAgoOfPurchases** | **Integer** | Number of days that are considered to add the purchase history. |  [optional] |
|**enableBuyTogetherPerSku** | **Boolean** | Enable **Buy Together** per SKU. |  [optional] |
|**featured** | **Boolean** | Defines if the target audience is featured (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  [optional] |
|**firstBuyIsProfileOptimistic** | **Boolean** | Applies the discount even if the user is not logged. |  [optional] |
|**giftListTypes** | **List&lt;String&gt;** | Gifts List Type. |  [optional] |
|**id** | **String** | Target audience ID. |  [optional] |
|**idSellerIsInclusive** | **Boolean** | Shows if at least one of the sellers must be valid to active the campaign audience. |  [optional] |
|**idsSalesChannel** | **List&lt;String&gt;** | Shows the trade policies that active the campaign audience. |  [optional] |
|**installment** | **Integer** |  |  [optional] |
|**isDifferentListPriceAndPrice** | **Boolean** | Applies the campaign audience only if the list price and price is different. |  [optional] |
|**isFirstBuy** | **Boolean** | Applies the discount only if it&#39;s a first buy. |  [optional] |
|**isMinMaxInstallments** | **Boolean** | Set if the campaign audience will be applied considering a minimum and maximum values for installments. |  [optional] |
|**isSlaSelected** | **Boolean** | Applies selected discount only when one of the defined shipping method is selected by the customer. |  [optional] |
|**itemMaxPrice** | **BigDecimal** | Maximum price of the item. |  [optional] |
|**itemMinPrice** | **BigDecimal** | Minimum price of the item. |  [optional] |
|**listBrand1BuyTogether** | **List&lt;Object&gt;** | Brand first list for the promotion **Buy Together. |  [optional] |
|**listCategory1BuyTogether** | [**List&lt;SetcampaignconfigurationRequestTargetConfigurationsInnerListCategory1BuyTogetherInner&gt;**](SetcampaignconfigurationRequestTargetConfigurationsInnerListCategory1BuyTogetherInner.md) | Category first list for the promotion **Buy Together**. |  [optional] |
|**listSku1BuyTogether** | **List&lt;Object&gt;** | SKU first list for the promotion **Buy Together**. |  [optional] |
|**listSku2BuyTogether** | **List&lt;Object&gt;** | SKU second list for the promotion **Buy Together**. |  [optional] |
|**marketingTags** | **List&lt;String&gt;** | Array with all campaign audience&#39;s marketing tags. |  [optional] |
|**marketingTagsAreNotInclusive** | **Boolean** | Shows if marketing tags are not inclusive. |  [optional] |
|**maxInstallment** | **Integer** | Maximum value for installment. |  [optional] |
|**maxUsage** | **Integer** | Defines how many times the campaign audience can be used. |  [optional] |
|**maxUsagePerClient** | **Integer** | Defines if the campaign audience can be used multiple times per client. |  [optional] |
|**merchants** | **List&lt;Object&gt;** |  |  [optional] |
|**minInstallment** | **Integer** | Minimum value for installment. |  [optional] |
|**minimumQuantityBuyTogether** | **Integer** | Minimum quantity for **Buy Together** promotion. |  [optional] |
|**multipleUsePerClient** | **Boolean** | Defines if the campaign audience can be used multiple times per client. |  [optional] |
|**name** | **String** | Target audience name. |  [optional] |
|**origin** | **String** | Shows the campaign audience origin, &#x60;Marketplace&#x60; or &#x60;Fulfillment&#x60;.  Read [Difference between orders with marketplace and fulfillment sources](https://help.vtex.com/en/tutorial/what-are-orders-with-marketplace-source-and-orders-with-fulfillment-source--6eVYrmUAwMOeKICU2KuG06) for more information. |  [optional] |
|**paymentsMethods** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestPaymentsMethodsInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestPaymentsMethodsInner.md) | Array composed by all the Payments Methods. |  [optional] |
|**paymentsRules** | **List&lt;Object&gt;** |  |  [optional] |
|**percentualDiscountValueList** | **List&lt;BigDecimal&gt;** | Percentual discount value list. |  [optional] |
|**products** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestProductsInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestProductsInner.md) | Object composed by the products that will activate or deactivate the campaign audience. |  [optional] |
|**productsAreInclusive** | **Boolean** | If set to &#x60;true&#x60;, this campaign audience will be applied to any product present on the &#x60;products&#x60; field. If set to &#x60;false&#x60;, products present on that field will make this campaign audience not to be applied. |  [optional] |
|**productsSpecifications** | **List&lt;Object&gt;** |  |  [optional] |
|**quantityToAffectBuyTogether** | **Integer** | Quantity to affect **Buy Together** promotion. |  [optional] |
|**restrictionsBins** | **List&lt;String&gt;** | The discount will be granted if the card&#39;s BIN is given. |  [optional] |
|**shouldDistributeDiscountAmongMatchedItems** | **Boolean** | Should distribute discount among matched items. |  [optional] |
|**skus** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestSkusInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestSkusInner.md) | Object composed by the SKUs that will activate or deactivate the campaign audience. |  [optional] |
|**skusAreInclusive** | **Boolean** | If set to &#x60;true&#x60;, this campaign audience will be applied to any SKU present on the &#x60;skus&#x60; field. If set to &#x60;false&#x60;, SKUs present on that field will make this campaign audience not to be applied. |  [optional] |
|**slasIds** | **List&lt;String&gt;** | The discount will be granted if the shipping method is the same as the one given. |  [optional] |
|**stores** | **List&lt;Object&gt;** |  |  [optional] |
|**storesAreInclusive** | **Boolean** |  |  [optional] |
|**totalValueCeling** | **BigDecimal** | Maximum chart value to active the campaign audience. |  [optional] |
|**totalValueFloor** | **BigDecimal** | Minimum chart value to active the campaign audience. |  [optional] |
|**totalValueIncludeAllItems** | **Boolean** |  |  [optional] |
|**totalValueMode** | **String** | Total chart value to active the campaign audience. |  [optional] |
|**totalValuePurchase** | **BigDecimal** | Total value a client must have in past orders to active the campaign audience. |  [optional] |
|**useNewProgressiveAlgorithm** | **Boolean** | Use new progressive algorithm. |  [optional] |
|**zipCodeRanges** | [**List&lt;SetcampaignconfigurationRequestTargetConfigurationsInnerZipCodeRangesInner&gt;**](SetcampaignconfigurationRequestTargetConfigurationsInnerZipCodeRangesInner.md) | Range of the zip code that applies the campaign audience. |  [optional] |



