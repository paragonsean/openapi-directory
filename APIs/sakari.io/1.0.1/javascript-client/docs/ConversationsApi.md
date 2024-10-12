# Sakari.ConversationsApi

All URIs are relative to *https://api.sakari.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversationsClose**](ConversationsApi.md#conversationsClose) | **PUT** /v1/accounts/{accountId}/conversations/{conversationId}/close | Closes a conversation
[**conversationsFetch**](ConversationsApi.md#conversationsFetch) | **GET** /v1/accounts/{accountId}/conversations/{conversationId} | Fetch conversation by ID
[**conversationsFetchAll**](ConversationsApi.md#conversationsFetchAll) | **GET** /v1/accounts/{accountId}/conversations | Fetch conversations



## conversationsClose

> ConversationResponse conversationsClose(accountId, conversationId)

Closes a conversation

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ConversationsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let conversationId = "conversationId_example"; // String | ID of conversation
apiInstance.conversationsClose(accountId, conversationId, (error, data, response) => {
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
 **conversationId** | **String**| ID of conversation | 

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsFetch

> ConversationResponse conversationsFetch(accountId, conversationId)

Fetch conversation by ID

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ConversationsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let conversationId = "conversationId_example"; // String | ID of template to return
apiInstance.conversationsFetch(accountId, conversationId, (error, data, response) => {
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
 **conversationId** | **String**| ID of template to return | 

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsFetchAll

> ConversationsResponse conversationsFetchAll(accountId, opts)

Fetch conversations

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ConversationsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'offset': 789, // Number | Results to skip when paginating through a result set
  'limit': 789 // Number | Maximum number of results to return
};
apiInstance.conversationsFetchAll(accountId, opts, (error, data, response) => {
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

### Return type

[**ConversationsResponse**](ConversationsResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

