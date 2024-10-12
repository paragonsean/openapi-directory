# Sakari.MessagesApi

All URIs are relative to *https://api.sakari.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messagesFetch**](MessagesApi.md#messagesFetch) | **GET** /v1/accounts/{accountId}/messages/{messageId} | Fetch message by id
[**messagesFetchAll**](MessagesApi.md#messagesFetchAll) | **GET** /v1/accounts/{accountId}/messages | Fetch messages
[**messagesSend**](MessagesApi.md#messagesSend) | **POST** /v1/accounts/{accountId}/messages | Send Messages



## messagesFetch

> MessageResponse messagesFetch(accountId, messageId)

Fetch message by id

Returns a single messag

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.MessagesApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let messageId = "messageId_example"; // String | ID of message to return
apiInstance.messagesFetch(accountId, messageId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **messageId** | **String**| ID of message to return | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesFetchAll

> MessagesResponse messagesFetchAll(accountId, opts)

Fetch messages

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.MessagesApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'offset': 789, // Number | Results to skip when paginating through a result set
  'limit': 789, // Number | Maximum number of results to return
  'contactId': "contactId_example", // String | ID of contact
  'conversationId': "conversationId_example" // String | ID of conversation
};
apiInstance.messagesFetchAll(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **offset** | **Number**| Results to skip when paginating through a result set | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] 
 **contactId** | **String**| ID of contact | [optional] 
 **conversationId** | **String**| ID of conversation | [optional] 

### Return type

[**MessagesResponse**](MessagesResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesSend

> SendMessagesResponse messagesSend(accountId, opts)

Send Messages

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.MessagesApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'sendMessagesRequest': new Sakari.SendMessagesRequest() // SendMessagesRequest | 
};
apiInstance.messagesSend(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **sendMessagesRequest** | [**SendMessagesRequest**](SendMessagesRequest.md)|  | [optional] 

### Return type

[**SendMessagesResponse**](SendMessagesResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

