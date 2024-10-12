# OrdersApi.ConversationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConversation**](ConversationApi.md#getConversation) | **GET** /api/oms/pvt/orders/{orderId}/conversation-message | Retrieve order conversation



## getConversation

> [GetConversation] getConversation(accept, contentType, orderId, opts)

Retrieve order conversation

List all order conversations of an order by its order ID.

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

let apiInstance = new OrdersApi.ConversationApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let orderId = "1172452900788-01"; // String | Order ID is a unique code that identifies an order.
let opts = {
  'reason': "data-validation" // String | Reason for requesting unmasked data. Relevant only for PII platform version.
};
apiInstance.getConversation(accept, contentType, orderId, opts, (error, data, response) => {
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
 **orderId** | **String**| Order ID is a unique code that identifies an order. | 
 **reason** | **String**| Reason for requesting unmasked data. Relevant only for PII platform version. | [optional] 

### Return type

[**[GetConversation]**](GetConversation.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

