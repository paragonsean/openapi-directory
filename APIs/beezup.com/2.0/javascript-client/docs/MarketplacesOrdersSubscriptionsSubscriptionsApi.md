# BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#activateSubscription) | **POST** /v2/user/marketplaces/orders/subscriptions/{id}/activate | Activate a subscription to the orders
[**createSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#createSubscription) | **POST** /v2/user/marketplaces/orders/subscriptions/{id} | Creates a subscription to the orders
[**deactivateSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#deactivateSubscription) | **POST** /v2/user/marketplaces/orders/subscriptions/{id}/deactivate | Deactivate a subscription to the orders
[**deleteSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#deleteSubscription) | **DELETE** /v2/user/marketplaces/orders/subscriptions/{id} | Delete a subscription to the orders
[**getSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#getSubscription) | **GET** /v2/user/marketplaces/orders/subscriptions/{id} | Get a subscription to the orders
[**getSubscriptionList**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#getSubscriptionList) | **GET** /v2/user/marketplaces/orders/subscriptions/ | Get the subscription list
[**getSubscriptionPushReporting**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#getSubscriptionPushReporting) | **GET** /v2/user/marketplaces/orders/subscriptions/{id}/reporting | Get the push reporting related to this subscription
[**retryPushOrders**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#retryPushOrders) | **POST** /v2/user/marketplaces/orders/subscriptions/{id}/retry | Force retry push orders immediatly



## activateSubscription

> activateSubscription(id, opts)

Activate a subscription to the orders

At this moment, BeezUP will ensure that your callback url is respecting this specification:  - https://api.beezup.com/swaggerhub/apis/BeezUP/public_marketplaces_orders_subscriptions_consumer-dev/1.0#/Subscriptions/Verification  After that we will send you the orders related to your subscription, respecting this specification:  - https://api.beezup.com/swaggerhub/apis/BeezUP/public_marketplaces_orders_subscriptions_consumer-dev/1.0#/Subscriptions/PushOrders 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi();
let id = "id_example"; // String | 
let opts = {
  'activateSubscriptionRequest': new BeezUpMerchantApi.ActivateSubscriptionRequest() // ActivateSubscriptionRequest | 
};
apiInstance.activateSubscription(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **activateSubscriptionRequest** | [**ActivateSubscriptionRequest**](ActivateSubscriptionRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSubscription

> createSubscription(id, createSubscriptionRequest)

Creates a subscription to the orders

Please take a look at this sequence diagram to understand the subscription process to follow [here](https://www.websequencediagrams.com/files/render?link&#x3D;SBYbeIc8NGshk6ooCbmjoBLIMl4fIGO1xjJbPBQAglBo0n6BwEReh7NXQiPSjOTX)

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi();
let id = "id_example"; // String | 
let createSubscriptionRequest = new BeezUpMerchantApi.CreateSubscriptionRequest(); // CreateSubscriptionRequest | 
apiInstance.createSubscription(id, createSubscriptionRequest, (error, data, response) => {
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
 **id** | **String**|  | 
 **createSubscriptionRequest** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deactivateSubscription

> deactivateSubscription(id)

Deactivate a subscription to the orders

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi();
let id = "id_example"; // String | 
apiInstance.deactivateSubscription(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSubscription

> deleteSubscription(id)

Delete a subscription to the orders

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi();
let id = "id_example"; // String | 
apiInstance.deleteSubscription(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubscription

> SubscriptionIndex getSubscription(id)

Get a subscription to the orders

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi();
let id = "id_example"; // String | 
apiInstance.getSubscription(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**SubscriptionIndex**](SubscriptionIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubscriptionList

> [SubscriptionIndex] getSubscriptionList()

Get the subscription list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi();
apiInstance.getSubscriptionList((error, data, response) => {
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

[**[SubscriptionIndex]**](SubscriptionIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubscriptionPushReporting

> [SubscriptionPushReporting] getSubscriptionPushReporting(id, opts)

Get the push reporting related to this subscription

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi();
let id = "id_example"; // String | 
let opts = {
  'pageNumber': 56, // Number | 
  'pageSize': 56 // Number | 
};
apiInstance.getSubscriptionPushReporting(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **pageNumber** | **Number**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 

### Return type

[**[SubscriptionPushReporting]**](SubscriptionPushReporting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retryPushOrders

> retryPushOrders(id)

Force retry push orders immediatly

In case your subscription consumption is unavailable and your subscription is still active you can ask to retry immediatly to push orders instead of waiting the next scheduled retry date

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersSubscriptionsSubscriptionsApi();
let id = "id_example"; // String | 
apiInstance.retryPushOrders(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

