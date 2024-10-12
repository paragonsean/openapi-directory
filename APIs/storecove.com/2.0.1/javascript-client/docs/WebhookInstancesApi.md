# StorecoveApi.WebhookInstancesApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteWebhookInstance**](WebhookInstancesApi.md#deleteWebhookInstance) | **DELETE** /webhook_instances/{guid} | DELETE a WebhookInstance
[**getWebhookInstances**](WebhookInstancesApi.md#getWebhookInstances) | **GET** /webhook_instances/ | GET a WebhookInstance



## deleteWebhookInstance

> deleteWebhookInstance(guid)

DELETE a WebhookInstance

DELETE a specific WebhookInstance

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.WebhookInstancesApi();
let guid = "guid_example"; // String | WebhookInstance guid
apiInstance.deleteWebhookInstance(guid, (error, data, response) => {
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
 **guid** | **String**| WebhookInstance guid | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getWebhookInstances

> WebhookInstance getWebhookInstances()

GET a WebhookInstance

GET a WebhookInstance from the queue. After processing it successfully, DELETE it and GET the next one. When a 204 is received, the queue is empty and the polling process can sleep for a while.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.WebhookInstancesApi();
apiInstance.getWebhookInstances((error, data, response) => {
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

[**WebhookInstance**](WebhookInstance.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

