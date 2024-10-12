

# OrderTrackingSignalLineItemDetails

The line items of the order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | Brand of the product. |  [optional] |
|**gtin** | **String** | The Global Trade Item Number. |  [optional] |
|**lineItemId** | **String** | Required. The ID for this line item. |  [optional] |
|**mpn** | **String** | The manufacturer part number. |  [optional] |
|**productDescription** | **String** | Plain text description of this product (deprecated: Please use product_title instead). |  [optional] |
|**productId** | **String** | Required. The Content API REST ID of the product, in the form channel:contentLanguage:targetCountry:offerId. |  [optional] |
|**productTitle** | **String** | Plain text title of this product. |  [optional] |
|**quantity** | **String** | The quantity of the line item in the order. |  [optional] |
|**sku** | **String** | Merchant SKU for this item (deprecated). |  [optional] |
|**upc** | **String** | Universal product code for this item (deprecated: Please use GTIN instead). |  [optional] |



