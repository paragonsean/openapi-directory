# MessagesApi.DefaultApi

All URIs are relative to *https://api.nexmo.com/v1/messages*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendMessage**](DefaultApi.md#sendMessage) | **POST** / | Send a message to the given channel.



## sendMessage

> SendMessage202Response sendMessage(sendMessageRequest)

Send a message to the given channel.

Send a Message

### Example

```javascript
import MessagesApi from 'messages_api';
let defaultClient = MessagesApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MessagesApi.DefaultApi();
let sendMessageRequest = new MessagesApi.SendMessageRequest(); // SendMessageRequest | Send a Message.
apiInstance.sendMessage(sendMessageRequest, (error, data, response) => {
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
 **sendMessageRequest** | [**SendMessageRequest**](SendMessageRequest.md)| Send a Message. | 

### Return type

[**SendMessage202Response**](SendMessage202Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

