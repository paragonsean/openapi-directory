# CheckoutApi.PlaceOrderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientProfileData** | [**PlaceOrderRequestClientProfileData**](PlaceOrderRequestClientProfileData.md) |  | 
**items** | [**[PlaceOrderRequestItemsInner]**](PlaceOrderRequestItemsInner.md) | Array of objects containing information on each of the order&#39;s items. | 
**marketingData** | [**PlaceOrderRequestMarketingData**](PlaceOrderRequestMarketingData.md) |  | [optional] 
**openTextField** | **String** | Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as &#x60;JSON&#x60; even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1) | [optional] [default to &#39;open-text-example&#39;]
**paymentData** | [**PlaceOrderRequestPaymentData**](PlaceOrderRequestPaymentData.md) |  | 
**salesAssociateData** | [**AddMerchantContextDataRequestSalesAssociateData**](AddMerchantContextDataRequestSalesAssociateData.md) |  | [optional] 
**shippingData** | [**PlaceOrderRequestShippingData**](PlaceOrderRequestShippingData.md) |  | 


