

# ProductDeliveryTime

The estimated days to deliver a product after an order is placed. Only authorized shipping signals partners working with a merchant can use this resource. Merchants should use the [`products`](https://developers.google.com/shopping-content/reference/rest/v2.1/products#productshipping) resource instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**areaDeliveryTimes** | [**List&lt;ProductDeliveryTimeAreaDeliveryTime&gt;**](ProductDeliveryTimeAreaDeliveryTime.md) | Required. A set of associations between &#x60;DeliveryArea&#x60; and &#x60;DeliveryTime&#x60; entries. The total number of &#x60;areaDeliveryTimes&#x60; can be at most 100. |  [optional] |
|**productId** | [**ProductId**](ProductId.md) |  |  [optional] |



