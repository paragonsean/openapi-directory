# OrdersApiPiiVersion.InvoiceApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoiceNotification2**](InvoiceApi.md#invoiceNotification2) | **POST** /api/orders/pvt/document/{orderId}/invoices | Order invoice notification



## invoiceNotification2

> CancelOrder2200Response invoiceNotification2(contentType, accept, orderId, invoiceNotificationRequest)

Order invoice notification

Once the order is invoiced, the seller should use this request to send the invoice information to the marketplace.  We strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided.  It is not allowed to use the same &#x60;invoiceNumber&#x60; in more than one request to the Order Invoice Notification endpoint.  Be aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a separate moment, once the seller has the tracking information.    &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).

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

let apiInstance = new OrdersApiPiiVersion.InvoiceApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let orderId = "70caf3941s6df1"; // String | ID of the order.
let invoiceNotificationRequest = {"courier":null,"dispatchedDate":null,"invoiceKey":null,"invoiceNumber":"9999","invoiceUrl":null,"invoiceValue":"10000","issuanceDate":"2010-01-31","items":[{"id":"1234","price":10000,"quantity":1}],"trackingNumber":null,"trackingUrl":null,"type":"Output"}; // InvoiceNotificationRequest | 
apiInstance.invoiceNotification2(contentType, accept, orderId, invoiceNotificationRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **orderId** | **String**| ID of the order. | 
 **invoiceNotificationRequest** | [**InvoiceNotificationRequest**](InvoiceNotificationRequest.md)|  | 

### Return type

[**CancelOrder2200Response**](CancelOrder2200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

