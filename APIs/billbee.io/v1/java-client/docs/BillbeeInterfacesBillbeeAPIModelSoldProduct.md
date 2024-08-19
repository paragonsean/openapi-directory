

# BillbeeInterfacesBillbeeAPIModelSoldProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billbeeId** | **Long** | The Billbee internal id of the linked product |  [optional] |
|**countryOfOrigin** | **String** | The country where this article was made |  [optional] |
|**EAN** | **String** | The EAN / GTIN of this product |  [optional] |
|**id** | **String** | The id of this product in the external system |  [optional] |
|**images** | [**List&lt;BillbeeInterfacesBillbeeAPIModelProductImage&gt;**](BillbeeInterfacesBillbeeAPIModelProductImage.md) | The images of this product |  [optional] |
|**isDigital** | **Boolean** | True if the product is a digital good (download etc.), false if not |  [optional] |
|**oldId** | **String** | This is for migration scenarios when the internal id of a product changes  I.E. Etsy when switching to the new inventory management, the ids for variants will change. |  [optional] |
|**platformData** | **String** | Optional platform specific Data as serialized JSON Object for the product |  [optional] |
|**SKU** | **String** | The SKU of this product |  [optional] |
|**skuOrId** | **String** | The SKU of this product or the id if the SKU is empty |  [optional] [readonly] |
|**taRICCode** | **String** | The TARIC code |  [optional] |
|**title** | **String** | The name of this product |  [optional] |
|**type** | **Integer** | Indicates whether the article is 1 &#x3D; normal or 2 &#x3D; BOM |  [optional] |
|**weight** | **Integer** | Weight of one item in gram |  [optional] |



