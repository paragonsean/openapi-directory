

# CatalogQuery

A query composed of one or more different types of filters to narrow the scope of targeted objects when calling the `SearchCatalogObjects` endpoint.  Although a query can have multiple filters, only certain query types can be combined per call to [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects). Any combination of the following types may be used together: - [exact_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQueryExact) - [prefix_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQueryPrefix) - [range_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQueryRange) - [sorted_attribute_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQuerySortedAttribute) - [text_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQueryText) All other query types cannot be combined with any others.  When a query filter is based on an attribute, the attribute must be searchable. Searchable attributes are listed as follows, along their parent types that can be searched for with applicable query filters.  * Searchable attribute and objects queryable by searchable attributes ** - `name`:  `CatalogItem`, `CatalogItemVariation`, `CatalogCategory`, `CatalogTax`, `CatalogDiscount`, `CatalogModifier`, 'CatalogModifierList`, `CatalogItemOption`, `CatalogItemOptionValue` - `description`: `CatalogItem`, `CatalogItemOptionValue` - `abbreviation`: `CatalogItem` - `upc`: `CatalogItemVariation` - `sku`: `CatalogItemVariation` - `caption`: `CatalogImage` - `display_name`: `CatalogItemOption`  For example, to search for [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) objects by searchable attributes, you can use the `\"name\"`, `\"description\"`, or `\"abbreviation\"` attribute in an applicable query filter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exactQuery** | [**CatalogQueryExact**](CatalogQueryExact.md) |  |  [optional] |
|**itemVariationsForItemOptionValuesQuery** | [**CatalogQueryItemVariationsForItemOptionValues**](CatalogQueryItemVariationsForItemOptionValues.md) |  |  [optional] |
|**itemsForItemOptionsQuery** | [**CatalogQueryItemsForItemOptions**](CatalogQueryItemsForItemOptions.md) |  |  [optional] |
|**itemsForModifierListQuery** | [**CatalogQueryItemsForModifierList**](CatalogQueryItemsForModifierList.md) |  |  [optional] |
|**itemsForTaxQuery** | [**CatalogQueryItemsForTax**](CatalogQueryItemsForTax.md) |  |  [optional] |
|**prefixQuery** | [**CatalogQueryPrefix**](CatalogQueryPrefix.md) |  |  [optional] |
|**rangeQuery** | [**CatalogQueryRange**](CatalogQueryRange.md) |  |  [optional] |
|**setQuery** | [**CatalogQuerySet**](CatalogQuerySet.md) |  |  [optional] |
|**sortedAttributeQuery** | [**CatalogQuerySortedAttribute**](CatalogQuerySortedAttribute.md) |  |  [optional] |
|**textQuery** | [**CatalogQueryText**](CatalogQueryText.md) |  |  [optional] |



