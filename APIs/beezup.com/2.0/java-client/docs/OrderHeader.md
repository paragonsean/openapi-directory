

# OrderHeader

Describe the basic information related to an order. All properties with the prefix order_ are translated in the list of values /user/lov/OrderMetaInfoOrderDetails

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Integer** | The marketplace account identifier in BeezUP. This account identifier is based on your api settings. |  |
|**beezUPOrderId** | **UUID** | The BeezUP Order identifier |  |
|**beezUPOrderUrl** | **String** | The URL &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/URL\&quot;&gt;https://en.wikipedia.org/wiki/URL&lt;/a&gt; |  [optional] |
|**etag** | **String** | ETag value to identify the order.\\ This information is required for the operation GetOrder and ChangeOrder.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  |  |
|**links** | [**OrderHeaderLinks**](OrderHeaderLinks.md) |  |  |
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



