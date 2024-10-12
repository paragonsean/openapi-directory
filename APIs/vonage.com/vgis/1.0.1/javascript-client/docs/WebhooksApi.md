# VonageIntegrationSuite.WebhooksApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWebhook**](WebhooksApi.md#createWebhook) | **POST** /self/webhooks | Create a new webhook subscription
[**destroyWebhook**](WebhooksApi.md#destroyWebhook) | **DELETE** /self/webhooks/{id} | Remove a web hook
[**listWebhooks**](WebhooksApi.md#listWebhooks) | **GET** /self/webhooks | List web hooks
[**renewWebhook**](WebhooksApi.md#renewWebhook) | **PUT** /self/webhooks/{id}/renew | Renews a web hook
[**viewWebhook**](WebhooksApi.md#viewWebhook) | **GET** /self/webhooks/{id} | Get web hook details



## createWebhook

> Webhook createWebhook(webhookCreate)

Create a new webhook subscription

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.WebhooksApi();
let webhookCreate = new VonageIntegrationSuite.WebhookCreate(); // WebhookCreate | Webhook create parameters
apiInstance.createWebhook(webhookCreate, (error, data, response) => {
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
 **webhookCreate** | [**WebhookCreate**](WebhookCreate.md)| Webhook create parameters | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## destroyWebhook

> destroyWebhook(id)

Remove a web hook

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.WebhooksApi();
let id = "id_example"; // String | Unique identifier of the webhook
apiInstance.destroyWebhook(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the webhook | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWebhooks

> [Webhook] listWebhooks()

List web hooks

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.WebhooksApi();
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renewWebhook

> Webhook renewWebhook(id)

Renews a web hook

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.WebhooksApi();
let id = "id_example"; // String | Webhook ID
apiInstance.renewWebhook(id, (error, data, response) => {
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
 **id** | **String**| Webhook ID | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## viewWebhook

> Webhook viewWebhook(id)

Get web hook details

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.WebhooksApi();
let id = "id_example"; // String | Unique identifier of the webhook
apiInstance.viewWebhook(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the webhook | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

