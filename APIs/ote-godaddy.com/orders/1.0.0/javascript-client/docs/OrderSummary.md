# OpenapiJsClient.OrderSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | Date and time when the current order was created | 
**currency** | **String** | Currency in which the order was placed | 
**items** | [**[LineItemSummary]**](LineItemSummary.md) | Sets of two or more line items in current order | 
**orderId** | **String** | Unique identifier of the current order | 
**parentOrderId** | **String** | Unique identifier of the parent order. All refund/chargeback orders are tied to the original order. The orginal order&#39;s &#x60;orderId&#x60; is the &#x60;parentOrderId&#x60; of refund/chargeback orders | [optional] 
**pricing** | [**OrderSummaryPricing**](OrderSummaryPricing.md) |  | 


