# BeezUpMerchantApi.AnalyticsStatisticsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStoreReportByCategory**](AnalyticsStatisticsApi.md#getStoreReportByCategory) | **POST** /v2/user/analytics/{storeId}/reports/bycategory | Get the report by category
[**getStoreReportByChannel**](AnalyticsStatisticsApi.md#getStoreReportByChannel) | **POST** /v2/user/analytics/{storeId}/reports/bychannel | Get the report by channel
[**getStoreReportByDay**](AnalyticsStatisticsApi.md#getStoreReportByDay) | **POST** /v2/user/analytics/{storeId}/reports/byday | Get the report by day for a StoreId
[**getStoreReportByDayPerStore**](AnalyticsStatisticsApi.md#getStoreReportByDayPerStore) | **POST** /v2/user/analytics/reports/byday | Get the report by day for a StoreId
[**getStoreReportByProduct**](AnalyticsStatisticsApi.md#getStoreReportByProduct) | **POST** /v2/user/analytics/{storeId}/reports/byproduct | Get the report by product



## getStoreReportByCategory

> ReportByCategoryResponse getStoreReportByCategory(storeId, reportByCategoryRequest)

Get the report by category

Get the report by category

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsStatisticsApi();
let storeId = "storeId_example"; // String | Your store identifier
let reportByCategoryRequest = new BeezUpMerchantApi.ReportByCategoryRequest(); // ReportByCategoryRequest | 
apiInstance.getStoreReportByCategory(storeId, reportByCategoryRequest, (error, data, response) => {
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
 **reportByCategoryRequest** | [**ReportByCategoryRequest**](ReportByCategoryRequest.md)|  | 

### Return type

[**ReportByCategoryResponse**](ReportByCategoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getStoreReportByChannel

> ReportByChannelResponse getStoreReportByChannel(storeId, reportByChannelRequest)

Get the report by channel

Get the report by channel

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsStatisticsApi();
let storeId = "storeId_example"; // String | Your store identifier
let reportByChannelRequest = new BeezUpMerchantApi.ReportByChannelRequest(); // ReportByChannelRequest | 
apiInstance.getStoreReportByChannel(storeId, reportByChannelRequest, (error, data, response) => {
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
 **reportByChannelRequest** | [**ReportByChannelRequest**](ReportByChannelRequest.md)|  | 

### Return type

[**ReportByChannelResponse**](ReportByChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getStoreReportByDay

> ReportByDayResponse getStoreReportByDay(storeId, reportByDayRequest)

Get the report by day for a StoreId

Get the report by day for a StoreId

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsStatisticsApi();
let storeId = "storeId_example"; // String | Your store identifier
let reportByDayRequest = new BeezUpMerchantApi.ReportByDayRequest(); // ReportByDayRequest | 
apiInstance.getStoreReportByDay(storeId, reportByDayRequest, (error, data, response) => {
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
 **reportByDayRequest** | [**ReportByDayRequest**](ReportByDayRequest.md)|  | 

### Return type

[**ReportByDayResponse**](ReportByDayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getStoreReportByDayPerStore

> {String: ReportByDayResponse} getStoreReportByDayPerStore(reportByDayRequest)

Get the report by day for a StoreId

Get the report by day for a StoreId

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsStatisticsApi();
let reportByDayRequest = new BeezUpMerchantApi.ReportByDayRequest(); // ReportByDayRequest | 
apiInstance.getStoreReportByDayPerStore(reportByDayRequest, (error, data, response) => {
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
 **reportByDayRequest** | [**ReportByDayRequest**](ReportByDayRequest.md)|  | 

### Return type

[**{String: ReportByDayResponse}**](ReportByDayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getStoreReportByProduct

> ReportByProductResponse getStoreReportByProduct(storeId, reportByProductRequest)

Get the report by product

Get the report by product

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsStatisticsApi();
let storeId = "storeId_example"; // String | Your store identifier
let reportByProductRequest = new BeezUpMerchantApi.ReportByProductRequest(); // ReportByProductRequest | 
apiInstance.getStoreReportByProduct(storeId, reportByProductRequest, (error, data, response) => {
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
 **reportByProductRequest** | [**ReportByProductRequest**](ReportByProductRequest.md)|  | 

### Return type

[**ReportByProductResponse**](ReportByProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

