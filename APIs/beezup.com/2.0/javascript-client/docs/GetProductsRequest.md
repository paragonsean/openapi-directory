# BeezUpMerchantApi.GetProductsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryPath** | **[String]** | The catalog category path | [optional] 
**columnIdList** | **[String]** |  | [optional] 
**ean** | **String** | Search for product by ean | [optional] 
**exists** | **Boolean** | Search for existing products or not. If null you will received both. | [optional] 
**mpn** | **String** | Search for product by mpn | [optional] 
**orderByCatalogColumnId** | **String** | The catalog column identifier (catalog or custom column) | [optional] 
**pageNumber** | **Number** | Indicates the page number | 
**pageSize** | **Number** | Indicate the item count per page | 
**productIdList** | **[String]** | Filter with a list of product identifier | [optional] 
**sku** | **String** | Search for product by sku | [optional] 
**title** | **String** | Search for products containing this title | [optional] 
**withoutSubCategories** | **Boolean** | Do not retrieve sub categories. By default, this value is set to false | [optional] 


