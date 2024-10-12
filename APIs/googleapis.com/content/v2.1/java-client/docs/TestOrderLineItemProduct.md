

# TestOrderLineItemProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | Required. Brand of the item. |  [optional] |
|**condition** | **String** | Required. Condition or state of the item. Acceptable values are: - \&quot;&#x60;new&#x60;\&quot;  |  [optional] |
|**contentLanguage** | **String** | Required. The two-letter ISO 639-1 language code for the item. Acceptable values are: - \&quot;&#x60;en&#x60;\&quot; - \&quot;&#x60;fr&#x60;\&quot;  |  [optional] |
|**fees** | [**List&lt;OrderLineItemProductFee&gt;**](OrderLineItemProductFee.md) | Fees for the item. Optional. |  [optional] |
|**gtin** | **String** | Global Trade Item Number (GTIN) of the item. Optional. |  [optional] |
|**imageLink** | **String** | Required. URL of an image of the item. |  [optional] |
|**itemGroupId** | **String** | Shared identifier for all variants of the same product. Optional. |  [optional] |
|**mpn** | **String** | Manufacturer Part Number (MPN) of the item. Optional. |  [optional] |
|**offerId** | **String** | Required. An identifier of the item. |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |
|**targetCountry** | **String** | Required. The CLDR territory code of the target country of the product. |  [optional] |
|**title** | **String** | Required. The title of the product. |  [optional] |
|**variantAttributes** | [**List&lt;OrderLineItemProductVariantAttribute&gt;**](OrderLineItemProductVariantAttribute.md) | Variant attributes for the item. Optional. |  [optional] |



