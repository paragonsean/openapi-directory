

# CatalogCustomAttributeValue

An instance of a custom attribute. Custom attributes can be defined and added to `ITEM` and `ITEM_VARIATION` type catalog objects. [Read more about custom attributes](https://developer.squareup.com/docs/catalog-api/add-custom-attributes).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**booleanValue** | **Boolean** | A &#x60;true&#x60; or &#x60;false&#x60; value. Populated if &#x60;type&#x60; &#x3D; &#x60;BOOLEAN&#x60;. |  [optional] |
|**customAttributeDefinitionId** | **String** | __Read-only.__ The id of the [CatalogCustomAttributeDefinition](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogCustomAttributeDefinition) this value belongs to. |  [optional] |
|**key** | **String** | __Read-only.__ A copy of key from the associated &#x60;CatalogCustomAttributeDefinition&#x60;. |  [optional] |
|**name** | **String** | The name of the custom attribute. |  [optional] |
|**numberValue** | **String** | Populated if &#x60;type&#x60; &#x3D; &#x60;NUMBER&#x60;. Contains a string representation of a decimal number, using a &#x60;.&#x60; as the decimal separator. |  [optional] |
|**selectionUidValues** | **List&lt;String&gt;** | One or more choices from &#x60;allowed_selections&#x60;. Populated if &#x60;type&#x60; &#x3D; &#x60;SELECTION&#x60;. |  [optional] |
|**stringValue** | **String** | The string value of the custom attribute.  Populated if &#x60;type&#x60; &#x3D; &#x60;STRING&#x60;. |  [optional] |
|**type** | **String** | __Read-only.__ A copy of type from the associated &#x60;CatalogCustomAttributeDefinition&#x60;. |  [optional] |



