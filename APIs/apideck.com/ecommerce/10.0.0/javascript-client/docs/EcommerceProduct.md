# EcommerceApi.EcommerceProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**[ProductCategoriesInner]**](ProductCategoriesInner.md) | An array of categories for the product, used for organization and searching. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**description** | **String** | A detailed description of the product. | [optional] 
**id** | **String** | A unique identifier for an object. | [readonly] 
**images** | [**[ProductImagesInner]**](ProductImagesInner.md) | An array of image URLs for the product. | [optional] 
**inventoryQuantity** | **String** | The quantity of the product in stock. | [optional] 
**name** | **String** | The name of the product as it should be displayed to customers. | [optional] 
**options** | [**[ProductOptionsInner]**](ProductOptionsInner.md) | An array of options for the product. | [optional] 
**price** | **String** | The price of the product. | [optional] 
**sku** | **String** | The stock keeping unit of the product. | [optional] 
**status** | **String** | The current status of the product (active or archived). | [optional] 
**tags** | **[String]** | An array of tags for the product, used for organization and searching. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**variants** | [**[EcommerceProductVariantsInner]**](EcommerceProductVariantsInner.md) |  | [optional] 
**weight** | **String** | The weight of the product. | [optional] 
**weightUnit** | **String** | The unit of measurement for the weight of the product. | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `archived` (value: `"archived"`)




