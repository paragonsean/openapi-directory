

# EcommerceProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | [**List&lt;ProductCategoriesInner&gt;**](ProductCategoriesInner.md) | An array of categories for the product, used for organization and searching. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**description** | **String** | A detailed description of the product. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [readonly] |
|**images** | [**List&lt;ProductImagesInner&gt;**](ProductImagesInner.md) | An array of image URLs for the product. |  [optional] |
|**inventoryQuantity** | **String** | The quantity of the product in stock. |  [optional] |
|**name** | **String** | The name of the product as it should be displayed to customers. |  [optional] |
|**options** | [**List&lt;ProductOptionsInner&gt;**](ProductOptionsInner.md) | An array of options for the product. |  [optional] |
|**price** | **String** | The price of the product. |  [optional] |
|**sku** | **String** | The stock keeping unit of the product. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the product (active or archived). |  [optional] |
|**tags** | **List&lt;String&gt;** | An array of tags for the product, used for organization and searching. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**variants** | [**List&lt;EcommerceProductVariantsInner&gt;**](EcommerceProductVariantsInner.md) |  |  [optional] |
|**weight** | **String** | The weight of the product. |  [optional] |
|**weightUnit** | **String** | The unit of measurement for the weight of the product. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



