# VaultApi.ConsumersApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerRequestCountsAll**](ConsumersApi.md#consumerRequestCountsAll) | **GET** /vault/consumers/{consumer_id}/stats | Consumer request counts
[**consumersAdd**](ConsumersApi.md#consumersAdd) | **POST** /vault/consumers | Create consumer
[**consumersAll**](ConsumersApi.md#consumersAll) | **GET** /vault/consumers | Get all consumers
[**consumersDelete**](ConsumersApi.md#consumersDelete) | **DELETE** /vault/consumers/{consumer_id} | Delete consumer
[**consumersOne**](ConsumersApi.md#consumersOne) | **GET** /vault/consumers/{consumer_id} | Get consumer
[**consumersUpdate**](ConsumersApi.md#consumersUpdate) | **PATCH** /vault/consumers/{consumer_id} | Update consumer



## consumerRequestCountsAll

> ConsumerRequestCountsInDateRangeResponse consumerRequestCountsAll(xApideckAppId, consumerId, startDatetime, endDatetime)

Consumer request counts

Get consumer request counts within a given datetime range. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConsumersApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let consumerId = "test_user_id"; // String | ID of the consumer to return
let startDatetime = "2021-05-01T12:00:00.000Z"; // String | Scopes results to requests that happened after datetime
let endDatetime = "2021-05-30T12:00:00.000Z"; // String | Scopes results to requests that happened before datetime
apiInstance.consumerRequestCountsAll(xApideckAppId, consumerId, startDatetime, endDatetime, (error, data, response) => {
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
 **consumerId** | **String**| ID of the consumer to return | 
 **startDatetime** | **String**| Scopes results to requests that happened after datetime | 
 **endDatetime** | **String**| Scopes results to requests that happened before datetime | 

### Return type

[**ConsumerRequestCountsInDateRangeResponse**](ConsumerRequestCountsInDateRangeResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumersAdd

> CreateConsumerResponse consumersAdd(xApideckAppId, consumer)

Create consumer

Create a consumer

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConsumersApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let consumer = new VaultApi.Consumer(); // Consumer | 
apiInstance.consumersAdd(xApideckAppId, consumer, (error, data, response) => {
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
 **consumer** | [**Consumer**](Consumer.md)|  | 

### Return type

[**CreateConsumerResponse**](CreateConsumerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## consumersAll

> GetConsumersResponse consumersAll(xApideckAppId, opts)

Get all consumers

This endpoint includes all application consumers, along with an aggregated count of requests made. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConsumersApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20 // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
};
apiInstance.consumersAll(xApideckAppId, opts, (error, data, response) => {
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

[**GetConsumersResponse**](GetConsumersResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumersDelete

> DeleteConsumerResponse consumersDelete(xApideckAppId, consumerId)

Delete consumer

Delete consumer and all their connections, including credentials.

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConsumersApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let consumerId = "test_user_id"; // String | ID of the consumer to return
apiInstance.consumersDelete(xApideckAppId, consumerId, (error, data, response) => {
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
 **consumerId** | **String**| ID of the consumer to return | 

### Return type

[**DeleteConsumerResponse**](DeleteConsumerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumersOne

> GetConsumerResponse consumersOne(xApideckAppId, consumerId)

Get consumer

Consumer detail including their aggregated counts with the connections they have authorized. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConsumersApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let consumerId = "test_user_id"; // String | ID of the consumer to return
apiInstance.consumersOne(xApideckAppId, consumerId, (error, data, response) => {
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
 **consumerId** | **String**| ID of the consumer to return | 

### Return type

[**GetConsumerResponse**](GetConsumerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumersUpdate

> UpdateConsumerResponse consumersUpdate(xApideckAppId, consumerId, updateConsumerRequest)

Update consumer

Update consumer metadata such as name and email.

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConsumersApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let consumerId = "test_user_id"; // String | ID of the consumer to return
let updateConsumerRequest = new VaultApi.UpdateConsumerRequest(); // UpdateConsumerRequest | 
apiInstance.consumersUpdate(xApideckAppId, consumerId, updateConsumerRequest, (error, data, response) => {
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
 **consumerId** | **String**| ID of the consumer to return | 
 **updateConsumerRequest** | [**UpdateConsumerRequest**](UpdateConsumerRequest.md)|  | 

### Return type

[**UpdateConsumerResponse**](UpdateConsumerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

