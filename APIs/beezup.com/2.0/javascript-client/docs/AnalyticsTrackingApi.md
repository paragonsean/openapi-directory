# BeezUpMerchantApi.AnalyticsTrackingApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStoreTrackedClicks**](AnalyticsTrackingApi.md#getStoreTrackedClicks) | **GET** /v2/user/analytics/{storeId}/tracking/clicks | Get the latest tracked clicks
[**getStoreTrackedExternalOrders**](AnalyticsTrackingApi.md#getStoreTrackedExternalOrders) | **GET** /v2/user/analytics/{storeId}/tracking/externalorders | Get the latest tracked external orders
[**getStoreTrackedOrders**](AnalyticsTrackingApi.md#getStoreTrackedOrders) | **GET** /v2/user/analytics/{storeId}/tracking/orders | Get the latest tracked orders
[**getStoreTrackingStatus**](AnalyticsTrackingApi.md#getStoreTrackingStatus) | **GET** /v2/user/analytics/{storeId}/tracking/status | Get the synchronization status of clicks and orders of a store
[**getTrackingStatus**](AnalyticsTrackingApi.md#getTrackingStatus) | **GET** /v2/user/analytics/tracking/status | Get the global synchronization status of clicks and orders



## getStoreTrackedClicks

> TrackedClicks getStoreTrackedClicks(storeId, opts)

Get the latest tracked clicks

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsTrackingApi();
let storeId = "storeId_example"; // String | Your store identifier
let opts = {
  'count': 56 // Number | The amount of clicks to retrieve
};
apiInstance.getStoreTrackedClicks(storeId, opts, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **count** | **Number**| The amount of clicks to retrieve | [optional] 

### Return type

[**TrackedClicks**](TrackedClicks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStoreTrackedExternalOrders

> TrackedExternalOrders getStoreTrackedExternalOrders(storeId, opts)

Get the latest tracked external orders

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsTrackingApi();
let storeId = "storeId_example"; // String | Your store identifier
let opts = {
  'count': 56 // Number | The amount of external orders to retrieve
};
apiInstance.getStoreTrackedExternalOrders(storeId, opts, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **count** | **Number**| The amount of external orders to retrieve | [optional] 

### Return type

[**TrackedExternalOrders**](TrackedExternalOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStoreTrackedOrders

> TrackedOrders getStoreTrackedOrders(storeId, opts)

Get the latest tracked orders

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsTrackingApi();
let storeId = "storeId_example"; // String | Your store identifier
let opts = {
  'count': 56 // Number | The amount of orders to retrieve
};
apiInstance.getStoreTrackedOrders(storeId, opts, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **count** | **Number**| The amount of orders to retrieve | [optional] 

### Return type

[**TrackedOrders**](TrackedOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStoreTrackingStatus

> StoreTrackingStatus getStoreTrackingStatus(storeId)

Get the synchronization status of clicks and orders of a store

Clicks and orders are eventually consistent. \\ This operation gets the current state of projections for a store. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsTrackingApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.getStoreTrackingStatus(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**StoreTrackingStatus**](StoreTrackingStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackingStatus

> TrackingStatus getTrackingStatus()

Get the global synchronization status of clicks and orders

Clicks and orders are eventually consistent. \\ This operation gets the current global state of projections. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsTrackingApi();
apiInstance.getTrackingStatus((error, data, response) => {
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

[**TrackingStatus**](TrackingStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

