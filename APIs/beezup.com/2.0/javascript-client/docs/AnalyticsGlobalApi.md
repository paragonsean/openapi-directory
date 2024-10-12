# BeezUpMerchantApi.AnalyticsGlobalApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyticsIndex**](AnalyticsGlobalApi.md#analyticsIndex) | **GET** /v2/user/analytics/ | Get the Analytics API operation index
[**analyticsStoreIndex**](AnalyticsGlobalApi.md#analyticsStoreIndex) | **GET** /v2/user/analytics/{storeId} | Get the Analytics API operation index for one store



## analyticsIndex

> AnalyticsIndex analyticsIndex()

Get the Analytics API operation index

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsGlobalApi();
apiInstance.analyticsIndex((error, data, response) => {
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

[**AnalyticsIndex**](AnalyticsIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsStoreIndex

> AnalyticsStoreIndex analyticsStoreIndex(storeId)

Get the Analytics API operation index for one store

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsGlobalApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.analyticsStoreIndex(storeId, (error, data, response) => {
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

[**AnalyticsStoreIndex**](AnalyticsStoreIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

