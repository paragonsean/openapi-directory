# AdafruitIoRestApi.WebhooksApi

All URIs are relative to *https://io.adafruit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRawWebhookFeedData**](WebhooksApi.md#createRawWebhookFeedData) | **POST** /webhooks/feed/:token/raw | Send arbitrary data to a feed via webhook URL.
[**createWebhookFeedData**](WebhooksApi.md#createWebhookFeedData) | **POST** /webhooks/feed/:token | Send data to a feed via webhook URL.



## createRawWebhookFeedData

> Data createRawWebhookFeedData()

Send arbitrary data to a feed via webhook URL.

The raw data webhook receiver accepts POST requests and stores the raw request body on your feed. This is useful when you don&#39;t have control of the webhook sender. If feed history is turned on, payloads will be truncated at 1024 bytes. If feed history is turned off, payloads will be truncated at 100KB.

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.WebhooksApi();
apiInstance.createRawWebhookFeedData((error, data, response) => {
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

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## createWebhookFeedData

> Data createWebhookFeedData(payload)

Send data to a feed via webhook URL.

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.WebhooksApi();
let payload = new AdafruitIoRestApi.CreateWebhookFeedDataRequest(); // CreateWebhookFeedDataRequest | Webhook payload containing data `value` parameter.
apiInstance.createWebhookFeedData(payload, (error, data, response) => {
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
 **payload** | [**CreateWebhookFeedDataRequest**](CreateWebhookFeedDataRequest.md)| Webhook payload containing data &#x60;value&#x60; parameter. | 

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv

