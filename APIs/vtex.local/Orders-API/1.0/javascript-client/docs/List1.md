# OrdersApi.List1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shippingEstimatedDate** | **String** | Estimate shipping date. | 
**shippingEstimatedDateMax** | **String** | The most extended shipping estimation possible. | 
**shippingEstimatedDateMin** | **String** | The least extended shipping estimation possible. | 
**affiliateId** | **String** | Corresponds to the three-digits [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) identification code of the seller responsible for the order. | 
**authorizedDate** | **String** | Authorized order date. | 
**callCenterOperatorName** | **String** | Call center operator responsible for the order. | 
**clientName** | **String** | Order&#39;s customer name. | 
**creationDate** | **String** | Order&#39;s creation date. | 
**currencyCode** | **String** | Currency code in ISO 4217. For example, &#x60;BRL&#x60;. | 
**items** | [**[Item2]**](Item2.md) | Information about order&#39;s items | 
**lastMessageUnread** | **String** | Last sent transactional message. | 
**listId** | **String** | Related Gift List ID. | 
**listType** | **String** | Related Gift list type. | 
**marketPlaceOrderId** | **String** | Marketplace order ID. | 
**orderId** | **String** | Order ID is a unique code that identifies an order. | 
**orderIsComplete** | **Boolean** | If it is a completed order (&#x60;true&#x60;) or not (&#x60;false&#x60;). For more information, see [Order flow and status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196). | 
**origin** | **String** | Order Origin, if &#x60;Marketplace&#x60; or &#x60;Fulfillment&#x60;. | 
**paymentNames** | **String** | Payment system name. | 
**salesChannel** | **String** | Sales channel (or [trade policy](https://help.vtex.com/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) ID related to the order. | 
**sequence** | **String** | Six-digit string that follows the order ID. For example, in order &#x60;1268540501456-01 (501456)&#x60;, the sequence is &#x60;501456&#x60;. | 
**status** | **String** | Order [status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196). | 
**statusDescription** | **String** | Status description which is displayed on the Admin panel. This field is deprecated and may not return any value. | 
**totalItems** | **Number** | Order&#39;s total amount of items. | 
**totalValue** | **Number** | Total value amount. | 
**workflowInErrorState** | **Boolean** | If there is a work flow error (&#x60;true&#x60;) or not (&#x60;false&#x60;). | 
**workflowInRetry** | **Boolean** | If the order is in a work flow retry (&#x60;true&#x60;) or not (&#x60;false&#x60;). | 


