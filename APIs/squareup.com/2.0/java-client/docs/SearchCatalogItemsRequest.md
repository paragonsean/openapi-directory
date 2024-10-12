

# SearchCatalogItemsRequest

Defines the request body for the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryIds** | **List&lt;String&gt;** | The category id query expression to return items containing the specified category IDs. |  [optional] |
|**cursor** | **String** | The pagination token, returned in the previous response, used to fetch the next batch of pending results. |  [optional] |
|**customAttributeFilters** | [**List&lt;CustomAttributeFilter&gt;**](CustomAttributeFilter.md) | The customer-attribute filter to return items or item variations matching the specified custom attribute expressions. A maximum number of 10 custom attribute expressions are supported in a single call to the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint. |  [optional] |
|**enabledLocationIds** | **List&lt;String&gt;** | The enabled-location query expression to return items and item variations having specified enabled locations. |  [optional] |
|**limit** | **Integer** | The maximum number of results to return per page. The default value is 100. |  [optional] |
|**productTypes** | **List&lt;String&gt;** | The product types query expression to return items or item variations having the specified product types. |  [optional] |
|**sortOrder** | **String** | The order to sort the results by item names. The default sort order is ascending (&#x60;ASC&#x60;). |  [optional] |
|**stockLevels** | **List&lt;String&gt;** | The stock-level query expression to return item variations with the specified stock levels. |  [optional] |
|**textFilter** | **String** | The text filter expression to return items or item variations containing specified text in the &#x60;name&#x60;, &#x60;description&#x60;, or &#x60;abbreviation&#x60; attribute value of an item, or in the &#x60;name&#x60;, &#x60;sku&#x60;, or &#x60;upc&#x60; attribute value of an item variation. |  [optional] |



