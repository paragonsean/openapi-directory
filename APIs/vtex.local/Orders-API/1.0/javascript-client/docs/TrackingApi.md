# OrdersApi.TrackingApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateTrackingStatus**](TrackingApi.md#updateTrackingStatus) | **PUT** /api/oms/pvt/orders/{orderId}/invoice/{invoiceNumber}/tracking | Update order tracking status



## updateTrackingStatus

> UpdateTrackingStatus updateTrackingStatus(contentType, accept, orderId, invoiceNumber, updateTrackingStatusRequest)

Update order tracking status

This endpoint sends a tracking event to an order that already has a tracking number registered to its invoice.    This request is not meant to send tracking number and URL to the invoice. If you wish to send tracking number and URL to an order, use the [Update order&#39;s partial invoice API request](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/oms/pvt/orders/-orderId-/invoice/-invoiceNumber-). You can also learn more about [Partial invoice](https://help.vtex.com/en/tracks/partial-invoices--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenarios.     &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc).

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

let apiInstance = new OrdersApi.TrackingApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let orderId = "1172452900788-01"; // String | Order ID is a unique code that identifies an order.
let invoiceNumber = "000030711"; // String | Number that identifies the invoice.
let updateTrackingStatusRequest = {"deliveredDate":"2022-10-01 21:15","events":[{"city":"Rio de Janeiro","date":"2015-06-23","description":"Coletado pela transportadora","state":"RJ"},{"city":"Sao Paulo","date":"2015-06-24","description":"A caminho de Curitiba","state":"SP"}],"isDelivered":false}; // UpdateTrackingStatusRequest | 
apiInstance.updateTrackingStatus(contentType, accept, orderId, invoiceNumber, updateTrackingStatusRequest, (error, data, response) => {
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
 **orderId** | **String**| Order ID is a unique code that identifies an order. | 
 **invoiceNumber** | **String**| Number that identifies the invoice. | 
 **updateTrackingStatusRequest** | [**UpdateTrackingStatusRequest**](UpdateTrackingStatusRequest.md)|  | 

### Return type

[**UpdateTrackingStatus**](UpdateTrackingStatus.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

