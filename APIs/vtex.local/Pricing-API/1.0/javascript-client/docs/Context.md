# PricingApi.Context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brands** | **{String: {String: String}}** | Brands that an item should have to be eligible for the rule. Format: key: &#x60;brandId&#x60;, value: &#x60;brandName&#x60;. | 
**categories** | **{String: {String: String}}** | Categories that an item should have to be eligible for the rule. Format: key: &#x60;categoryId&#x60;, value: &#x60;categoryName&#x60;. | 
**dateRange** | [**DateRange**](DateRange.md) |  | 
**internalCategories** | **Object** | Internal Categories. | [optional] 
**markupRange** | [**MarkupRange**](MarkupRange.md) |  | 
**stockStatuses** | **Object** | Stock statuses. | [optional] 


