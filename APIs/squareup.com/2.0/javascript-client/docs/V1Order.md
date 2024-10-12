# SquareConnectApi.V1Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btcPriceSatoshi** | **Number** | For Bitcoin transactions, the price of the buyer&#39;s order in satoshi (100 million satoshi equals 1 BTC). | [optional] 
**btcReceiveAddress** | **String** | For Bitcoin transactions, the address that the buyer sent Bitcoin to. | [optional] 
**buyerEmail** | **String** | The email address of the order&#39;s buyer. | [optional] 
**buyerNote** | **String** | A note provided by the buyer when the order was created, if any. | [optional] 
**canceledNote** | **String** | A note provided by the merchant when the order&#39;s state was set to CANCELED, if any. | [optional] 
**completedNote** | **String** | A note provided by the merchant when the order&#39;s state was set to COMPLETED, if any | [optional] 
**createdAt** | **String** | The time when the order was created, in ISO 8601 format. | [optional] 
**errors** | [**[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**expiresAt** | **String** | The time when the order expires if no action is taken, in ISO 8601 format. | [optional] 
**id** | **String** | The order&#39;s unique identifier. | [optional] 
**orderHistory** | [**[V1OrderHistoryEntry]**](V1OrderHistoryEntry.md) | The history of actions associated with the order. | [optional] 
**paymentId** | **String** | The unique identifier of the payment associated with the order. | [optional] 
**promoCode** | **String** | The promo code provided by the buyer, if any. | [optional] 
**recipientName** | **String** | The name of the order&#39;s buyer. | [optional] 
**recipientPhoneNumber** | **String** | The phone number to use for the order&#39;s delivery. | [optional] 
**refundedNote** | **String** | A note provided by the merchant when the order&#39;s state was set to REFUNDED, if any. | [optional] 
**shippingAddress** | [**Address**](Address.md) |  | [optional] 
**state** | **String** | Whether the tax is an ADDITIVE tax or an INCLUSIVE tax. | [optional] 
**subtotalMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**tender** | [**V1Tender**](V1Tender.md) |  | [optional] 
**totalDiscountMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**totalPriceMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**totalShippingMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**totalTaxMoney** | [**V1Money**](V1Money.md) |  | [optional] 
**updatedAt** | **String** | The time when the order was last modified, in ISO 8601 format. | [optional] 


