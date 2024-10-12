# OrdersApi.OrdersApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLog**](OrdersApi.md#addLog) | **POST** /api/oms/pvt/orders/{orderId}/interactions | Add log in orders
[**cancelOrder**](OrdersApi.md#cancelOrder) | **POST** /api/oms/pvt/orders/{orderId}/cancel | Cancel order
[**getOrder**](OrdersApi.md#getOrder) | **GET** /api/oms/pvt/orders/{orderId} | Get order
[**listOrders**](OrdersApi.md#listOrders) | **GET** /api/oms/pvt/orders | List orders
[**registerChange**](OrdersApi.md#registerChange) | **POST** /api/oms/pvt/orders/{orderId}/changes | Register change on order
[**startHandling**](OrdersApi.md#startHandling) | **POST** /api/oms/pvt/orders/{orderId}/start-handling | Start handling order



## addLog

> addLog(contentType, accept, orderId, addLogRequest)

Add log in orders

Add a Log in Interactions Order Array.

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrdersApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let orderId = "1172452900788-01"; // String | Order ID is a unique code that identifies an order.
let addLogRequest = {"message":"Teste add interactions","source":"Postman"}; // AddLogRequest | 
apiInstance.addLog(contentType, accept, orderId, addLogRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **orderId** | **String**| Order ID is a unique code that identifies an order. | 
 **addLogRequest** | [**AddLogRequest**](AddLogRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## cancelOrder

> CancelOrder200Response cancelOrder(accept, contentType, orderId, opts)

Cancel order

You should use this endpoint to cancel an order by its order identification number (the &#x60;orderId&#x60;).  A common scenario is one where the seller has a problem with the order fulfillment and needs to request the order cancellation to the marketplace. To do this, the seller would need to make this request, passing the &#x60;orderId&#x60; in the URL.  You should expect a response with the date when the notification was received, the orderId, and a receipt protocol code.  Be aware that if the order status is already &#x60;Invoiced&#x60;, the order can only be canceled if—before using this request—you send a return invoice through the [Order Invoice Notification endpoint](https://developers.vtex.com/reference/invoice#invoicenotification).    &gt; The &#x60;Cancel order&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrdersApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let orderId = "1172452900788-01"; // String | ID that identifies the order in the seller.
let opts = {
  'cancelOrderRequest': new OrdersApi.CancelOrderRequest() // CancelOrderRequest | 
};
apiInstance.cancelOrder(accept, contentType, orderId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **orderId** | **String**| ID that identifies the order in the seller. | 
 **cancelOrderRequest** | [**CancelOrderRequest**](CancelOrderRequest.md)|  | [optional] 

### Return type

[**CancelOrder200Response**](CancelOrder200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrder

> GetOrder200Response getOrder(accept, contentType, orderId)

Get order

This endpoint retrieves order details by searching a specific order ID or sequence number.    &gt; The &#x60;View order&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc).    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer&#39;s journey.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;orderId\&quot;: \&quot;1244730712239-01\&quot;,      \&quot;sequence\&quot;: \&quot;502790\&quot;,      \&quot;marketplaceOrderId\&quot;: \&quot;\&quot;,      \&quot;marketplaceServicesEndpoint\&quot;: null,      \&quot;sellerOrderId\&quot;: \&quot;SLR-1244730712239-01\&quot;,      \&quot;origin\&quot;: \&quot;Marketplace\&quot;,      \&quot;affiliateId\&quot;: \&quot;\&quot;,      \&quot;salesChannel\&quot;: \&quot;1\&quot;,      \&quot;merchantName\&quot;: null,      \&quot;status\&quot;: \&quot;payment-approved\&quot;,      \&quot;statusDescription\&quot;: \&quot;Pagamento Aprovado\&quot;,      \&quot;value\&quot;: 2012,      \&quot;creationDate\&quot;: \&quot;2022-07-06T09:11:51.4597231+00:00\&quot;,      \&quot;lastChange\&quot;: \&quot;2022-07-06T09:12:00.2849749+00:00\&quot;,      \&quot;orderGroup\&quot;: \&quot;1244730712239\&quot;,      \&quot;totals\&quot;: [          {              \&quot;id\&quot;: \&quot;Items\&quot;,              \&quot;name\&quot;: \&quot;Total dos Itens\&quot;,              \&quot;value\&quot;: 2265          },          {              \&quot;id\&quot;: \&quot;Discounts\&quot;,              \&quot;name\&quot;: \&quot;Total dos Descontos\&quot;,              \&quot;value\&quot;: -453          },          {              \&quot;id\&quot;: \&quot;Shipping\&quot;,              \&quot;name\&quot;: \&quot;Total do Frete\&quot;,              \&quot;value\&quot;: 200          },          {              \&quot;id\&quot;: \&quot;Tax\&quot;,              \&quot;name\&quot;: \&quot;Total da Taxa\&quot;,              \&quot;value\&quot;: 0          }      ],      \&quot;items\&quot;: [          {              \&quot;uniqueId\&quot;: \&quot;A14AD652AC5D40FBB0137D3ADA3CB800\&quot;,              \&quot;id\&quot;: \&quot;12\&quot;,              \&quot;productId\&quot;: \&quot;8\&quot;,              \&quot;ean\&quot;: null,              \&quot;lockId\&quot;: null,              \&quot;itemAttachment\&quot;: {                  \&quot;content\&quot;: {},                  \&quot;name\&quot;: null              },              \&quot;attachments\&quot;: [],              \&quot;quantity\&quot;: 1,              \&quot;seller\&quot;: \&quot;ppxpssp\&quot;,              \&quot;name\&quot;: \&quot;Camiseta P Azul\&quot;,              \&quot;refId\&quot;: \&quot;COP01_P-A\&quot;,              \&quot;price\&quot;: 2265,              \&quot;listPrice\&quot;: 2265,              \&quot;manualPrice\&quot;: null,              \&quot;priceTags\&quot;: [                  {                      \&quot;name\&quot;: \&quot;discount@price-d0231eb3-e9a4-47b2-9c74-bc346df11ce4#e9bb430d-30b3-4461-a86e-f66f35b2915d\&quot;,                      \&quot;value\&quot;: -453,                      \&quot;isPercentual\&quot;: false,                      \&quot;identifier\&quot;: \&quot;d0231eb3-e9a4-47b2-9c74-bc346df11ce4\&quot;,                      \&quot;rawValue\&quot;: -4.53,                      \&quot;rate\&quot;: null,                      \&quot;jurisCode\&quot;: null,                      \&quot;jurisType\&quot;: null,                      \&quot;jurisName\&quot;: null                  }              ],              \&quot;imageUrl\&quot;: \&quot;https://ppxps.vteximg.com.br/arquivos/ids/155407-55-55/EE803C74-37A5-4804-B1A6-9F12D22EA505.png?v&#x3D;637559269453730000\&quot;,              \&quot;detailUrl\&quot;: \&quot;/camiseta/p\&quot;,              \&quot;components\&quot;: [],              \&quot;bundleItems\&quot;: [],              \&quot;params\&quot;: [],              \&quot;offerings\&quot;: [],              \&quot;sellerSku\&quot;: \&quot;12\&quot;,              \&quot;priceValidUntil\&quot;: \&quot;2023-07-06T09:11:04.0000000+00:00\&quot;,              \&quot;commission\&quot;: 0,              \&quot;tax\&quot;: 0,              \&quot;preSaleDate\&quot;: null,              \&quot;additionalInfo\&quot;: {                  \&quot;brandName\&quot;: \&quot;Marca TOP\&quot;,                  \&quot;brandId\&quot;: \&quot;2000001\&quot;,                  \&quot;categoriesIds\&quot;: \&quot;/7/\&quot;,                  \&quot;categories\&quot;: [                      {                          \&quot;id\&quot;: 7,                          \&quot;name\&quot;: \&quot;Roupas\&quot;                      }                  ],                  \&quot;productClusterId\&quot;: \&quot;\&quot;,                  \&quot;commercialConditionId\&quot;: \&quot;1\&quot;,                  \&quot;dimension\&quot;: {                      \&quot;cubicweight\&quot;: 1.0000,                      \&quot;height\&quot;: 6.0000,                      \&quot;length\&quot;: 10.0000,                      \&quot;weight\&quot;: 4.0000,                      \&quot;width\&quot;: 8.0000                  },                  \&quot;offeringInfo\&quot;: null,                  \&quot;offeringType\&quot;: null,                  \&quot;offeringTypeId\&quot;: null              },              \&quot;measurementUnit\&quot;: \&quot;un\&quot;,              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;sellingPrice\&quot;: 1812,              \&quot;isGift\&quot;: false,              \&quot;shippingPrice\&quot;: null,              \&quot;rewardValue\&quot;: 0,              \&quot;freightCommission\&quot;: 0,              \&quot;priceDefinition\&quot;: {                  \&quot;sellingPrices\&quot;: [                      {                          \&quot;value\&quot;: 1812,                          \&quot;quantity\&quot;: 1                      }                  ],                  \&quot;calculatedSellingPrice\&quot;: 1812,                  \&quot;total\&quot;: 1812              },              \&quot;taxCode\&quot;: \&quot;1122\&quot;,              \&quot;parentItemIndex\&quot;: null,              \&quot;parentAssemblyBinding\&quot;: null,              \&quot;callCenterOperator\&quot;: null,              \&quot;serialNumbers\&quot;: null,              \&quot;assemblies\&quot;: [],              \&quot;costPrice\&quot;: null          }      ],      \&quot;marketplaceItems\&quot;: [],      \&quot;clientProfileData\&quot;: {          \&quot;id\&quot;: \&quot;clientProfileData\&quot;,          \&quot;email\&quot;: \&quot;0bf94cbf23ff410aaaf7c707dd8a808c@ct.vtex.com.br\&quot;,          \&quot;firstName\&quot;: \&quot;Paulo\&quot;,          \&quot;lastName\&quot;: \&quot;Filho\&quot;,          \&quot;documentType\&quot;: \&quot;cpf\&quot;,          \&quot;document\&quot;: \&quot;11156703794\&quot;,          \&quot;phone\&quot;: \&quot;+5521971126360\&quot;,          \&quot;corporateName\&quot;: null,          \&quot;tradeName\&quot;: null,          \&quot;corporateDocument\&quot;: null,          \&quot;stateInscription\&quot;: null,          \&quot;corporatePhone\&quot;: null,          \&quot;isCorporate\&quot;: false,          \&quot;userProfileId\&quot;: \&quot;ca0695a8-df34-4076-8663-725041930c75\&quot;,          \&quot;customerClass\&quot;: null      },      \&quot;giftRegistryData\&quot;: null,      \&quot;marketingData\&quot;: {          \&quot;id\&quot;: \&quot;marketingData\&quot;,          \&quot;utmSource\&quot;: null,          \&quot;utmPartner\&quot;: null,          \&quot;utmMedium\&quot;: null,          \&quot;utmCampaign\&quot;: null,          \&quot;coupon\&quot;: null,          \&quot;utmiCampaign\&quot;: null,          \&quot;utmipage\&quot;: null,          \&quot;utmiPart\&quot;: null,          \&quot;marketingTags\&quot;: [              \&quot;vtex-subscription\&quot;          ]      },      \&quot;ratesAndBenefitsData\&quot;: {          \&quot;id\&quot;: \&quot;ratesAndBenefitsData\&quot;,          \&quot;rateAndBenefitsIdentifiers\&quot;: [              {                  \&quot;description\&quot;: \&quot;Desconto de 20% no pedido para assinatura\&quot;,                  \&quot;featured\&quot;: true,                  \&quot;id\&quot;: \&quot;d0231eb3-e9a4-47b2-9c74-bc346df11ce4\&quot;,                  \&quot;name\&quot;: \&quot;Desconto 20% assinante\&quot;,                  \&quot;matchedParameters\&quot;: {},                  \&quot;additionalInfo\&quot;: null              }          ]      },      \&quot;shippingData\&quot;: {          \&quot;id\&quot;: \&quot;shippingData\&quot;,          \&quot;address\&quot;: {              \&quot;addressType\&quot;: \&quot;residential\&quot;,              \&quot;receiverName\&quot;: \&quot;Paulo Filho\&quot;,              \&quot;addressId\&quot;: \&quot;1651158093975\&quot;,              \&quot;postalCode\&quot;: \&quot;21341-270\&quot;,              \&quot;city\&quot;: \&quot;Rio de Janeiro\&quot;,              \&quot;state\&quot;: \&quot;RJ\&quot;,              \&quot;country\&quot;: \&quot;BRA\&quot;,              \&quot;street\&quot;: \&quot;Rua Pinto Teles\&quot;,              \&quot;number\&quot;: \&quot;1\&quot;,              \&quot;neighborhood\&quot;: \&quot;Praça Seca\&quot;,              \&quot;complement\&quot;: null,              \&quot;reference\&quot;: null,              \&quot;geoCoordinates\&quot;: [                  -43.350608825683594,                  -22.886520385742188              ]          },          \&quot;logisticsInfo\&quot;: [              {                  \&quot;itemIndex\&quot;: 0,                  \&quot;selectedSla\&quot;: \&quot;Normal\&quot;,                  \&quot;lockTTL\&quot;: \&quot;12d\&quot;,                  \&quot;price\&quot;: 200,                  \&quot;listPrice\&quot;: 200,                  \&quot;sellingPrice\&quot;: 200,                  \&quot;deliveryWindow\&quot;: null,                  \&quot;deliveryCompany\&quot;: \&quot;Transportadora\&quot;,                  \&quot;shippingEstimate\&quot;: \&quot;2bd\&quot;,                  \&quot;shippingEstimateDate\&quot;: \&quot;2022-07-08T09:11:57.8421126+00:00\&quot;,                  \&quot;slas\&quot;: [                      {                          \&quot;id\&quot;: \&quot;Normal\&quot;,                          \&quot;name\&quot;: \&quot;Normal\&quot;,                          \&quot;shippingEstimate\&quot;: \&quot;2bd\&quot;,                          \&quot;deliveryWindow\&quot;: null,                          \&quot;price\&quot;: 200,                          \&quot;deliveryChannel\&quot;: \&quot;delivery\&quot;,                          \&quot;pickupStoreInfo\&quot;: {                              \&quot;additionalInfo\&quot;: null,                              \&quot;address\&quot;: null,                              \&quot;dockId\&quot;: null,                              \&quot;friendlyName\&quot;: null,                              \&quot;isPickupStore\&quot;: false                          },                          \&quot;polygonName\&quot;: \&quot;\&quot;,                          \&quot;lockTTL\&quot;: \&quot;12d\&quot;,                          \&quot;pickupPointId\&quot;: null,                          \&quot;transitTime\&quot;: \&quot;2bd\&quot;                      }                  ],                  \&quot;shipsTo\&quot;: [                      \&quot;BRA\&quot;                  ],                  \&quot;deliveryIds\&quot;: [                      {                          \&quot;courierId\&quot;: \&quot;1\&quot;,                          \&quot;courierName\&quot;: \&quot;Transportadora\&quot;,                          \&quot;dockId\&quot;: \&quot;169fe66\&quot;,                          \&quot;quantity\&quot;: 1,                          \&quot;warehouseId\&quot;: \&quot;166cb0c\&quot;,                          \&quot;accountCarrierName\&quot;: null                      }                  ],                  \&quot;deliveryChannel\&quot;: \&quot;delivery\&quot;,                  \&quot;pickupStoreInfo\&quot;: {                      \&quot;additionalInfo\&quot;: null,                      \&quot;address\&quot;: null,                      \&quot;dockId\&quot;: null,                      \&quot;friendlyName\&quot;: null,                      \&quot;isPickupStore\&quot;: false                  },                  \&quot;addressId\&quot;: \&quot;1651158093975\&quot;,                  \&quot;polygonName\&quot;: \&quot;\&quot;,                  \&quot;pickupPointId\&quot;: null,                  \&quot;transitTime\&quot;: \&quot;2bd\&quot;              }          ],          \&quot;trackingHints\&quot;: null,          \&quot;selectedAddresses\&quot;: [              {                  \&quot;addressId\&quot;: \&quot;1651158093975\&quot;,                  \&quot;addressType\&quot;: \&quot;residential\&quot;,                  \&quot;receiverName\&quot;: \&quot;Paulo Filho\&quot;,                  \&quot;street\&quot;: \&quot;Rua Pinto Teles\&quot;,                  \&quot;number\&quot;: \&quot;1\&quot;,                  \&quot;complement\&quot;: null,                  \&quot;neighborhood\&quot;: \&quot;Praça Seca\&quot;,                  \&quot;postalCode\&quot;: \&quot;21341-270\&quot;,                  \&quot;city\&quot;: \&quot;Rio de Janeiro\&quot;,                  \&quot;state\&quot;: \&quot;RJ\&quot;,                  \&quot;country\&quot;: \&quot;BRA\&quot;,                  \&quot;reference\&quot;: null,                  \&quot;geoCoordinates\&quot;: [                      -43.350608825683594,                      -22.886520385742188                  ]              }          ]      },      \&quot;paymentData\&quot;: {          \&quot;giftCards\&quot;: [],          \&quot;transactions\&quot;: [              {                  \&quot;isActive\&quot;: true,                  \&quot;transactionId\&quot;: \&quot;A5BF0F884F314F788F4778B464EE1648\&quot;,                  \&quot;merchantName\&quot;: \&quot;PPXPS\&quot;,                  \&quot;payments\&quot;: [                      {                          \&quot;id\&quot;: \&quot;06D8D76D4BD549EF9CC209D969ACBA84\&quot;,                          \&quot;paymentSystem\&quot;: \&quot;47\&quot;,                          \&quot;paymentSystemName\&quot;: \&quot;Cash\&quot;,                          \&quot;value\&quot;: 2012,                          \&quot;installments\&quot;: 1,                          \&quot;referenceValue\&quot;: 2012,                          \&quot;cardHolder\&quot;: null,                          \&quot;cardNumber\&quot;: null,                          \&quot;firstDigits\&quot;: null,                          \&quot;lastDigits\&quot;: null,                          \&quot;cvv2\&quot;: null,                          \&quot;expireMonth\&quot;: null,                          \&quot;expireYear\&quot;: null,                          \&quot;url\&quot;: null,                          \&quot;giftCardId\&quot;: null,                          \&quot;giftCardName\&quot;: null,                          \&quot;giftCardCaption\&quot;: null,                          \&quot;redemptionCode\&quot;: null,                          \&quot;group\&quot;: \&quot;cash\&quot;,                          \&quot;tid\&quot;: null,                          \&quot;dueDate\&quot;: null,                          \&quot;connectorResponses\&quot;: {},                          \&quot;giftCardProvider\&quot;: null,                          \&quot;giftCardAsDiscount\&quot;: null,                          \&quot;koinUrl\&quot;: null,                          \&quot;accountId\&quot;: null,                          \&quot;parentAccountId\&quot;: null,                          \&quot;bankIssuedInvoiceIdentificationNumber\&quot;: null,                          \&quot;bankIssuedInvoiceIdentificationNumberFormatted\&quot;: null,                          \&quot;bankIssuedInvoiceBarCodeNumber\&quot;: null,                          \&quot;bankIssuedInvoiceBarCodeType\&quot;: null,                          \&quot;billingAddress\&quot;: null                      }                  ]              }          ]      },      \&quot;packageAttachment\&quot;: {          \&quot;packages\&quot;: []      },      \&quot;sellers\&quot;: [          {              \&quot;id\&quot;: \&quot;ppxpssp\&quot;,              \&quot;name\&quot;: \&quot;ppxpssp\&quot;,              \&quot;logo\&quot;: \&quot;\&quot;,              \&quot;fulfillmentEndpoint\&quot;: \&quot;http://fulfillment.vtexcommerce.com.br/api/fulfillment?an&#x3D;ppxpssp&amp;affiliateId&#x3D;SLR&amp;sc&#x3D;1\&quot;          }      ],      \&quot;callCenterOperatorData\&quot;: null,      \&quot;followUpEmail\&quot;: \&quot;0a902f64ba1443c3b26ab5cb0b2aad9e@ct.vtex.com.br\&quot;,      \&quot;lastMessage\&quot;: null,      \&quot;hostname\&quot;: \&quot;ppxps\&quot;,      \&quot;invoiceData\&quot;: null,      \&quot;changesAttachment\&quot;: null,      \&quot;openTextField\&quot;: {          \&quot;value\&quot;: \&quot;Order Created By VTEX Subscription System\&quot;      },      \&quot;roundingError\&quot;: 0,      \&quot;orderFormId\&quot;: \&quot;3d59650b4e9a447d80ecfac4830926d9\&quot;,      \&quot;commercialConditionData\&quot;: null,      \&quot;isCompleted\&quot;: true,      \&quot;customData\&quot;: null,      \&quot;storePreferencesData\&quot;: {          \&quot;countryCode\&quot;: \&quot;BRA\&quot;,          \&quot;currencyCode\&quot;: \&quot;BRL\&quot;,          \&quot;currencyFormatInfo\&quot;: {              \&quot;CurrencyDecimalDigits\&quot;: 2,              \&quot;CurrencyDecimalSeparator\&quot;: \&quot;,\&quot;,              \&quot;CurrencyGroupSeparator\&quot;: \&quot;.\&quot;,              \&quot;CurrencyGroupSize\&quot;: 3,              \&quot;StartsWithCurrencySymbol\&quot;: true          },          \&quot;currencyLocale\&quot;: 1046,          \&quot;currencySymbol\&quot;: \&quot;R$\&quot;,          \&quot;timeZone\&quot;: \&quot;E. South America Standard Time\&quot;      },      \&quot;allowCancellation\&quot;: true,      \&quot;allowEdition\&quot;: false,      \&quot;isCheckedIn\&quot;: false,      \&quot;marketplace\&quot;: null,      \&quot;authorizedDate\&quot;: \&quot;2022-07-06T09:11:56.0006230+00:00\&quot;,      \&quot;invoicedDate\&quot;: null,      \&quot;cancelReason\&quot;: null,      \&quot;itemMetadata\&quot;: {          \&quot;Items\&quot;: [              {                  \&quot;Id\&quot;: \&quot;12\&quot;,                  \&quot;Seller\&quot;: \&quot;1\&quot;,                  \&quot;Name\&quot;: \&quot;Camiseta P Azul\&quot;,                  \&quot;SkuName\&quot;: \&quot;P Azul\&quot;,                  \&quot;ProductId\&quot;: \&quot;8\&quot;,                  \&quot;RefId\&quot;: \&quot;COP01_P-A\&quot;,                  \&quot;Ean\&quot;: null,                  \&quot;ImageUrl\&quot;: \&quot;http://ppxps.vteximg.com.br/arquivos/ids/155407-55-55/EE803C74-37A5-4804-B1A6-9F12D22EA505.png?v&#x3D;637559269453730000\&quot;,                  \&quot;DetailUrl\&quot;: \&quot;/camiseta/p\&quot;,                  \&quot;AssemblyOptions\&quot;: []              }          ]      },      \&quot;subscriptionData\&quot;: {          \&quot;SubscriptionGroupId\&quot;: \&quot;C191822AF072C7508F9BBBC655FE8E60\&quot;,          \&quot;Subscriptions\&quot;: [              {                  \&quot;ExecutionCount\&quot;: 274,                  \&quot;PriceAtSubscriptionDate\&quot;: 2265.0,                  \&quot;ItemIndex\&quot;: 0,                  \&quot;Plan\&quot;: {                      \&quot;type\&quot;: \&quot;RECURRING_PAYMENT\&quot;,                      \&quot;frequency\&quot;: {                          \&quot;periodicity\&quot;: \&quot;DAILY\&quot;,                          \&quot;interval\&quot;: 1                      },                      \&quot;validity\&quot;: {                          \&quot;begin\&quot;: \&quot;2021-10-05T00:00:00.0000000+00:00\&quot;,                          \&quot;end\&quot;: null                      }                  }              }          ]      },      \&quot;taxData\&quot;: null,      \&quot;checkedInPickupPointId\&quot;: null,      \&quot;cancellationData\&quot;: null  }  &#x60;&#x60;&#x60;

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrdersApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let orderId = "1172452900788-01 or seq501456"; // String | Order ID is a unique code that identifies an order. Instead of using `orderId`, you can also make the request using the sequence, a six-digit string that follows the order ID. For example, in order 1268540501456-01 (501456), the sequence is 501456. To use this parameter, replace the value between `{ }` keys in `seq{sequence-number}` with the sequence. For example: `seq501456`.
apiInstance.getOrder(accept, contentType, orderId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **orderId** | **String**| Order ID is a unique code that identifies an order. Instead of using &#x60;orderId&#x60;, you can also make the request using the sequence, a six-digit string that follows the order ID. For example, in order 1268540501456-01 (501456), the sequence is 501456. To use this parameter, replace the value between &#x60;{ }&#x60; keys in &#x60;seq{sequence-number}&#x60; with the sequence. For example: &#x60;seq501456&#x60;. | 

### Return type

[**GetOrder200Response**](GetOrder200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOrders

> ListOrders listOrders(accept, contentType, fCreationDate, opts)

List orders

Retrieves a list of orders according to the filters described below.     The limit of information retrieval is 30 pages, the default number of orders per page is 15 and it is possible to configure it up to 100 using the  &#x60;per_page&#x60; parameter.      Be aware that as of October 3rd, 2018, this endpoint will not return the &#x60;items&#x60; property.     &gt; This should **not** be used for integrations. Use the [orders Feed or hook](https://developers.vtex.com/docs/guides/orders-feed) for this purpose.    This endpoint returns only orders that already have been indexed, which takes approximately four minutes. Because of this, the data retrieved may present inconsistencies. To get live up-to-date information and [build order integrations](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration) use the [orders Feed or hook](https://developers.vtex.com/docs/guides/orders-feed).   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer&#39;s journey.    

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrdersApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let fCreationDate = "'creationDate:[2016-01-01T02:00:00.000Z TO 2021-01-01T01:59:59.999Z]'"; // String | Concatened value sufix `{{creationDate}}` and range date in Timestamp format. To use the `utc` query parameter, to filter orders by time zone, you must also fill the `f_creationDate` date parameter.
let opts = {
  'orderBy': "'v502556llux-01,asc'", // String | You can retrieve orders lists filtering by an `OrderField` combined with an `OrderType`. To do so, you have to concatenate them: `orderBy={{OrderField}},{{OrderType}}`.   - `OrderField` values accepted: `creationDate`, `orderId`, `items`, `totalValue` and `origin`.   - `OrderType` values accepted: `asc` and `desc`.
  'page': 10, // Number | Define the number of pages you wish to retrieve, restricted to the limit of 30 pages.
  'perPage': 15, // Number | Quantity of orders for each page, the default value is 15 and it goes up to 100 orders per page. Be aware that the limit of retrieval ofthis endpoint is 30 pages.
  'fHasInputInvoice': false, // Boolean | Filters list to return only orders with non `null` values for the `invoiceInput` field.
  'q': "'- OrderID: v212333lux-02   - Client email: taylor@email.com   - Client document: 21133355524   - Client name: Taylor'", // String | This parameter filters using Fulltext and accepts the values below. Be aware that the `+` caracter is not allowed in Fulltext Search.   - Order Id   - Client email   - Client document   - Client name
  'utc': -2000, // Number | Converts orders' time zone to the Universal Time Coordinated (UTC) format and shows the amount of orders set for that UTC, up to the limit of 30 pages. For it to work properly, you have to associate it with the `f_creationDate` parameter.
  'fShippingEstimate': "'0.days'", // String | You can filter orders by shipping estimate time in days by concatenating the desired number of days with the sufix `.days`. For example:   - Next 7 days: `7.days`   - Tomorrow: `1.days`   - Today: `0.days`   - Late: `-1.days`
  'fInvoicedDate': "'invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]'", // String | You can filter orders by invoiced date by concatenating the sufix `invoicedDate:` with the range date in Timestamp format. For example:   - 1 Day: `invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]`  - 1 Month: `invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-02-01T01:59:59.999Z]`   - 1 Year: `invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-01-01T01:59:59.999Z]`
  'fAuthorizedDate': "'creationDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]'", // String | You can filter orders by creation date by concatenating the sufix `authorizedDate:` with the range date in Timestamp format. For example:   - 1 Day: `authorizedDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]`  - 1 Month: `authorizedDate:[2022-01-01T02:00:00.000Z TO 2022-02-01T01:59:59.999Z]`   - 1 Year: `authorizedDate:[2022-01-01T02:00:00.000Z TO 2022-01-01T01:59:59.999Z]`
  'fUtmSource': "'christmas_campaign'", // String | You can filter orders by using a Universal Transverse Mercator (UTM) source.
  'fSellerNames': "'SellerName'", // String | You can filter orders by using a seller's name.
  'fCallCenterOperatorName': "'Operator%20Name'", // String | You can filter orders by using a Call Center Operator's identification.
  'fSalesChannel': "'Main'", // String | You can filter orders by sales channel's ([or trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) name.
  'salesChannelId': "'1'", // String | You can filter orders by sales channel's ([or trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) ID.
  'fAffiliateId': "'WLM'", // String | You can filter orders by affiliate ID.
  'fStatus': "'ready-for-handling'", // String | You can filter orders by the following [order status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196):   - `waiting-for-sellers-confirmation`   - `payment-pending`   - `payment-approved`   - `ready-for-handling`   - `handling`   - `invoiced`   - `canceled`
  'incompleteOrders': true, // Boolean | When set as `true`, you retrieve [incomplete orders](https://help.vtex.com/en/tutorial/understanding-incomplete-orders), when set as `false`, you retrieve orders that are not incomplete.
  'fPaymentNames': "'Visa'", // String | You can filter orders by payment type.
  'fRnB': "'Free+Shipping'", // String | You can filter orders by rates and benefits (promotions).
  'searchField': "'  - SKU ID: `25`   - Gift List ID: `11223`   - Transaction ID (TID): `54546300238810034995829230012`   - PCI Connector's Transaction ID (TID): `7032909234899834298423209`   - Payment ID (PID): `2`   - Connector's NSU: `2437281`'", // String | You can search orders by using one of the following criterias:   - SKU ID - `sku_Ids&sku_Ids`   - Gift List ID - `listId&listId`   - Transaction ID (TID) - `tid&tid`   - PCI Connector's Transaction ID (TID) - `pci_tid&pci_tid`   - Payment ID (PID) - `paymentId&paymentId`   - Connector's NSU - `nsu&nsu`
  'fIsInstore': true // Boolean | When set as `true`, this parameter filters orders made via [inStore](https://help.vtex.com/en/tracks/what-is-instore--zav76TFEZlAjnyBVL5tRc), and when set as `false`, it filters orders that were not made via inStore.
};
apiInstance.listOrders(accept, contentType, fCreationDate, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **fCreationDate** | **String**| Concatened value sufix &#x60;{{creationDate}}&#x60; and range date in Timestamp format. To use the &#x60;utc&#x60; query parameter, to filter orders by time zone, you must also fill the &#x60;f_creationDate&#x60; date parameter. | [default to &#39;creationDate:[2016-01-01T02:00:00.000Z TO 2021-01-01T01:59:59.999Z]&#39;]
 **orderBy** | **String**| You can retrieve orders lists filtering by an &#x60;OrderField&#x60; combined with an &#x60;OrderType&#x60;. To do so, you have to concatenate them: &#x60;orderBy&#x3D;{{OrderField}},{{OrderType}}&#x60;.   - &#x60;OrderField&#x60; values accepted: &#x60;creationDate&#x60;, &#x60;orderId&#x60;, &#x60;items&#x60;, &#x60;totalValue&#x60; and &#x60;origin&#x60;.   - &#x60;OrderType&#x60; values accepted: &#x60;asc&#x60; and &#x60;desc&#x60;. | [optional] [default to &#39;v502556llux-01,asc&#39;]
 **page** | **Number**| Define the number of pages you wish to retrieve, restricted to the limit of 30 pages. | [optional] [default to 10]
 **perPage** | **Number**| Quantity of orders for each page, the default value is 15 and it goes up to 100 orders per page. Be aware that the limit of retrieval ofthis endpoint is 30 pages. | [optional] [default to 15]
 **fHasInputInvoice** | **Boolean**| Filters list to return only orders with non &#x60;null&#x60; values for the &#x60;invoiceInput&#x60; field. | [optional] [default to false]
 **q** | **String**| This parameter filters using Fulltext and accepts the values below. Be aware that the &#x60;+&#x60; caracter is not allowed in Fulltext Search.   - Order Id   - Client email   - Client document   - Client name | [optional] [default to &#39;- OrderID: v212333lux-02 
- Client email: taylor@email.com 
- Client document: 21133355524 
- Client name: Taylor&#39;]
 **utc** | **Number**| Converts orders&#39; time zone to the Universal Time Coordinated (UTC) format and shows the amount of orders set for that UTC, up to the limit of 30 pages. For it to work properly, you have to associate it with the &#x60;f_creationDate&#x60; parameter. | [optional] [default to -2000]
 **fShippingEstimate** | **String**| You can filter orders by shipping estimate time in days by concatenating the desired number of days with the sufix &#x60;.days&#x60;. For example:   - Next 7 days: &#x60;7.days&#x60;   - Tomorrow: &#x60;1.days&#x60;   - Today: &#x60;0.days&#x60;   - Late: &#x60;-1.days&#x60; | [optional] [default to &#39;0.days&#39;]
 **fInvoicedDate** | **String**| You can filter orders by invoiced date by concatenating the sufix &#x60;invoicedDate:&#x60; with the range date in Timestamp format. For example:   - 1 Day: &#x60;invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]&#x60;  - 1 Month: &#x60;invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-02-01T01:59:59.999Z]&#x60;   - 1 Year: &#x60;invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-01-01T01:59:59.999Z]&#x60; | [optional] [default to &#39;invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]&#39;]
 **fAuthorizedDate** | **String**| You can filter orders by creation date by concatenating the sufix &#x60;authorizedDate:&#x60; with the range date in Timestamp format. For example:   - 1 Day: &#x60;authorizedDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]&#x60;  - 1 Month: &#x60;authorizedDate:[2022-01-01T02:00:00.000Z TO 2022-02-01T01:59:59.999Z]&#x60;   - 1 Year: &#x60;authorizedDate:[2022-01-01T02:00:00.000Z TO 2022-01-01T01:59:59.999Z]&#x60; | [optional] [default to &#39;creationDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]&#39;]
 **fUtmSource** | **String**| You can filter orders by using a Universal Transverse Mercator (UTM) source. | [optional] [default to &#39;christmas_campaign&#39;]
 **fSellerNames** | **String**| You can filter orders by using a seller&#39;s name. | [optional] [default to &#39;SellerName&#39;]
 **fCallCenterOperatorName** | **String**| You can filter orders by using a Call Center Operator&#39;s identification. | [optional] [default to &#39;Operator%20Name&#39;]
 **fSalesChannel** | **String**| You can filter orders by sales channel&#39;s ([or trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) name. | [optional] [default to &#39;Main&#39;]
 **salesChannelId** | **String**| You can filter orders by sales channel&#39;s ([or trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) ID. | [optional] [default to &#39;1&#39;]
 **fAffiliateId** | **String**| You can filter orders by affiliate ID. | [optional] [default to &#39;WLM&#39;]
 **fStatus** | **String**| You can filter orders by the following [order status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196):   - &#x60;waiting-for-sellers-confirmation&#x60;   - &#x60;payment-pending&#x60;   - &#x60;payment-approved&#x60;   - &#x60;ready-for-handling&#x60;   - &#x60;handling&#x60;   - &#x60;invoiced&#x60;   - &#x60;canceled&#x60; | [optional] [default to &#39;ready-for-handling&#39;]
 **incompleteOrders** | **Boolean**| When set as &#x60;true&#x60;, you retrieve [incomplete orders](https://help.vtex.com/en/tutorial/understanding-incomplete-orders), when set as &#x60;false&#x60;, you retrieve orders that are not incomplete. | [optional] [default to true]
 **fPaymentNames** | **String**| You can filter orders by payment type. | [optional] [default to &#39;Visa&#39;]
 **fRnB** | **String**| You can filter orders by rates and benefits (promotions). | [optional] [default to &#39;Free+Shipping&#39;]
 **searchField** | **String**| You can search orders by using one of the following criterias:   - SKU ID - &#x60;sku_Ids&amp;sku_Ids&#x60;   - Gift List ID - &#x60;listId&amp;listId&#x60;   - Transaction ID (TID) - &#x60;tid&amp;tid&#x60;   - PCI Connector&#39;s Transaction ID (TID) - &#x60;pci_tid&amp;pci_tid&#x60;   - Payment ID (PID) - &#x60;paymentId&amp;paymentId&#x60;   - Connector&#39;s NSU - &#x60;nsu&amp;nsu&#x60; | [optional] [default to &#39;
- SKU ID: &#x60;25&#x60; 
- Gift List ID: &#x60;11223&#x60; 
- Transaction ID (TID): &#x60;54546300238810034995829230012&#x60; 
- PCI Connector&#39;s Transaction ID (TID): &#x60;7032909234899834298423209&#x60; 
- Payment ID (PID): &#x60;2&#x60; 
- Connector&#39;s NSU: &#x60;2437281&#x60;&#39;]
 **fIsInstore** | **Boolean**| When set as &#x60;true&#x60;, this parameter filters orders made via [inStore](https://help.vtex.com/en/tracks/what-is-instore--zav76TFEZlAjnyBVL5tRc), and when set as &#x60;false&#x60;, it filters orders that were not made via inStore. | [optional] [default to true]

### Return type

[**ListOrders**](ListOrders.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## registerChange

> RegisterChange registerChange(contentType, accept, orderId, registerChangeRequest)

Register change on order

  &gt; Timeout settings  &gt;  &gt; This is a synchronous API, which means the application requests data and waits until a value is returned. This behavior can cause timeout errors; to avoid them, we recommend setting the timeout in 20 seconds.     This request allows [changing an order](https://help.vtex.com/en/tutorial/changing-items-from-a-completed-order--tutorials_190) by:  - Adding items to an order  - Removing items from an order  - Applying discounts to the total value of the order  - Incrementing the total value of the order.   In those scenarios of order changes, it is possible to insert a [Partial invoice](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe). The total value of the order will be updated after the insertion of the invoice, even when there is a partial invoice scenario. The updated value is settled by VTEX&#39;s Payment Gateway. The reimbursement for the shopper is automatic.     This action can only be done for orders in these status:  - &#x60;handling&#x60;  - &#x60;waiting-for-fulfillment&#x60;     &gt; The &#x60;Change order&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrdersApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let orderId = "1172452900788-01"; // String | ID that identifies the order in the seller.
let registerChangeRequest = {"discountValue":1000,"incrementValue":0,"itemsAdded":[{"id":"234788","price":200,"quantity":1}],"itemsRemoved":[{"id":"234794","price":600,"quantity":2}],"reason":"Promoção dada por telefone","requestId":"change-request-0123"}; // RegisterChangeRequest | 
apiInstance.registerChange(contentType, accept, orderId, registerChangeRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **orderId** | **String**| ID that identifies the order in the seller. | 
 **registerChangeRequest** | [**RegisterChangeRequest**](RegisterChangeRequest.md)|  | 

### Return type

[**RegisterChange**](RegisterChange.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startHandling

> startHandling(accept, contentType, orderId)

Start handling order

Changes the status of an order to indicate that it is in &#x60;handling&#x60;.    &gt; Expect a &#x60;status 204&#x60; response with no content in case of a successful request. The store must validate this response to retry the call if the response differs from the &#x60;204&#x60; code, making this flow the store&#39;s responsibility. This endpoint can also respond with &#x60;status 500&#x60;.     &gt; The &#x60;Change order workflow status&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrdersApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let orderId = "1172452900788-01"; // String | Order ID is a unique code that identifies an order.
apiInstance.startHandling(accept, contentType, orderId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **orderId** | **String**| Order ID is a unique code that identifies an order. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

