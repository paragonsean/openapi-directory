# SquareConnectApi.CatalogCustomAttributeDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedObjectTypes** | **[String]** | The set of Catalog Object Types that this Custom Attribute may be applied to. Currently, only &#x60;ITEM&#x60; and &#x60;ITEM_VARIATION&#x60; are allowed. At least one type must be included. | 
**appVisibility** | **String** | The visibility of a custom attribute to applications other than the application that created the attribute. | [optional] 
**customAttributeUsageCount** | **Number** | __Read-only.__ The number of custom attributes that reference this custom attribute definition. Set by the server in response to a ListCatalog request with &#x60;include_counts&#x60; set to &#x60;true&#x60;.  If the actual count is greater than 100, &#x60;custom_attribute_usage_count&#x60; will be set to &#x60;100&#x60;. | [optional] 
**description** | **String** | Seller-oriented description of the meaning of this Custom Attribute, any constraints that the seller should observe, etc. May be displayed as a tooltip in Square UIs. | [optional] 
**key** | **String** | The name of the desired custom attribute key that can be used to access the custom attribute value on catalog objects. Cannot be modified after the custom attribute definition has been created. Must be between 1 and 60 characters, and may only contain the characters &#x60;[a-zA-Z0-9_-]&#x60;. | [optional] 
**name** | **String** |  The name of this definition for API and seller-facing UI purposes. The name must be unique within the (merchant, application) pair. Required. May not be empty and may not exceed 255 characters. Can be modified after creation. | 
**numberConfig** | [**CatalogCustomAttributeDefinitionNumberConfig**](CatalogCustomAttributeDefinitionNumberConfig.md) |  | [optional] 
**selectionConfig** | [**CatalogCustomAttributeDefinitionSelectionConfig**](CatalogCustomAttributeDefinitionSelectionConfig.md) |  | [optional] 
**sellerVisibility** | **String** | The visibility of a custom attribute in seller-facing UIs (including Square Point of Sale applications and Square Dashboard). May be modified. | [optional] 
**sourceApplication** | [**SourceApplication**](SourceApplication.md) |  | [optional] 
**stringConfig** | [**CatalogCustomAttributeDefinitionStringConfig**](CatalogCustomAttributeDefinitionStringConfig.md) |  | [optional] 
**type** | **String** | The type of this custom attribute. Cannot be modified after creation. Required. | 


