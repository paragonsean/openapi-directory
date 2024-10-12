

# CatalogItem

A [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) instance of the `ITEM` type, also referred to as an item, in the catalog.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abbreviation** | **String** | The text of the item&#39;s display label in the Square Point of Sale app. Only up to the first five characters of the string are used. This attribute is searchable, and its value length is of Unicode code points. |  [optional] |
|**availableElectronically** | **Boolean** | If &#x60;true&#x60;, the item can be added to electronically fulfilled orders from the merchant&#39;s online store. |  [optional] |
|**availableForPickup** | **Boolean** | If &#x60;true&#x60;, the item can be added to pickup orders from the merchant&#39;s online store. |  [optional] |
|**availableOnline** | **Boolean** | If &#x60;true&#x60;, the item can be added to shipping orders from the merchant&#39;s online store. |  [optional] |
|**categoryId** | **String** | The ID of the item&#39;s category, if any. |  [optional] |
|**description** | **String** | The item&#39;s description. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points. |  [optional] |
|**itemOptions** | [**List&lt;CatalogItemOptionForItem&gt;**](CatalogItemOptionForItem.md) | List of item options IDs for this item. Used to manage and group item variations in a specified order.  Maximum: 6 item options. |  [optional] |
|**labelColor** | **String** | The color of the item&#39;s display label in the Square Point of Sale app. This must be a valid hex color code. |  [optional] |
|**modifierListInfo** | [**List&lt;CatalogItemModifierListInfo&gt;**](CatalogItemModifierListInfo.md) | A set of &#x60;CatalogItemModifierListInfo&#x60; objects representing the modifier lists that apply to this item, along with the overrides and min and max limits that are specific to this item. Modifier lists may also be added to or deleted from an item using &#x60;UpdateItemModifierLists&#x60;. |  [optional] |
|**name** | **String** | The item&#39;s name. This is a searchable attribute for use in applicable query filters, its value must not be empty, and the length is of Unicode code points. |  [optional] |
|**productType** | **String** | The product type of the item. May not be changed once an item has been created.  Only items of product type &#x60;REGULAR&#x60; or &#x60;APPOINTMENTS_SERVICE&#x60; may be created by this API; items with other product types are read-only. |  [optional] |
|**skipModifierScreen** | **Boolean** | If &#x60;false&#x60;, the Square Point of Sale app will present the &#x60;CatalogItem&#x60;&#39;s details screen immediately, allowing the merchant to choose &#x60;CatalogModifier&#x60;s before adding the item to the cart.  This is the default behavior.  If &#x60;true&#x60;, the Square Point of Sale app will immediately add the item to the cart with the pre-selected modifiers, and merchants can edit modifiers by drilling down onto the item&#39;s details.  Third-party clients are encouraged to implement similar behaviors. |  [optional] |
|**sortName** | **String** | A name to sort the item by. If this name is unspecified, namely, the &#x60;sort_name&#x60; field is absent, the regular &#x60;name&#x60; field is used for sorting.  It is currently supported for sellers of the Japanese locale only. |  [optional] |
|**taxIds** | **List&lt;String&gt;** | A set of IDs indicating the taxes enabled for this item. When updating an item, any taxes listed here will be added to the item. Taxes may also be added to or deleted from an item using &#x60;UpdateItemTaxes&#x60;. |  [optional] |
|**variations** | [**List&lt;CatalogObject&gt;**](CatalogObject.md) | A list of [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) objects for this item. An item must have at least one variation. |  [optional] |



