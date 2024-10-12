

# GetProductsRequest

The request message to get products based on these filters

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryPath** | **List&lt;String&gt;** | The catalog category path |  [optional] |
|**columnIdList** | **List&lt;String&gt;** |  |  [optional] |
|**ean** | **String** | Search for product by ean |  [optional] |
|**exists** | **Boolean** | Search for existing products or not. If null you will received both. |  [optional] |
|**mpn** | **String** | Search for product by mpn |  [optional] |
|**orderByCatalogColumnId** | **String** | The catalog column identifier (catalog or custom column) |  [optional] |
|**pageNumber** | **Integer** | Indicates the page number |  |
|**pageSize** | **Integer** | Indicate the item count per page |  |
|**productIdList** | **List&lt;String&gt;** | Filter with a list of product identifier |  [optional] |
|**sku** | **String** | Search for product by sku |  [optional] |
|**title** | **String** | Search for products containing this title |  [optional] |
|**withoutSubCategories** | **Boolean** | Do not retrieve sub categories. By default, this value is set to false |  [optional] |



