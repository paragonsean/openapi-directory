

# OrderConfirmPost200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**ShippingAddress**](ShippingAddress.md) |  |  [optional] |
|**deliveryDate** | **String** | The target delivery date for the shipping method. Formatted as a datetime string. |  [optional] |
|**notes** | **String** |  |  [optional] |
|**orderId** | **String** | Unique identifier for referencing this order. |  [optional] |
|**orderItems** | [**List&lt;Print&gt;**](Print.md) |  |  [optional] |
|**purchased** | **Boolean** | true if the purchase was completed successfully. |  [optional] |
|**quote** | [**Quote**](Quote.md) |  |  [optional] |
|**shippingService** | **String** | Service identifier string pulled from a specific rate returned by /order/shipping. |  [optional] |



