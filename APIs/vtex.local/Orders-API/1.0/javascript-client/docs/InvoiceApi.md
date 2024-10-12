# OrdersApi.InvoiceApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoiceNotification**](InvoiceApi.md#invoiceNotification) | **POST** /api/oms/pvt/orders/{orderId}/invoice | Order invoice notification
[**updatepartialinvoiceSendTrackingNumber**](InvoiceApi.md#updatepartialinvoiceSendTrackingNumber) | **PATCH** /api/oms/pvt/orders/{orderId}/invoice/{invoiceNumber} | Update order&#39;s partial invoice (send tracking number)



## invoiceNotification

> CancelOrder200Response invoiceNotification(accept, contentType, orderId, invoiceNotificationRequest)

Order invoice notification

Entering the [invoice in the order](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/2WgQrlHTyVo4hLjhUs1LMT) is a required step for its [status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196#order-status-details) to change to Invoiced - a sign that the order has been successfully completed. Remember that once an order is read as invoiced by the system, this status cannot be changed.   The total value of the order will be updated after the insertion of the invoice, even when there&#39;s a [Partial invoice](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenario. The updated value is settled by VTEX&#39;s Payment Gateway. The reimbursement for the shopper is automatic.   We strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided.   When returning items, an input invoice must be sent through this call. For that, the &#x60;type&#x60; field should be filled in with &#x60;input&#x60;.   It is not allowed to use the same &#x60;invoiceNumber&#x60; in more than one request to the Order Invoice Notification endpoint.  For marketplace integrations: once the order is invoiced, the seller should use this request to send the invoice information to the marketplace. Be aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a separate moment, once the seller has the tracking information.      &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer&#39;s journey.    

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

let apiInstance = new OrdersApi.InvoiceApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let orderId = "1172452900788-01"; // String | Unique code that identifies the order whose invoice is being sent.
let invoiceNotificationRequest = {"courier":null,"dispatchedDate":null,"invoiceKey":null,"invoiceNumber":"9999","invoiceUrl":"link","invoiceValue":"10000","issuanceDate":"2019-01-31T18:25:43-05:00","items":[{"description":"335","id":"1234","price":10000,"quantity":1}],"trackingNumber":null,"trackingUrl":null,"type":"Output"}; // InvoiceNotificationRequest | 
apiInstance.invoiceNotification(accept, contentType, orderId, invoiceNotificationRequest, (error, data, response) => {
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
 **orderId** | **String**| Unique code that identifies the order whose invoice is being sent. | 
 **invoiceNotificationRequest** | [**InvoiceNotificationRequest**](InvoiceNotificationRequest.md)|  | 

### Return type

[**CancelOrder200Response**](CancelOrder200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatepartialinvoiceSendTrackingNumber

> UpdatepartialinvoiceSendTrackingNumber updatepartialinvoiceSendTrackingNumber(contentType, accept, orderId, invoiceNumber, updatepartialinvoiceSendTrackingNumberRequest)

Update order&#39;s partial invoice (send tracking number)

Update a given order, adding its tracking number to its [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe).    After using this call to add a tracking number to an order, you can use the [Update order tracking status](https://developers.vtex.com/vtex-rest-api/reference/tracking#updatetrackingstatus) API request to add tracking events.    &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc).

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

let apiInstance = new OrdersApi.InvoiceApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let orderId = "1172452900788-01"; // String | Unique code that identifies the order whose invoice is being sent.
let invoiceNumber = "000030711"; // String | Number that identifies the invoice.
let updatepartialinvoiceSendTrackingNumberRequest = {"courier":"carrierOne","dispatchedDate":"2022-02-08T13:16:13.4617653+00:00","trackingNumber":"87658","trackingUrl":"https://www.tracking.com/url"}; // UpdatepartialinvoiceSendTrackingNumberRequest | 
apiInstance.updatepartialinvoiceSendTrackingNumber(contentType, accept, orderId, invoiceNumber, updatepartialinvoiceSendTrackingNumberRequest, (error, data, response) => {
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
 **orderId** | **String**| Unique code that identifies the order whose invoice is being sent. | 
 **invoiceNumber** | **String**| Number that identifies the invoice. | 
 **updatepartialinvoiceSendTrackingNumberRequest** | [**UpdatepartialinvoiceSendTrackingNumberRequest**](UpdatepartialinvoiceSendTrackingNumberRequest.md)|  | 

### Return type

[**UpdatepartialinvoiceSendTrackingNumber**](UpdatepartialinvoiceSendTrackingNumber.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

