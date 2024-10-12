# WebhooksWebhooks.SubscriptionsApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive**](SubscriptionsApi.md#deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive) | **DELETE** /webhooks/v3/{appId}/subscriptions/{subscriptionId} | 
[**getWebhooksV3AppIdSubscriptionsGetAll**](SubscriptionsApi.md#getWebhooksV3AppIdSubscriptionsGetAll) | **GET** /webhooks/v3/{appId}/subscriptions | 
[**getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById**](SubscriptionsApi.md#getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById) | **GET** /webhooks/v3/{appId}/subscriptions/{subscriptionId} | 
[**patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate**](SubscriptionsApi.md#patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate) | **PATCH** /webhooks/v3/{appId}/subscriptions/{subscriptionId} | 
[**postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch**](SubscriptionsApi.md#postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch) | **POST** /webhooks/v3/{appId}/subscriptions/batch/update | 
[**postWebhooksV3AppIdSubscriptionsCreate**](SubscriptionsApi.md#postWebhooksV3AppIdSubscriptionsCreate) | **POST** /webhooks/v3/{appId}/subscriptions | 



## deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive

> deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive(subscriptionId, appId)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SubscriptionsApi();
let subscriptionId = 56; // Number | 
let appId = 56; // Number | 
apiInstance.deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive(subscriptionId, appId, (error, data, response) => {
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
 **subscriptionId** | **Number**|  | 
 **appId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getWebhooksV3AppIdSubscriptionsGetAll

> SubscriptionListResponse getWebhooksV3AppIdSubscriptionsGetAll(appId)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SubscriptionsApi();
let appId = 56; // Number | 
apiInstance.getWebhooksV3AppIdSubscriptionsGetAll(appId, (error, data, response) => {
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
 **appId** | **Number**|  | 

### Return type

[**SubscriptionListResponse**](SubscriptionListResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById

> SubscriptionResponse getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById(subscriptionId, appId)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SubscriptionsApi();
let subscriptionId = 56; // Number | 
let appId = 56; // Number | 
apiInstance.getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById(subscriptionId, appId, (error, data, response) => {
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
 **subscriptionId** | **Number**|  | 
 **appId** | **Number**|  | 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate

> SubscriptionResponse patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate(subscriptionId, appId, subscriptionPatchRequest)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SubscriptionsApi();
let subscriptionId = 56; // Number | 
let appId = 56; // Number | 
let subscriptionPatchRequest = new WebhooksWebhooks.SubscriptionPatchRequest(); // SubscriptionPatchRequest | 
apiInstance.patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate(subscriptionId, appId, subscriptionPatchRequest, (error, data, response) => {
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
 **subscriptionId** | **Number**|  | 
 **appId** | **Number**|  | 
 **subscriptionPatchRequest** | [**SubscriptionPatchRequest**](SubscriptionPatchRequest.md)|  | 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch

> BatchResponseSubscriptionResponse postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch(appId, batchInputSubscriptionBatchUpdateRequest)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SubscriptionsApi();
let appId = 56; // Number | 
let batchInputSubscriptionBatchUpdateRequest = new WebhooksWebhooks.BatchInputSubscriptionBatchUpdateRequest(); // BatchInputSubscriptionBatchUpdateRequest | 
apiInstance.postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch(appId, batchInputSubscriptionBatchUpdateRequest, (error, data, response) => {
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
 **appId** | **Number**|  | 
 **batchInputSubscriptionBatchUpdateRequest** | [**BatchInputSubscriptionBatchUpdateRequest**](BatchInputSubscriptionBatchUpdateRequest.md)|  | 

### Return type

[**BatchResponseSubscriptionResponse**](BatchResponseSubscriptionResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postWebhooksV3AppIdSubscriptionsCreate

> SubscriptionResponse postWebhooksV3AppIdSubscriptionsCreate(appId, subscriptionCreateRequest)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SubscriptionsApi();
let appId = 56; // Number | 
let subscriptionCreateRequest = new WebhooksWebhooks.SubscriptionCreateRequest(); // SubscriptionCreateRequest | 
apiInstance.postWebhooksV3AppIdSubscriptionsCreate(appId, subscriptionCreateRequest, (error, data, response) => {
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
 **appId** | **Number**|  | 
 **subscriptionCreateRequest** | [**SubscriptionCreateRequest**](SubscriptionCreateRequest.md)|  | 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

