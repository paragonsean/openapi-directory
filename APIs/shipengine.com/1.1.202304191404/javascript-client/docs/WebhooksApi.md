# ShipEngineApi.WebhooksApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWebhook**](WebhooksApi.md#createWebhook) | **POST** /v1/environment/webhooks | Create a Webhook
[**deleteWebhook**](WebhooksApi.md#deleteWebhook) | **DELETE** /v1/environment/webhooks/{webhook_id} | Delete Webhook By ID
[**getWebhookById**](WebhooksApi.md#getWebhookById) | **GET** /v1/environment/webhooks/{webhook_id} | Get Webhook By ID
[**listWebhooks**](WebhooksApi.md#listWebhooks) | **GET** /v1/environment/webhooks | List Webhooks
[**updateWebhook**](WebhooksApi.md#updateWebhook) | **PUT** /v1/environment/webhooks/{webhook_id} | Update a Webhook



## createWebhook

> CreateWebhookResponseBody createWebhook(createWebhookRequestBody)

Create a Webhook

Create a webook for specific events in the environment.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WebhooksApi();
let createWebhookRequestBody = new ShipEngineApi.CreateWebhookRequestBody(); // CreateWebhookRequestBody | 
apiInstance.createWebhook(createWebhookRequestBody, (error, data, response) => {
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
 **createWebhookRequestBody** | [**CreateWebhookRequestBody**](CreateWebhookRequestBody.md)|  | 

### Return type

[**CreateWebhookResponseBody**](CreateWebhookResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteWebhook

> String deleteWebhook(webhookId)

Delete Webhook By ID

Delete a webhook

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WebhooksApi();
let webhookId = "webhookId_example"; // String | Webhook ID
apiInstance.deleteWebhook(webhookId, (error, data, response) => {
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
 **webhookId** | **String**| Webhook ID | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## getWebhookById

> GetWebhookByIdResponseBody getWebhookById(webhookId)

Get Webhook By ID

Retrieve individual webhook by an ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WebhooksApi();
let webhookId = "webhookId_example"; // String | Webhook ID
apiInstance.getWebhookById(webhookId, (error, data, response) => {
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
 **webhookId** | **String**| Webhook ID | 

### Return type

[**GetWebhookByIdResponseBody**](GetWebhookByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWebhooks

> [Webhook] listWebhooks()

List Webhooks

List all webhooks currently enabled for the account.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WebhooksApi();
apiInstance.listWebhooks((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Webhook]**](Webhook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWebhook

> String updateWebhook(webhookId, updateWebhookRequestBody)

Update a Webhook

Update the webhook url property

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.WebhooksApi();
let webhookId = "webhookId_example"; // String | Webhook ID
let updateWebhookRequestBody = new ShipEngineApi.UpdateWebhookRequestBody(); // UpdateWebhookRequestBody | 
apiInstance.updateWebhook(webhookId, updateWebhookRequestBody, (error, data, response) => {
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
 **webhookId** | **String**| Webhook ID | 
 **updateWebhookRequestBody** | [**UpdateWebhookRequestBody**](UpdateWebhookRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain

