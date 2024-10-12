# DealApi.DealItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalImages** | [**[Image]**](Image.md) | The additional images for the deal item. | [optional] 
**categoryAncestorIds** | **[String]** | The IDs of the ancestors for the primary category. | [optional] 
**categoryId** | **String** | The ID of the leaf category for the deal item. A leaf category is the lowest level in a category and has no children. | [optional] 
**commissionable** | **Boolean** | A boolean value specifying whether the listing has commission. | [optional] 
**dealAffiliateWebUrl** | **String** | The deal associated with the item with affiliate attribution. | [optional] 
**dealEndDate** | **String** | The date after which the deal ends. | [optional] 
**dealStartDate** | **String** | The date on which the deal starts. | [optional] 
**dealWebUrl** | **String** | The web URL for the deal associated with the item. | [optional] 
**energyEfficiencyClass** | **String** | A string value specifying the Energy Efficiency class. | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**itemAffiliateWebUrl** | **String** | The item web URL with affiliate attribution. | [optional] 
**itemGroupId** | **String** | The unique identifier for the deal item group. This is the parent item ID for the seller-defined variations. Note: This field is returned for multiple-SKU items. | [optional] 
**itemGroupType** | **String** | An enumeration value that indicates the type of item group. An item group contains items that have various aspect differences, such as color, size, or storage capacity. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/buy/deal/types/api:ItemGroupTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**itemId** | **String** | The unique identifier for the deal item. Note: This field is only returned for single-SKU items. | [optional] 
**itemWebUrl** | **String** | The web URL for the deal item. | [optional] 
**legacyItemId** | **String** | The legacy item ID associated with the deal item. | [optional] 
**marketingPrice** | [**MarketingPrice**](MarketingPrice.md) |  | [optional] 
**price** | [**Amount**](Amount.md) |  | [optional] 
**qualifiedPrograms** | **[String]** | A list of programs applicable to the item. | [optional] 
**shippingOptions** | [**[ShippingOption]**](ShippingOption.md) | The cost required to ship the deal item. | [optional] 
**title** | **String** | The title of the deal item. | [optional] 
**unitPrice** | [**Amount**](Amount.md) |  | [optional] 
**unitPricingMeasure** | **String** | The designation used to specify the quantity of the deal item, such as size, weight, volume, and count. This helps buyers compare prices. For example, the following tells the buyer that the item is 7.99 per 100 grams. &amp;quot;unitPricingMeasure&amp;quot;: &amp;quot;100g&amp;quot;, &amp;quot;unitPrice&amp;quot;: { &amp;nbsp;&amp;nbsp;&amp;quot;value&amp;quot;: &amp;quot;7.99&amp;quot;, &amp;nbsp;&amp;nbsp;&amp;quot;currency&amp;quot;: &amp;quot;GBP&amp;quot; | [optional] 


