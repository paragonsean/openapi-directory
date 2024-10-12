# BeezUpMerchantApi.TrackedExternalOrderProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**margin** | **String** | The product&#39;s margin for the external order. This property is voluntarily a string because the value could be an invalid one | [optional] 
**productActive** | **Boolean** | We tried to get the catalog product if it&#39;s still active based on the product SKU. This property can be null, if we cannot found the product. This is possible if the product is not referenced in the imported catalog. | [optional] 
**productId** | **String** | We tried to get the catalog product identifier based on the product SKU. This property can be null, if we cannot found the product. This is possible if the product is not referenced in the imported catalog. | [optional] 
**productImageUrl** | **String** | We tried to get the catalog product image Url based on the product SKU. This property can be null, if we cannot found the product. This is possible if the product is not referenced in the imported catalog. | [optional] 
**productSku** | **String** | The product sku received for the external order | 
**productTitle** | **String** | We tried to get the catalog product title based on the product SKU. This property can be null, if we cannot found the product. This is possible if the product is not referenced in the imported catalog. | [optional] 
**quantity** | **String** | The quantity of this product for the external order. This property is voluntarily a string because the value could be an invalid one | [optional] 
**unitPrice** | **String** | The product&#39;s unit price for the external order. This property is voluntarily a string because the value could be an invalid one. | [optional] 


