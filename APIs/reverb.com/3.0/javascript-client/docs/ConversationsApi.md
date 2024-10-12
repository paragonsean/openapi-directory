# Reverb.ConversationsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversationsConversationIdOfferPost**](ConversationsApi.md#conversationsConversationIdOfferPost) | **POST** /conversations/{conversation_id}/offer | Make an offer to the other participant in the conversation
[**conversationsIdOfferPost**](ConversationsApi.md#conversationsIdOfferPost) | **POST** /conversations/{id}/offer | Make an offer to the other participant in the conversation



## conversationsConversationIdOfferPost

> conversationsConversationIdOfferPost(conversationId, opts)

Make an offer to the other participant in the conversation

Make an offer to the other participant in the conversation

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ConversationsApi();
let conversationId = "conversationId_example"; // String | 
let opts = {
  'conversationsConversationIdOfferPostRequest': new Reverb.ConversationsConversationIdOfferPostRequest() // ConversationsConversationIdOfferPostRequest | the content of the request
};
apiInstance.conversationsConversationIdOfferPost(conversationId, opts, (error, data, response) => {
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
 **conversationId** | **String**|  | 
 **conversationsConversationIdOfferPostRequest** | [**ConversationsConversationIdOfferPostRequest**](ConversationsConversationIdOfferPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## conversationsIdOfferPost

> conversationsIdOfferPost(id, opts)

Make an offer to the other participant in the conversation

Make an offer to the other participant in the conversation

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ConversationsApi();
let id = "id_example"; // String | 
let opts = {
  'conversationsIdOfferPostRequest': new Reverb.ConversationsIdOfferPostRequest() // ConversationsIdOfferPostRequest | the content of the request
};
apiInstance.conversationsIdOfferPost(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **conversationsIdOfferPostRequest** | [**ConversationsIdOfferPostRequest**](ConversationsIdOfferPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

