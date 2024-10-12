# AnchoreEngineApiServer.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSubscription**](SubscriptionsApi.md#addSubscription) | **POST** /subscriptions | Add a subscription of a specific type
[**deleteSubscription**](SubscriptionsApi.md#deleteSubscription) | **DELETE** /subscriptions/{subscriptionId} | Delete subscriptions of a specific type
[**getSubscription**](SubscriptionsApi.md#getSubscription) | **GET** /subscriptions/{subscriptionId} | Get a specific subscription set
[**listSubscriptions**](SubscriptionsApi.md#listSubscriptions) | **GET** /subscriptions | List all subscriptions
[**updateSubscription**](SubscriptionsApi.md#updateSubscription) | **PUT** /subscriptions/{subscriptionId} | Update an existing and specific subscription



## addSubscription

> [Subscription] addSubscription(subscriptionRequest, opts)

Add a subscription of a specific type

Create a new subscription to watch a tag and get notifications of changes

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SubscriptionsApi();
let subscriptionRequest = new AnchoreEngineApiServer.SubscriptionRequest(); // SubscriptionRequest | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.addSubscription(subscriptionRequest, opts, (error, data, response) => {
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
 **subscriptionRequest** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSubscription

> deleteSubscription(subscriptionId, opts)

Delete subscriptions of a specific type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.deleteSubscription(subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubscription

> [Subscription] getSubscription(subscriptionId, opts)

Get a specific subscription set

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getSubscription(subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSubscriptions

> [Subscription] listSubscriptions(opts)

List all subscriptions

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SubscriptionsApi();
let opts = {
  'subscriptionKey': "subscriptionKey_example", // String | filter only subscriptions matching key
  'subscriptionType': "subscriptionType_example", // String | filter only subscriptions matching type
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.listSubscriptions(opts, (error, data, response) => {
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
 **subscriptionKey** | **String**| filter only subscriptions matching key | [optional] 
 **subscriptionType** | **String**| filter only subscriptions matching type | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSubscription

> [Subscription] updateSubscription(subscriptionId, subscriptionUpdate, opts)

Update an existing and specific subscription

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | 
let subscriptionUpdate = new AnchoreEngineApiServer.SubscriptionUpdate(); // SubscriptionUpdate | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.updateSubscription(subscriptionId, subscriptionUpdate, opts, (error, data, response) => {
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
 **subscriptionId** | **String**|  | 
 **subscriptionUpdate** | [**SubscriptionUpdate**](SubscriptionUpdate.md)|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

