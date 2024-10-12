# RestApiVersion2.IncomingWebhooksApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIncomingWebhook**](IncomingWebhooksApi.md#createIncomingWebhook) | **POST** /webhooks/incoming/create/{conversationId} | Create a new webhook for existing conversation.
[**deleteIncomingWebhook**](IncomingWebhooksApi.md#deleteIncomingWebhook) | **DELETE** /webhooks/incoming/{webhookId} | Delete an existing webhook
[**getIncomingWebhookByUser**](IncomingWebhooksApi.md#getIncomingWebhookByUser) | **GET** /webhooks/incoming/user/{userId} | Get all webhooks of a special user.
[**postWebhookAsSlackMessage**](IncomingWebhooksApi.md#postWebhookAsSlackMessage) | **POST** /webhooks/incoming/{webhookId} | Post text item for conversation via webhook.



## createIncomingWebhook

> IncomingWebhook createIncomingWebhook(conversationId, opts)

Create a new webhook for existing conversation.

Create a new webhook. Conversation must exist and creater has to be participant. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.IncomingWebhooksApi();
let conversationId = "conversationId_example"; // String | The id of the conversation.
let opts = {
  'name': "name_example", // String | The name of the webhook
  'userId': "userId_example", // String | The id of the user of the webhook
  'description': "description_example" // String | A short description of the webhook
};
apiInstance.createIncomingWebhook(conversationId, opts, (error, data, response) => {
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
 **conversationId** | **String**| The id of the conversation. | 
 **name** | **String**| The name of the webhook | [optional] 
 **userId** | **String**| The id of the user of the webhook | [optional] 
 **description** | **String**| A short description of the webhook | [optional] 

### Return type

[**IncomingWebhook**](IncomingWebhook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteIncomingWebhook

> deleteIncomingWebhook(webhookId)

Delete an existing webhook

Delete a new webhook. Webhook must exist OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.IncomingWebhooksApi();
let webhookId = "webhookId_example"; // String | The id of the webhook
apiInstance.deleteIncomingWebhook(webhookId, (error, data, response) => {
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
 **webhookId** | **String**| The id of the webhook | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIncomingWebhookByUser

> [IncomingWebhook] getIncomingWebhookByUser(userId, opts)

Get all webhooks of a special user.

Get all webhooks of a special user. OauthScopes: READ_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.IncomingWebhooksApi();
let userId = "userId_example"; // String | The id of the user.
let opts = {
  'pagesize': 25, // Number | Max number of hooks per request. Default is 25
  'searchpointer': "searchpointer_example" // String | Start of search if consequtive call.
};
apiInstance.getIncomingWebhookByUser(userId, opts, (error, data, response) => {
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
 **userId** | **String**| The id of the user. | 
 **pagesize** | **Number**| Max number of hooks per request. Default is 25 | [optional] [default to 25]
 **searchpointer** | **String**| Start of search if consequtive call. | [optional] 

### Return type

[**[IncomingWebhook]**](IncomingWebhook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## postWebhookAsSlackMessage

> postWebhookAsSlackMessage(webhookId, opts)

Post text item for conversation via webhook.

Post text items to conversations via slack apps.

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';

let apiInstance = new RestApiVersion2.IncomingWebhooksApi();
let webhookId = "webhookId_example"; // String | The id of the webhook.
let opts = {
  'fileURL': "fileURL_example", // String | missing documentation
  'filename': "filename_example", // String | missing documentation
  'markdown': true, // Boolean | missing documentation
  'subject': "subject_example", // String | missing documentation
  'text': "text_example" // String | The text which will occur in the conversation. May contain formats like *bold* or _italic_
};
apiInstance.postWebhookAsSlackMessage(webhookId, opts, (error, data, response) => {
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
 **webhookId** | **String**| The id of the webhook. | 
 **fileURL** | **String**| missing documentation | [optional] 
 **filename** | **String**| missing documentation | [optional] 
 **markdown** | **Boolean**| missing documentation | [optional] 
 **subject** | **String**| missing documentation | [optional] 
 **text** | **String**| The text which will occur in the conversation. May contain formats like *bold* or _italic_ | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

