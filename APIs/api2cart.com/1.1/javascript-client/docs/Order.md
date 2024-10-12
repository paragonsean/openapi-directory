# SwaggerApi2Cart.Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalFields** | **Object** |  | [optional] 
**basketId** | **String** |  | [optional] 
**billingAddress** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**bundles** | [**[OrderItem]**](OrderItem.md) |  | [optional] 
**channelId** | **String** |  | [optional] 
**comment** | **String** |  | [optional] 
**createAt** | [**A2CDateTime**](A2CDateTime.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customFields** | **Object** |  | [optional] 
**customer** | [**BaseCustomer**](BaseCustomer.md) |  | [optional] 
**discounts** | [**[OrderTotalsNewDiscount]**](OrderTotalsNewDiscount.md) |  | [optional] 
**finishedTime** | [**A2CDateTime**](A2CDateTime.md) |  | [optional] 
**giftMessage** | **String** |  | [optional] 
**id** | **String** |  | [optional] 
**modifiedAt** | [**A2CDateTime**](A2CDateTime.md) |  | [optional] 
**orderDetailsUrl** | **String** |  | [optional] 
**orderId** | **String** |  | [optional] 
**orderProducts** | [**[OrderItem]**](OrderItem.md) |  | [optional] 
**paymentMethod** | [**OrderPaymentMethod**](OrderPaymentMethod.md) |  | [optional] 
**refunds** | [**[OrderRefund]**](OrderRefund.md) |  | [optional] 
**shippingAddress** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**shippingMethod** | [**OrderShippingMethod**](OrderShippingMethod.md) |  | [optional] 
**shippingMethods** | [**[OrderShippingMethod]**](OrderShippingMethod.md) |  | [optional] 
**status** | [**OrderStatus**](OrderStatus.md) |  | [optional] 
**storeId** | **String** |  | [optional] 
**total** | [**OrderTotal**](OrderTotal.md) |  | [optional] 
**totals** | [**OrderTotals**](OrderTotals.md) |  | [optional] 
**warehousesIds** | **[String]** |  | [optional] 


