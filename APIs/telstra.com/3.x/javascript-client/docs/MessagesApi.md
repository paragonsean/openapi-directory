# MessagingApiV3X.MessagesApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMessageById**](MessagesApi.md#deleteMessageById) | **DELETE** /messages/{messageId} | delete a message
[**getMessageById**](MessagesApi.md#getMessageById) | **GET** /messages/{messageId} | fetch a specific message
[**getMessages**](MessagesApi.md#getMessages) | **GET** /messages | fetch all sent/received messages
[**sendMessages**](MessagesApi.md#sendMessages) | **POST** /messages | send messages
[**updateMessageById**](MessagesApi.md#updateMessageById) | **PUT** /messages/{messageId} | update a message
[**updateMessageTags**](MessagesApi.md#updateMessageTags) | **PATCH** /messages/{messageId} | update message tags



## deleteMessageById

> deleteMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, opts)

delete a message

Use this endpoint to delete a message that&#39;s been scheduled for sending, but hasn&#39;t yet sent. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.MessagesApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let messageId = "messageId_example"; // String | When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints. 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.deleteMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **messageId** | **String**| When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints.  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessageById

> MessageGet getMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, opts)

fetch a specific message

Use the **messageId** to fetch a message that&#39;s been sent from/to your account within the last 30 days. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.MessagesApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let messageId = "messageId_example"; // String | When you sent the original message, this is the UUID that was returned in the response. Use this ID to fetch, update or delete a message with the appropriate endpoints.   Incoming messages are also assigned a messageId. Use this ID with GET/ messages/{messageId} to fetch the message later. 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.getMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **messageId** | **String**| When you sent the original message, this is the UUID that was returned in the response. Use this ID to fetch, update or delete a message with the appropriate endpoints.   Incoming messages are also assigned a messageId. Use this ID with GET/ messages/{messageId} to fetch the message later.  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**MessageGet**](MessageGet.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessages

> GetMessages200Response getMessages(contentLanguage, authorization, accept, acceptCharset, contentType, opts)

fetch all sent/received messages

Fetch messages that have been sent from/to your account in the last 30 days.

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.MessagesApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let opts = {
  'telstraApiVersion': "3.1.0", // String | 
  'limit': 10, // Number | Tell us how many results you want us to return, up to a maximum of 50. 
  'offset': 0, // Number | Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on. 
  'direction': "direction_example", // String | Filter your messages by direction: * **outgoing** – messages sent from your account. * **incoming** – messages sent to your account. 
  'status': "status_example", // String | Filter your messages by one of the statuses below:  * **queued** – messages queued for sending or still in transit. * **sent** – messages that have been sent from the server. * **delivered** – messages successful delivered to the recipient's device. Note that we will only be able to return this status if you set deliveryNotification to **true** (paid feature).  * **expired** – message that couldn't be sent within the **retryTimeout** timeframe. 
  'filter': "filter_example" // String | Filter your messages by:  * tag - use one of the tags assigned to your message(s) * number - either the Virtual Number used to send the message, or the Recipient Number the message was sent to. 
};
apiInstance.getMessages(contentLanguage, authorization, accept, acceptCharset, contentType, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **telstraApiVersion** | **String**|  | [optional] 
 **limit** | **Number**| Tell us how many results you want us to return, up to a maximum of 50.  | [optional] [default to 10]
 **offset** | **Number**| Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on.  | [optional] [default to 0]
 **direction** | **String**| Filter your messages by direction: * **outgoing** – messages sent from your account. * **incoming** – messages sent to your account.  | [optional] 
 **status** | **String**| Filter your messages by one of the statuses below:  * **queued** – messages queued for sending or still in transit. * **sent** – messages that have been sent from the server. * **delivered** – messages successful delivered to the recipient&#39;s device. Note that we will only be able to return this status if you set deliveryNotification to **true** (paid feature).  * **expired** – message that couldn&#39;t be sent within the **retryTimeout** timeframe.  | [optional] 
 **filter** | **String**| Filter your messages by:  * tag - use one of the tags assigned to your message(s) * number - either the Virtual Number used to send the message, or the Recipient Number the message was sent to.  | [optional] 

### Return type

[**GetMessages200Response**](GetMessages200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendMessages

> MessageSent sendMessages(contentLanguage, authorization, accept, acceptCharset, contentType, sendMessagesRequest, opts)

send messages

Send an SMS/MMS to a mobile number, or to multiple mobile numbers.  Free Trial users can message to up to 10 unique recipient numbers for free. The first five recipients will be automatically added to your Free Trial Numbers list. Need more? Just use the POST /free-trial-numbers call to add another five. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.MessagesApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let sendMessagesRequest = new MessagingApiV3X.SendMessagesRequest(); // SendMessagesRequest | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.sendMessages(contentLanguage, authorization, accept, acceptCharset, contentType, sendMessagesRequest, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **sendMessagesRequest** | [**SendMessagesRequest**](SendMessagesRequest.md)|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**MessageSent**](MessageSent.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMessageById

> MessageUpdate updateMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, updateMessageByIdRequest, opts)

update a message

Need to update a message that&#39;s scheduled for sending? You can change any of the below parameters, as long as the message hasn&#39;t been sent yet. This request body will override the original POST/ messages call. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.MessagesApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let messageId = "messageId_example"; // String | When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints. 
let updateMessageByIdRequest = new MessagingApiV3X.UpdateMessageByIdRequest(); // UpdateMessageByIdRequest | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.updateMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, updateMessageByIdRequest, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **messageId** | **String**| When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints.  | 
 **updateMessageByIdRequest** | [**UpdateMessageByIdRequest**](UpdateMessageByIdRequest.md)|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**MessageUpdate**](MessageUpdate.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMessageTags

> updateMessageTags(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, updateMessageTagsRequest, opts)

update message tags

Use the **messageId** to update the tag(s) assigned to a message. You can use this endpoint any time, even after your message has been delivered. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.MessagesApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let messageId = "messageId_example"; // String | When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints. 
let updateMessageTagsRequest = new MessagingApiV3X.UpdateMessageTagsRequest(); // UpdateMessageTagsRequest | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.updateMessageTags(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, updateMessageTagsRequest, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **messageId** | **String**| When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints.  | 
 **updateMessageTagsRequest** | [**UpdateMessageTagsRequest**](UpdateMessageTagsRequest.md)|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

