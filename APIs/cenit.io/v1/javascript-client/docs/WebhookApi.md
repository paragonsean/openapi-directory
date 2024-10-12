# CenitIoRestApiSpecification.WebhookApi

All URIs are relative to *https://cenit.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupWebhookGet**](WebhookApi.md#setupWebhookGet) | **GET** /setup/webhook/ | Returns a list of webhooks
[**setupWebhookIdDelete**](WebhookApi.md#setupWebhookIdDelete) | **DELETE** /setup/webhook/{id} | Delete a webhook
[**setupWebhookIdGet**](WebhookApi.md#setupWebhookIdGet) | **GET** /setup/webhook/{id} | Retrieve an existing webhook
[**setupWebhookPost**](WebhookApi.md#setupWebhookPost) | **POST** /setup/webhook/ | Create or update a webhook



## setupWebhookGet

> [Webhook] setupWebhookGet()

Returns a list of webhooks

Returns a list of webhooks you&#39;ve previously created. The webhooks are returned in sorted order, with the most recent webhook appearing first.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.WebhookApi();
apiInstance.setupWebhookGet((error, data, response) => {
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

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupWebhookIdDelete

> setupWebhookIdDelete(id)

Delete a webhook

Deletes the specified webhook.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.WebhookApi();
let id = "id_example"; // String | Webhook ID.
apiInstance.setupWebhookIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Webhook ID. | 

### Return type

null (empty response body)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setupWebhookIdGet

> Webhook setupWebhookIdGet(id)

Retrieve an existing webhook

Retrieves the details of an existing webhook. You need only supply the unique webhook identifier that was returned upon webhook creation.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.WebhookApi();
let id = "id_example"; // String | Webhook ID.
apiInstance.setupWebhookIdGet(id, (error, data, response) => {
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
 **id** | **String**| Webhook ID. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupWebhookPost

> Webhook setupWebhookPost()

Create or update a webhook

Creates or updates the specified webhook. Any parameters not provided will be left unchanged.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.WebhookApi();
apiInstance.setupWebhookPost((error, data, response) => {
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

[**Webhook**](Webhook.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

