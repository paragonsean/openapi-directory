

# CreateOrUpdateCalculatorConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**absoluteShippingDiscountValue** | **BigDecimal** | Maximum shipping value. |  [optional] |
|**accumulateWithManualPrice** | **Boolean** | Allows the promotion to apply to products whose prices have been manually added by a call-center operator. |  [optional] |
|**activateGiftsMultiplier** | **Boolean** | If set as &#x60;true&#x60;, it activates gifts Multiplier. |  [optional] |
|**activeDaysOfWeek** | **List&lt;String&gt;** | Defines which days of the week the Promotion or Tax will applied. |  [optional] |
|**affiliates** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestAffiliatesInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestAffiliatesInner.md) | Marketplace order identifier. The discount will apply to selected affiliates. |  [optional] |
|**applyToAllShippings** | **Boolean** | Promotion or Tax will be applied to all kind of shipping. |  [optional] |
|**areSalesChannelIdsExclusive** | **Boolean** | If set to &#x60;false&#x60;, this Promotion or Tax will be applied to any trade policies present on the &#x60;idsSalesChannel&#x60; field. If set to &#x60;true&#x60;, trade policies present on that field will make this Promotion or Tax not to be applied. |  [optional] |
|**beginDateUtc** | **String** | Promotion or Tax Begin Date (UTC). |  [optional] |
|**brands** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestBrandsInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestBrandsInner.md) | Object composed by the brands that will activate or deactivate the Promotion or Tax. |  [optional] |
|**brandsAreInclusive** | **Boolean** | If set to &#x60;true&#x60;, this Promotion or Tax will be applied to any brand present on the &#x60;brands&#x60; field. If set to &#x60;false&#x60;, brands present on that field will make this Promotion or Tax not to be applied. |  [optional] |
|**campaigns** | **List&lt;Object&gt;** | Campaign Audiences that activate this Promotion or Tax. |  [optional] |
|**cardIssuers** | **List&lt;Object&gt;** |  |  [optional] |
|**categories** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestCategoriesInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestCategoriesInner.md) | Object composed by the categories that will activate or deactivate the Promotion or Tax. |  [optional] |
|**categoriesAreInclusive** | **Boolean** | If set to &#x60;true&#x60;, this Promotion or Tax will be applied to any category present on the &#x60;categories&#x60; field. If set to &#x60;false&#x60;, categories present on that field will make this Promotion or Tax not to be applied. |  [optional] |
|**clusterExpressions** | **List&lt;String&gt;** | An expression to use with clusters. |  [optional] |
|**collections** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestCollectionsInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestCollectionsInner.md) | Object composed by the collections that will activate or deactivate the Promotion or Tax. |  [optional] |
|**collections1BuyTogether** | **List&lt;String&gt;** | Collections that will generate the Promotion, type **Buy Together**, **More for less**, **Progressive Discount**, **Buy One Get One**. |  [optional] |
|**collections2BuyTogether** | **List&lt;Object&gt;** |  |  [optional] |
|**collectionsIsInclusive** | **Boolean** | If set to &#x60;true&#x60;, this Promotion or Tax will be applied to any collection present on the &#x60;collections&#x60; field. If set to &#x60;false&#x60;, collections present on that field will make this Promotion or Tax not to be applied. |  [optional] |
|**compareListPriceAndPrice** | **Boolean** | If the **List Price** and **Price** are the same. |  [optional] |
|**conditionsIds** | **List&lt;String&gt;** | Array with conditions IDs. |  [optional] |
|**coupon** | **List&lt;Object&gt;** |  |  [optional] |
|**cumulative** | **Boolean** | Defines if a Promotion or Tax can accumulate with another one. (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  [optional] |
|**daysAgoOfPurchases** | **Integer** | Number of days that are considered to add the purchase history. |  [optional] |
|**description** | **String** | Internal description of the Promotion or Tax. |  [optional] |
|**disableDeal** | **Boolean** |  |  [optional] |
|**discountType** | **String** | The type of discount that will apply to the promotion. |  [optional] |
|**enableBuyTogetherPerSku** | **Boolean** | Enable **Buy Together** per SKU. |  [optional] |
|**endDateUtc** | **String** | Promotion or Tax End Date (UTC). |  [optional] |
|**firstBuyIsProfileOptimistic** | **Boolean** | Applies the discount even if the user is not logged. |  [optional] |
|**giftListTypes** | **List&lt;String&gt;** | Gifts List Type. |  [optional] |
|**idCalculatorConfiguration** | **String** | Promotion ID or Tax ID. |  [optional] |
|**idSeller** | **String** | Seller Name. |  [optional] |
|**idSellerIsInclusive** | **Boolean** | If set to &#x60;true&#x60;, this Promotion or Tax will be applied to any seller present on the &#x60;idSeller&#x60; field. If set to &#x60;false&#x60;, sellers present on that field will make this Promotion or Tax not to be applied. |  [optional] |
|**idsSalesChannel** | **List&lt;String&gt;** | List of Trade Policies that activate this Promotion or Tax. |  [optional] |
|**installment** | **Integer** |  |  [optional] |
|**isActive** | **Boolean** | If set as &#x60;true&#x60; the Promotion or Tax is activated. If set as &#x60;false&#x60; the Promotion or Tax is deactivated. |  [optional] |
|**isArchived** | **Boolean** | If set as &#x60;true&#x60; the Promotion or Tax is archived. If set as &#x60;false&#x60; the Promotion or Tax is not archived. |  [optional] |
|**isDifferentListPriceAndPrice** | **Boolean** | Applies the Promotion or Tax only if the list price and price is different. |  [optional] |
|**isFeatured** | **Boolean** | Insert a flag with the promotion name used in the product&#39;s window display and page. |  [optional] |
|**isFirstBuy** | **Boolean** | Applies the discount only if it&#39;s a first buy. |  [optional] |
|**isMinMaxInstallments** | **Boolean** | Set if the Promotion or Tax will be applied considering a minimum and maximum values for installments. |  [optional] |
|**isSlaSelected** | **Boolean** | Applies selected discount only when one of the defined shipping method is selected by the customer. |  [optional] |
|**itemMaxPrice** | **BigDecimal** | Maximum price of the item. |  [optional] |
|**itemMinPrice** | **BigDecimal** | Minimum price of the item. |  [optional] |
|**lastModified** | **String** | Date when the Promotion or Tax was last modified. |  [optional] |
|**listSku1BuyTogether** | **List&lt;Object&gt;** | SKU first list for the promotion **Buy Together**. |  [optional] |
|**listSku2BuyTogether** | **List&lt;Object&gt;** | SKU second list for the promotion **Buy Together**. |  [optional] |
|**marketingTags** | **List&lt;String&gt;** | Promotion or Tax Marketing tags. |  [optional] |
|**marketingTagsAreNotInclusive** | **Boolean** | If set to &#x60;false&#x60;, this Promotion or Tax will be applied to any marketing tag present on the &#x60;marketingTags&#x60; field. If set to &#x60;true&#x60;, marketing tags present on that field will make this Promotion or Tax not to be applied. |  [optional] |
|**maxInstallment** | **Integer** | Maximum value for installment. |  [optional] |
|**maxNumberOfAffectedItems** | **Integer** | The maximum number of affected items for a promotion. |  [optional] |
|**maxNumberOfAffectedItemsGroupKey** | **String** | The maximum number of affected items by group key for a promotion. |  [optional] |
|**maxPricesPerItems** | **List&lt;Object&gt;** |  |  [optional] |
|**maxUsage** | **Integer** | Defines how many times the Promotion or Tax can be used. |  [optional] |
|**maxUsagePerClient** | **Integer** | Defines if the promotion can be used multiple times per client. |  [optional] |
|**maximumUnitPriceDiscount** | **BigDecimal** | The maximum price for each item of the purchase will be the price set up. |  [optional] |
|**merchants** | **List&lt;Object&gt;** |  |  [optional] |
|**minInstallment** | **Integer** | Minimum value for installment. |  [optional] |
|**minimumQuantityBuyTogether** | **Integer** | Minimum quantity for **Buy Together** promotion. |  [optional] |
|**multipleUsePerClient** | **Boolean** | Defines if the promotion can be used multiple times per client. |  [optional] |
|**name** | **String** | Promotion name or Tax name. |  [optional] |
|**newOffset** | **BigDecimal** | New time offset from UTC in seconds. |  [optional] |
|**nominalDiscountValue** | **BigDecimal** | Exact discount to be applied for the total purchase value. |  [optional] |
|**nominalRewardValue** | **BigDecimal** | Nominal value for rewards program. |  [optional] |
|**nominalShippingDiscountValue** | **BigDecimal** | Exact discount to be applied for the shipping value. |  [optional] |
|**nominalTax** | **BigDecimal** | Nominal Tax. |  [optional] |
|**offset** | **Integer** | Time offset from UTC in seconds. |  [optional] |
|**orderStatusRewardValue** | **String** | Order status reward value. |  [optional] |
|**origin** | **String** | Origin of the Promotion or Tax, &#x60;marketplace&#x60; or &#x60;Fulfillment&#x60;.  Read [Difference between orders with marketplace and fulfillment sources](https://help.vtex.com/en/tutorial/what-are-orders-with-marketplace-source-and-orders-with-fulfillment-source--6eVYrmUAwMOeKICU2KuG06) for more information. |  [optional] |
|**paymentsMethods** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestPaymentsMethodsInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestPaymentsMethodsInner.md) | Array composed by all the Payments Methods that activate this Promotion or Tax. |  [optional] |
|**paymentsRules** | **List&lt;Object&gt;** |  |  [optional] |
|**percentualDiscountValue** | **BigDecimal** | Percentage discount to be applied for total purchase value. |  [optional] |
|**percentualDiscountValueList** | **List&lt;BigDecimal&gt;** | Percentual discount value list. |  [optional] |
|**percentualDiscountValueList1** | **BigDecimal** | Valid discounts for the SKUs in &#x60;listSku1BuyTogether&#x60;, discount list used for Buy Together Promotions. |  [optional] |
|**percentualDiscountValueList2** | **BigDecimal** | Equivalent to &#x60;percentualDiscountValueList1&#x60;. |  [optional] |
|**percentualRewardValue** | **BigDecimal** | Percentage value for rewards program. |  [optional] |
|**percentualShippingDiscountValue** | **BigDecimal** | Percentage discount to be applied for shipping value. |  [optional] |
|**percentualTax** | **BigDecimal** | Percentual Tax over purchase total value. |  [optional] |
|**products** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestProductsInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestProductsInner.md) | Object composed by the products that will activate or deactivate the Promotion or Tax. |  [optional] |
|**productsAreInclusive** | **Boolean** | If set to &#x60;true&#x60;, this Promotion or Tax will be applied to any product present on the &#x60;products&#x60; field. If set to &#x60;false&#x60;, products present on that field will make this Promotion or Tax not to be applied. |  [optional] |
|**productsSpecifications** | **List&lt;Object&gt;** |  |  [optional] |
|**quantityToAffectBuyTogether** | **Integer** | Quantity to affect **Buy Together** promotion. |  [optional] |
|**rebatePercentualDiscountValue** | **BigDecimal** | Percentual Shipping Discount Value. |  [optional] |
|**restrictionsBins** | **List&lt;String&gt;** | The discount will be granted if the card&#39;s BIN is given. |  [optional] |
|**shippingPercentualTax** | **BigDecimal** | Shipping Percentual Tax over purchase total value. |  [optional] |
|**shouldDistributeDiscountAmongMatchedItems** | **Boolean** | Should distribute discount among matched items. |  [optional] |
|**skus** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestSkusInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestSkusInner.md) | Object composed by the SKUs that will activate or deactivate the Promotion or Tax. |  [optional] |
|**skusAreInclusive** | **Boolean** | If set to &#x60;true&#x60;, this Promotion or Tax will be applied to any SKU present on the &#x60;skus&#x60; field. If set to &#x60;false&#x60;, SKUs present on that field will make this Promotion or Tax not to be applied. |  [optional] |
|**skusGift** | [**CreateOrUpdateCalculatorConfigurationRequestSkusGift**](CreateOrUpdateCalculatorConfigurationRequestSkusGift.md) |  |  [optional] |
|**slasIds** | **List&lt;String&gt;** | The discount will be granted if the shipping method is the same as the one given. |  [optional] |
|**stores** | **List&lt;Object&gt;** |  |  [optional] |
|**storesAreInclusive** | **Boolean** |  |  [optional] |
|**totalValueCeling** | **BigDecimal** | Maximum chart value to activate the Promotion or Tax. |  [optional] |
|**totalValueFloor** | **BigDecimal** | Minimum chart value to activate the Promotion or Tax. |  [optional] |
|**totalValueIncludeAllItems** | **Boolean** |  |  [optional] |
|**totalValueMode** | **String** | Defines if products that already are receiving a promotion will be considered on the chart total value. There are three options available: &#x60;IncludeMatchedItems&#x60;, &#x60;ExcludeMatchedItems&#x60;, &#x60;AllItems&#x60;. |  [optional] |
|**totalValuePurchase** | **BigDecimal** | Total value a client must have in past orders to activate the Promotion or Tax. |  [optional] |
|**type** | **String** | Defines what is the type of the promotion or indicates if it is a tax. Possible values: &#x60;regular&#x60; ([Regular Promotion](https://help.vtex.com/tutorial/regular-promotion--tutorials_327)), &#x60;combo&#x60; ([Buy Together](https://help.vtex.com/en/tutorial/buy-together--tutorials_323)), &#x60;forThePriceOf&#x60; ([More for Less](https://help.vtex.com/en/tutorial/creating-a-more-for-less-promotion--tutorials_325)), &#x60;progressive&#x60; ([Progressive Discount](https://help.vtex.com/en/tutorial/progressive-discount--tutorials_324)), &#x60;buyAndWin&#x60; ([Buy One Get One](https://help.vtex.com/en/tutorial/buy-one-get-one--tutorials_322)), &#x60;maxPricePerItem&#x60; (Deprecated), &#x60;campaign&#x60; ([Campaign Promotion](https://help.vtex.com/en/tutorial/campaign-promotion--1ChYXhK2AQGuS6wAqS8Ume)), &#x60;tax&#x60; (Tax), &#x60;multipleEffects&#x60; (Multiple Effects). |  [optional] |
|**useNewProgressiveAlgorithm** | **Boolean** | Use new progressive algorithm. |  [optional] |
|**utmCampaign** | **String** | Coupon utmCampaign code. |  [optional] |
|**utmSource** | **String** | Coupon utmSource code. |  [optional] |
|**zipCodeRanges** | [**List&lt;CreateOrUpdateCalculatorConfigurationRequestZipCodeRangesInner&gt;**](CreateOrUpdateCalculatorConfigurationRequestZipCodeRangesInner.md) | Range of the zip code that applies the promotion. |  [optional] |



