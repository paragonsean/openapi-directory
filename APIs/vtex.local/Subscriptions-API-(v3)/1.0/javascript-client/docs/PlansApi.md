# SubscriptionsApiV3.PlansApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRnsPvtPlansGet**](PlansApi.md#apiRnsPvtPlansGet) | **GET** /api/rns/pvt/plans | List plans
[**apiRnsPvtPlansIdGet**](PlansApi.md#apiRnsPvtPlansIdGet) | **GET** /api/rns/pvt/plans/{id} | Get plan details



## apiRnsPvtPlansGet

> [StorePlan] apiRnsPvtPlansGet(contentType, accept, opts)

List plans

List plans filtering by some arguments.

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

let apiInstance = new SubscriptionsApiV3.PlansApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'periodicity': "periodicity_example", // String | Filter plans by available periodicity
  'interval': "interval_example", // String | Filter plans by available interval
  'page': 1, // Number | Page used for pagination
  'size': 15 // Number | Page size used for pagination
};
apiInstance.apiRnsPvtPlansGet(contentType, accept, opts, (error, data, response) => {
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
 **periodicity** | **String**| Filter plans by available periodicity | [optional] 
 **interval** | **String**| Filter plans by available interval | [optional] 
 **page** | **Number**| Page used for pagination | [optional] [default to 1]
 **size** | **Number**| Page size used for pagination | [optional] [default to 15]

### Return type

[**[StorePlan]**](StorePlan.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiRnsPvtPlansIdGet

> StorePlan apiRnsPvtPlansIdGet(id, contentType, accept)

Get plan details

This endpoint retrieves a specific plan by its ID.

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

let apiInstance = new SubscriptionsApiV3.PlansApi();
let id = "id_example"; // String | Id from the desired plan
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPvtPlansIdGet(id, contentType, accept, (error, data, response) => {
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
 **id** | **String**| Id from the desired plan | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

[**StorePlan**](StorePlan.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

