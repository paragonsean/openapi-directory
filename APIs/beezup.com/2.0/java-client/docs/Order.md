

# Order


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Integer** | The marketplace account identifier in BeezUP. This account identifier is based on your api settings. |  |
|**beezUPOrderId** | **UUID** | The BeezUP Order identifier |  |
|**beezUPOrderUrl** | **String** | The URL &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/URL\&quot;&gt;https://en.wikipedia.org/wiki/URL&lt;/a&gt; |  [optional] |
|**etag** | **String** | ETag value to identify the order.\\ This information is required for the operation GetOrder and ChangeOrder.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  |  |
|**links** | [**OrderLinks**](OrderLinks.md) |  |  |
|**marketplaceBusinessCode** | **String** | In an marketplace technical code like CDiscount you can have several marketplaces like GO SPORT, etc. We identify them by a business code. |  |
|**marketplaceTechnicalCode** | **String** | The technical code of the marketplace. |  |
|**orderBuyerName** | **String** | Buyer full name |  [optional] |
|**orderCurrencyCode** | **String** | The currency code &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_4217\&quot;&gt;(ISO 4217)&lt;/a&gt;  |  [optional] |
|**orderInvoiceNumber** | **String** | The order invoice number |  [optional] |
|**orderInvoiceUri** | **String** | The order invoice URI |  [optional] |
|**orderLastModificationUtcDate** | **OffsetDateTime** | The last modification UTC date done by BeezUP of this order |  |
|**orderMarketplaceLastModificationUtcDate** | **OffsetDateTime** | The last modification UTC date done by the marketplace on this order |  |
|**orderMarketplaceOrderId** | **String** | The order marketplace identifier |  |
|**orderMerchantECommerceSoftwareName** | **String** | The e-commerce software name of the merchant |  [optional] |
|**orderMerchantECommerceSoftwareVersion** | **String** | The e-commece software version of the merchant |  [optional] |
|**orderMerchantOrderId** | **String** | The order merchant identifier |  [optional] |
|**orderPurchaseUtcDate** | **OffsetDateTime** | The purchase date of this order |  |
|**orderStatusBeezUPOrderStatus** | **String** | BeezUP order status. Unified for all marketplaces. |  |
|**orderStatusMarketplaceOrderStatus** | **String** | The marketplace order state |  [optional] |
|**orderTotalPrice** | **BigDecimal** | The total price of this order (corresponding to the amount paid by the customer) |  [optional] |
|**processing** | **Boolean** | If true, there is currently a harvest or an order change in progress. Otherwise false. |  |
|**orderItems** | [**List&lt;OrderItem&gt;**](OrderItem.md) |  |  |
|**orderBuyerAddressCity** | **String** | The Buyer address city of this order |  [optional] |
|**orderBuyerAddressCountryIsoCodeAlpha2** | **String** | The Buyer address country iso code alpha 2 (see http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#/decoding_table for more details) |  [optional] |
|**orderBuyerAddressCountryName** | **String** | The Buyer address country name |  [optional] |
|**orderBuyerAddressLine1** | **String** | The Buyer address line 1 of this order |  [optional] |
|**orderBuyerAddressLine2** | **String** | The Buyer address line 2 of this order |  [optional] |
|**orderBuyerAddressLine3** | **String** | The Buyer address line 3 of this order |  [optional] |
|**orderBuyerAddressPostalCode** | **String** | The Buyer address postal code of this order |  [optional] |
|**orderBuyerAddressStateOrRegion** | **String** | The Buyer address state or region of this order |  [optional] |
|**orderBuyerCivility** | **String** | The buyer civility for this order |  [optional] |
|**orderBuyerCompanyName** | **String** | The buyer company name for this order |  [optional] |
|**orderBuyerEmail** | **String** | The email of the buyer for this order |  [optional] |
|**orderBuyerFirstName** | **String** | Order Buyer first name |  [optional] |
|**orderBuyerIdentifier** | **String** | The buyer identifier for this order |  [optional] |
|**orderBuyerLastName** | **String** | Order Buyer last name |  [optional] |
|**orderBuyerMobilePhone** | **String** | The mobile phone number of the buyer for this order |  [optional] |
|**orderBuyerPhone** | **String** | The phone number of the buyer for this order |  [optional] |
|**orderComment** | **String** | The comment associated to this order |  [optional] |
|**orderFulfilledBy** | **String** | The order FulfilledBy |  [optional] |
|**orderIsBusiness** | **Boolean** | The order IsBusiness |  [optional] |
|**orderIsPrime** | **Boolean** | Indicates if the order is considered as Prime (only on Amazon) |  [optional] |
|**orderMarketPlaceChannel** | **String** | Useful to identify the origin of the order. For example in Amazon. |  [optional] |
|**orderOrderItemsSourceUri** | **URI** | Technical information: The url to the source of this order items. We received this information from the marketplace.  |  [optional] |
|**orderOrderSourceUri** | **URI** | Technical information: The url to the source of this order. We received this information from the marketplace.  |  [optional] |
|**orderPayingUtcDate** | **OffsetDateTime** | The UTC date of the payment of this order |  [optional] |
|**orderPaymentMethod** | **String** | The payment method of this order |  [optional] |
|**orderShippingAddressCity** | **String** | The shipping address city of this order |  [optional] |
|**orderShippingAddressCountryIsoCodeAlpha2** | **String** | The shipping address country iso code alpha 2 (see http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#/decoding_table for more details) |  [optional] |
|**orderShippingAddressCountryName** | **String** | The shipping address country name |  [optional] |
|**orderShippingAddressLine1** | **String** | The shipping address line 1 of this order |  [optional] |
|**orderShippingAddressLine2** | **String** | The shipping address line 2 of this order |  [optional] |
|**orderShippingAddressLine3** | **String** | The shipping address line 3 of this order |  [optional] |
|**orderShippingAddressName** | **String** | The name of the person in the shipping address for this order |  [optional] |
|**orderShippingAddressPostalCode** | **String** | The shipping address postal code of this order |  [optional] |
|**orderShippingAddressStateOrRegion** | **String** | The shipping address state or region of this order |  [optional] |
|**orderShippingCivility** | **String** | The civility of the person in the shipping address for this order |  [optional] |
|**orderShippingCompanyName** | **String** | The company name of the shipping address for this order |  [optional] |
|**orderShippingEarliestShipUtcDate** | **OffsetDateTime** | The UTC date of the earliest ship for this order |  [optional] |
|**orderShippingEmail** | **String** | The email of the person in the shipping address for this order |  [optional] |
|**orderShippingFirstName** | **String** | Order Shipping first name |  [optional] |
|**orderShippingLastName** | **String** | Order Shipping last name |  [optional] |
|**orderShippingLatestShipUtcDate** | **OffsetDateTime** | The UTC date of the latest ship for this order |  [optional] |
|**orderShippingMethod** | **String** | The shipping method of this order |  [optional] |
|**orderShippingMobilePhone** | **String** | The mobile phone number of the person in the shipping address for this order |  [optional] |
|**orderShippingPhone** | **String** | The phone number of the person in the shipping address for this order |  [optional] |
|**orderShippingPrice** | **BigDecimal** | The shipping price of this order |  [optional] |
|**orderShippingShippingTax** | **BigDecimal** | The shipping tax for this order |  [optional] |
|**orderTotalCommission** | **BigDecimal** | The total commission of this order |  [optional] |
|**orderTotalTax** | **BigDecimal** | The total tax of this order |  [optional] |
|**transitionLinks** | [**List&lt;LinksChangeOrderLink&gt;**](LinksChangeOrderLink.md) | Contains the authorized change actions for an order |  |



