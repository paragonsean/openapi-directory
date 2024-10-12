

# OrderLineItemProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | Brand of the item. |  [optional] |
|**channel** | **String** | The item&#39;s channel (online or local). Acceptable values are: - \&quot;&#x60;local&#x60;\&quot; - \&quot;&#x60;online&#x60;\&quot;  |  [optional] |
|**condition** | **String** | Condition or state of the item. Acceptable values are: - \&quot;&#x60;new&#x60;\&quot; - \&quot;&#x60;refurbished&#x60;\&quot; - \&quot;&#x60;used&#x60;\&quot;  |  [optional] |
|**contentLanguage** | **String** | The two-letter ISO 639-1 language code for the item. |  [optional] |
|**fees** | [**List&lt;OrderLineItemProductFee&gt;**](OrderLineItemProductFee.md) | Associated fees at order creation time. |  [optional] |
|**gtin** | **String** | Global Trade Item Number (GTIN) of the item. |  [optional] |
|**id** | **String** | The REST ID of the product. |  [optional] |
|**imageLink** | **String** | URL of an image of the item. |  [optional] |
|**itemGroupId** | **String** | Shared identifier for all variants of the same product. |  [optional] |
|**mpn** | **String** | Manufacturer Part Number (MPN) of the item. |  [optional] |
|**offerId** | **String** | An identifier of the item. |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |
|**shownImage** | **String** | URL to the cached image shown to the user when order was placed. |  [optional] |
|**targetCountry** | **String** | The CLDR territory // code of the target country of the product. |  [optional] |
|**title** | **String** | The title of the product. |  [optional] |
|**variantAttributes** | [**List&lt;OrderLineItemProductVariantAttribute&gt;**](OrderLineItemProductVariantAttribute.md) | Variant attributes for the item. These are dimensions of the product, such as color, gender, material, pattern, and size. You can find a comprehensive list of variant attributes here. |  [optional] |



