# WhatsAppBusinessApi.MessagesApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markMessageAsRead**](MessagesApi.md#markMessageAsRead) | **PUT** /messages/{MessageID} | Mark-Message-As-Read
[**sendMessage**](MessagesApi.md#sendMessage) | **POST** /messages | Send-Message



## markMessageAsRead

> markMessageAsRead(messageID, markMessageAsReadRequestBody)

Mark-Message-As-Read

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.MessagesApi();
let messageID = "messageID_example"; // String | Message ID from Webhook
let markMessageAsReadRequestBody = {"status":"read"}; // MarkMessageAsReadRequestBody | 
apiInstance.markMessageAsRead(messageID, markMessageAsReadRequestBody, (error, data, response) => {
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
 **messageID** | **String**| Message ID from Webhook | 
 **markMessageAsReadRequestBody** | [**MarkMessageAsReadRequestBody**](MarkMessageAsReadRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## sendMessage

> MessageResponse sendMessage(sendMessageRequestBody)

Send-Message

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.MessagesApi();
let sendMessageRequestBody = {"recipient_type":"individual","text":{"body":"<Message Text>"},"to":"{{Recipient-WA-ID}}","type":"text"}; // SendMessageRequestBody | 
apiInstance.sendMessage(sendMessageRequestBody, (error, data, response) => {
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
 **sendMessageRequestBody** | [**SendMessageRequestBody**](SendMessageRequestBody.md)|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

