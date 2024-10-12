# WebhookApi.WebhooksApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventLogsAll**](WebhooksApi.md#eventLogsAll) | **GET** /webhook/logs | List event logs
[**webhooksAdd**](WebhooksApi.md#webhooksAdd) | **POST** /webhook/webhooks | Create webhook subscription
[**webhooksAll**](WebhooksApi.md#webhooksAll) | **GET** /webhook/webhooks | List webhook subscriptions
[**webhooksDelete**](WebhooksApi.md#webhooksDelete) | **DELETE** /webhook/webhooks/{id} | Delete webhook subscription
[**webhooksOne**](WebhooksApi.md#webhooksOne) | **GET** /webhook/webhooks/{id} | Get webhook subscription
[**webhooksUpdate**](WebhooksApi.md#webhooksUpdate) | **PATCH** /webhook/webhooks/{id} | Update webhook subscription



## eventLogsAll

> GetWebhookEventLogsResponse eventLogsAll(xApideckAppId, opts)

List event logs

List event logs

### Example

```javascript
import WebhookApi from 'webhook_api';
let defaultClient = WebhookApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new WebhookApi.WebhooksApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20, // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
  'filter': new WebhookApi.WebhookEventLogsFilter() // WebhookEventLogsFilter | Filter results
};
apiInstance.eventLogsAll(xApideckAppId, opts, (error, data, response) => {
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
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20]
 **filter** | [**WebhookEventLogsFilter**](.md)| Filter results | [optional] 

### Return type

[**GetWebhookEventLogsResponse**](GetWebhookEventLogsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksAdd

> CreateWebhookResponse webhooksAdd(xApideckAppId, createWebhookRequest)

Create webhook subscription

Create a webhook subscription to receive events

### Example

```javascript
import WebhookApi from 'webhook_api';
let defaultClient = WebhookApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new WebhookApi.WebhooksApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let createWebhookRequest = new WebhookApi.CreateWebhookRequest(); // CreateWebhookRequest | 
apiInstance.webhooksAdd(xApideckAppId, createWebhookRequest, (error, data, response) => {
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
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **createWebhookRequest** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 

### Return type

[**CreateWebhookResponse**](CreateWebhookResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webhooksAll

> GetWebhooksResponse webhooksAll(xApideckAppId, opts)

List webhook subscriptions

List all webhook subscriptions

### Example

```javascript
import WebhookApi from 'webhook_api';
let defaultClient = WebhookApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new WebhookApi.WebhooksApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20 // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
};
apiInstance.webhooksAll(xApideckAppId, opts, (error, data, response) => {
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
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20]

### Return type

[**GetWebhooksResponse**](GetWebhooksResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksDelete

> DeleteWebhookResponse webhooksDelete(id, xApideckAppId)

Delete webhook subscription

Delete a webhook subscription

### Example

```javascript
import WebhookApi from 'webhook_api';
let defaultClient = WebhookApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new WebhookApi.WebhooksApi();
let id = "id_example"; // String | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
apiInstance.webhooksDelete(id, xApideckAppId, (error, data, response) => {
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
 **id** | **String**| JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. | 
 **xApideckAppId** | **String**| The ID of your Unify application | 

### Return type

[**DeleteWebhookResponse**](DeleteWebhookResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksOne

> GetWebhookResponse webhooksOne(id, xApideckAppId)

Get webhook subscription

Get the webhook subscription details

### Example

```javascript
import WebhookApi from 'webhook_api';
let defaultClient = WebhookApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new WebhookApi.WebhooksApi();
let id = "id_example"; // String | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
apiInstance.webhooksOne(id, xApideckAppId, (error, data, response) => {
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
 **id** | **String**| JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. | 
 **xApideckAppId** | **String**| The ID of your Unify application | 

### Return type

[**GetWebhookResponse**](GetWebhookResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksUpdate

> UpdateWebhookResponse webhooksUpdate(id, xApideckAppId, updateWebhookRequest)

Update webhook subscription

Update a webhook subscription

### Example

```javascript
import WebhookApi from 'webhook_api';
let defaultClient = WebhookApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new WebhookApi.WebhooksApi();
let id = "id_example"; // String | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let updateWebhookRequest = new WebhookApi.UpdateWebhookRequest(); // UpdateWebhookRequest | 
apiInstance.webhooksUpdate(id, xApideckAppId, updateWebhookRequest, (error, data, response) => {
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
 **id** | **String**| JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **updateWebhookRequest** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | 

### Return type

[**UpdateWebhookResponse**](UpdateWebhookResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

