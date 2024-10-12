# SquareConnectApi.V1PaymentItemization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discountMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**discounts** | [**[V1PaymentDiscount]**](V1PaymentDiscount.md) | All discounts applied to this itemization. | [optional] 
**grossSalesMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**itemDetail** | [**V1PaymentItemDetail**](V1PaymentItemDetail.md) |  | [optional] 
**itemVariationName** | **String** | The name of the item variation purchased, if any. | [optional] 
**itemizationType** | **String** | The type of purchase that the itemization represents, such as an ITEM or CUSTOM_AMOUNT | [optional] 
**modifiers** | [**[V1PaymentModifier]**](V1PaymentModifier.md) | All modifier options applied to this itemization. | [optional] 
**name** | **String** | The item&#39;s name. | [optional] 
**netSalesMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**notes** | **String** | Notes entered by the merchant about the item at the time of payment, if any. | [optional] 
**quantity** | **Number** | The quantity of the item purchased. This can be a decimal value. | [optional] 
**singleQuantityMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**taxes** | [**[V1PaymentTax]**](V1PaymentTax.md) | All taxes applied to this itemization. | [optional] 
**totalMoney** | [**V1Money**](V1Money.md) |  | [optional] 


