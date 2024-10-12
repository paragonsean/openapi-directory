# SubscriptionsApiV3.CyclesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRnsPubCyclesCycleIdGet**](CyclesApi.md#apiRnsPubCyclesCycleIdGet) | **GET** /api/rns/pub/cycles/{cycleId} | Get cycle details
[**apiRnsPubCyclesCycleIdRetryPost**](CyclesApi.md#apiRnsPubCyclesCycleIdRetryPost) | **POST** /api/rns/pub/cycles/{cycleId}/retry | Retry cycle
[**apiRnsPubCyclesGet**](CyclesApi.md#apiRnsPubCyclesGet) | **GET** /api/rns/pub/cycles | List cycles



## apiRnsPubCyclesCycleIdGet

> SubscriptionCycleResponse apiRnsPubCyclesCycleIdGet(cycleId, contentType, accept)

Get cycle details

Retrieve a specific cycle by its ID.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.CyclesApi();
let cycleId = "cycleId_example"; // String | ID from the desired cycle.
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPubCyclesCycleIdGet(cycleId, contentType, accept, (error, data, response) => {
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
 **cycleId** | **String**| ID from the desired cycle. | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

[**SubscriptionCycleResponse**](SubscriptionCycleResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiRnsPubCyclesCycleIdRetryPost

> apiRnsPubCyclesCycleIdRetryPost(cycleId, contentType, accept)

Retry cycle

Every subscription order has an execution count called cycle, which determines the position of an order counting from when the shopper subscribed. This endpoint reruns a cycle that is currently in error state.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.CyclesApi();
let cycleId = "cycleId_example"; // String | Id from the cycle that will be retried
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPubCyclesCycleIdRetryPost(cycleId, contentType, accept, (error, data, response) => {
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
 **cycleId** | **String**| Id from the cycle that will be retried | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRnsPubCyclesGet

> [SubscriptionCycleResponse] apiRnsPubCyclesGet(contentType, accept, opts)

List cycles

List cycles filtering by some arguments.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.CyclesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'beginDate': "beginDate_example", // String | Lower limit for the date of creation of the cycle
  'endDate': "endDate_example", // String | Upper limit for the date of creation of the cycle
  'subscriptionId': "subscriptionId_example", // String | Id from the subscription that generated the cycle
  'customerEmail': "customerEmail_example", // String | Customer that owns the subscription. Defaults to the current logged user
  'status': "status_example", // String | Current cycle status
  'page': 1, // Number | Page used for pagination
  'size': 15 // Number | Page size used for pagination
};
apiInstance.apiRnsPubCyclesGet(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **beginDate** | **String**| Lower limit for the date of creation of the cycle | [optional] 
 **endDate** | **String**| Upper limit for the date of creation of the cycle | [optional] 
 **subscriptionId** | **String**| Id from the subscription that generated the cycle | [optional] 
 **customerEmail** | **String**| Customer that owns the subscription. Defaults to the current logged user | [optional] 
 **status** | **String**| Current cycle status | [optional] 
 **page** | **Number**| Page used for pagination | [optional] [default to 1]
 **size** | **Number**| Page size used for pagination | [optional] [default to 15]

### Return type

[**[SubscriptionCycleResponse]**](SubscriptionCycleResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

