

# PosInventoryResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentLanguage** | **String** | Required. The two-letter ISO 639-1 language code for the item. |  [optional] |
|**gtin** | **String** | Global Trade Item Number. |  [optional] |
|**itemId** | **String** | Required. A unique identifier for the item. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#posInventoryResponse&#x60;\&quot;. |  [optional] |
|**pickupMethod** | **String** | Optional. Supported pickup method for this offer. Unless the value is \&quot;not supported\&quot;, this field must be submitted together with &#x60;pickupSla&#x60;. For accepted attribute values, see the [local product inventory feed specification](https://support.google.com/merchants/answer/3061342). |  [optional] |
|**pickupSla** | **String** | Optional. Expected date that an order will be ready for pickup relative to the order date. Must be submitted together with &#x60;pickupMethod&#x60;. For accepted attribute values, see the [local product inventory feed specification](https://support.google.com/merchants/answer/3061342). |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |
|**quantity** | **String** | Required. The available quantity of the item. |  [optional] |
|**storeCode** | **String** | Required. The identifier of the merchant&#39;s store. Either a &#x60;storeCode&#x60; inserted through the API or the code of the store in a Business Profile. |  [optional] |
|**targetCountry** | **String** | Required. The CLDR territory code for the item. |  [optional] |
|**timestamp** | **String** | Required. The inventory timestamp, in ISO 8601 format. |  [optional] |



