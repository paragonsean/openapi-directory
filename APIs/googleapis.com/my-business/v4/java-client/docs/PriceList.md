

# PriceList

A list of item price information. Price lists are structured as one or more price lists, each containing one or more sections with one or more items. For example, food price lists may represent breakfast/lunch/dinner menus, with sections for burgers/steak/seafood.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labels** | [**List&lt;Label&gt;**](Label.md) | Required. Language-tagged labels for the price list. |  [optional] |
|**priceListId** | **String** | Required. ID for the price list. Price list, section, and item IDs cannot be duplicated within this Location. |  [optional] |
|**sections** | [**List&lt;Section&gt;**](Section.md) | Required. Sections for this price list. Each price list must contain at least one section. |  [optional] |
|**sourceUrl** | **String** | Optional source URL of where the price list was retrieved from. For example, this could be the URL of the page that was automatically scraped to populate the menu information. |  [optional] |



