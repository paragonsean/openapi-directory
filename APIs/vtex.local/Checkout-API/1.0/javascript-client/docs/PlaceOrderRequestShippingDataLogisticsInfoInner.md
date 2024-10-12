# CheckoutApi.PlaceOrderRequestShippingDataLogisticsInfoInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliveryWindow** | [**PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow**](PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow.md) |  | [optional] 
**itemIndex** | **Number** | Index of the item in the &#x60;items&#x60; array, starting from 0. | [default to 0]
**lockTTL** | **String** | Logistics reservation waiting time. | [optional] [default to &#39;8d&#39;]
**price** | **Number** | Shipping price for the item. Does not account for the whole order&#39;s shipping price. | [default to 1099]
**selectedSla** | **String** | Selected shipping option | [default to &#39;Express&#39;]
**shippingEstimate** | **String** | Estimated time until delivery for the item. | [optional] [default to &#39;7d&#39;]


