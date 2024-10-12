# SwaggerApi2Cart.ProductVariantAdd

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[ProductVariantAddAttributesInner]**](ProductVariantAddAttributesInner.md) | Defines variant&#39;s attributes list | [optional] 
**availableForSale** | **Boolean** | Specifies the set of visible/invisible product&#39;s variants for sale | [optional] [default to true]
**availableForView** | **Boolean** | Specifies the set of visible/invisible product&#39;s variants for users | [optional] [default to true]
**barcode** | **String** | A barcode is a unique code composed of numbers used as a product identifier. | [optional] 
**clearCache** | **Boolean** | Is cache clear required | [optional] [default to true]
**costPrice** | **Number** | Defines new product&#39;s cost price | [optional] 
**countryOfOrigin** | **String** | The country where the inventory item was made | [optional] 
**createdAt** | **String** | Defines the date of entity creation | [optional] 
**description** | **String** | Specifies variant&#39;s description | [optional] 
**harmonizedSystemCode** | **String** | Harmonized System Code. An HSC is a 6-digit identifier that allows participating countries to classify traded goods on a common basis for customs purposes | [optional] 
**height** | **Number** | Defines product&#39;s height | [optional] 
**langId** | **String** | Language id | [optional] 
**length** | **Number** | Defines product&#39;s length | [optional] 
**manageStock** | **Boolean** | Defines inventory tracking for product variant | [optional] 
**manufacturer** | **String** | Specifies the product variant&#39;s manufacturer | [optional] 
**metaDescription** | **String** | Defines unique meta description of a entity | [optional] 
**metaKeywords** | **String** | Defines unique meta keywords for each entity | [optional] 
**metaTitle** | **String** | Defines unique meta title for each entity | [optional] 
**model** | **String** | Specifies variant&#39;s model that has to be added | 
**name** | **String** | Defines variant&#39;s name that has to be added | [optional] 
**price** | **Number** | Defines new product&#39;s variant price | [optional] 
**productId** | **String** | Defines product&#39;s id where the variant has to be added | [optional] 
**quantity** | **Number** | Defines product variant&#39;s quantity that has to be added | [optional] [default to 0]
**shortDescription** | **String** | Defines short description | [optional] 
**sku** | **String** | Defines variant&#39;s sku that has to be added | [optional] 
**specialPrice** | **Number** | Specifies variant&#39;s model that has to be added | [optional] 
**spriceCreate** | **String** | Defines the date of special price creation | [optional] 
**spriceExpire** | **String** | Defines the term of special price offer duration | [optional] 
**spriceModified** | **String** | Defines the date of special price modification | [optional] 
**storeId** | **String** | Add variants specified by store id | [optional] 
**taxClassId** | **String** | Defines tax classes where entity has to be added | [optional] 
**taxable** | **Boolean** | Specifies whether a tax is charged | [optional] [default to true]
**url** | **String** | Defines unique product variant&#39;s URL | [optional] 
**warehouseId** | **String** | This parameter is used for selecting a warehouse where you need to set/modify a product quantity. | [optional] 
**weight** | **Number** | Weight | [optional] [default to 0]
**weightUnit** | **String** | Weight Unit | [optional] 
**width** | **Number** | Defines product&#39;s width | [optional] 


