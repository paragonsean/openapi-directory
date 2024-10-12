

# Getallpricetablesandrules200ResponseInnerRulesInnerContext

Rule Context is a group of filters to be checked at an item level when applying the rule. If all those filters check out, the rule will be applied for that item, unless there is a fixed price for that item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brands** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Brands that an item should have to be eligible for the rule. Format: key: &#x60;brandId&#x60;, value: &#x60;brandName&#x60;. |  [optional] |
|**categories** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Categories that an item should have to be eligible for the rule. Format: key: &#x60;categoryId&#x60;, value: &#x60;categoryName&#x60;. |  [optional] |
|**dateRange** | [**Getallpricetablesandrules200ResponseInnerRulesInnerContextDateRange**](Getallpricetablesandrules200ResponseInnerRulesInnerContextDateRange.md) |  |  [optional] |
|**internalCategories** | **Object** | Internal Categories. |  [optional] |
|**markupRange** | [**Getallpricetablesandrules200ResponseInnerRulesInnerContextMarkupRange**](Getallpricetablesandrules200ResponseInnerRulesInnerContextMarkupRange.md) |  |  [optional] |
|**stockStatuses** | **Object** | Stock statuses. |  [optional] |



