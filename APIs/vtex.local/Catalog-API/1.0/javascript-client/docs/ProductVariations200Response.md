# CatalogApi.ProductVariations200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **Boolean** | Defines if the product is available (&#x60;true&#x60;) or not (&#x60;false&#x60;). | [optional] 
**dimensions** | **[String]** | Lists SKU specifications. | [optional] 
**dimensionsInputType** | **{String: String}** | Lists SKU specifications and their field type, in the following format: &#x60;\&quot;{specificationName}\&quot;:\&quot;{fieldType}\&quot;&#x60;. | [optional] 
**dimensionsMap** | **{String: [Object]}** | Lists SKU specifications and their possible values inside arrays. | [optional] 
**displayMode** | **String** | Defines the mannner SKUs are displayed. | [optional] 
**name** | **String** | Product name. | [optional] 
**productId** | **Number** | Product’s unique numerical identifier. | [optional] 
**salesChannel** | **String** | Trade policy ID. | [optional] 
**skus** | [**[ProductVariations200ResponseSkusInner]**](ProductVariations200ResponseSkusInner.md) | Array containing information about the product&#39;s SKUs. | [optional] 


