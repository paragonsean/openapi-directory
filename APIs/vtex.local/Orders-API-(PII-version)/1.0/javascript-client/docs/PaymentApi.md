# OrdersApiPiiVersion.PaymentApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendPaymentNotification2**](PaymentApi.md#sendPaymentNotification2) | **POST** /api/orders/pvt/document/{orderId}/payment/{paymentId}/notify-payment | Send payment notification



## sendPaymentNotification2

> sendPaymentNotification2(contentType, accept, orderId, paymentId)

Send payment notification

Send a payment notification of a given order, by order ID and payment ID.    &gt; The &#x60;Notify payment&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).    &gt; Learn more about [Transaction Details](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details).      ## Request body properties    | Attribute    | Type        | Description |  | --------------- |:---------:| --------------------------------------:|  | &#x60;orderId&#x60; | string | Order Id |  | &#x60;paymentId&#x60; | string | Payment ID |

### Example

```javascript
import OrdersApiPiiVersion from 'orders_api__pii_version';
let defaultClient = OrdersApiPiiVersion.ApiClient.instance;
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

let apiInstance = new OrdersApiPiiVersion.PaymentApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let orderId = "70caf3941s6df1"; // String | ID of the order.
let paymentId = "45hsfg5jkyu1384jdsfgh654sfgj1"; // String | ID of the payment.
apiInstance.sendPaymentNotification2(contentType, accept, orderId, paymentId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **orderId** | **String**| ID of the order. | 
 **paymentId** | **String**| ID of the payment. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

