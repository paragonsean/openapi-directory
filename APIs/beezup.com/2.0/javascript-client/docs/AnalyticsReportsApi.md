# BeezUpMerchantApi.AnalyticsReportsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteReportFilter**](AnalyticsReportsApi.md#deleteReportFilter) | **DELETE** /v2/user/analytics/{storeId}/reports/filters/{reportFilterId} | Delete the report filter
[**getReportFilter**](AnalyticsReportsApi.md#getReportFilter) | **GET** /v2/user/analytics/{storeId}/reports/filters/{reportFilterId} | Get the report filter description
[**getReportFilters**](AnalyticsReportsApi.md#getReportFilters) | **GET** /v2/user/analytics/{storeId}/reports/filters | Get report filter list for the given store
[**saveReportFilter**](AnalyticsReportsApi.md#saveReportFilter) | **PUT** /v2/user/analytics/{storeId}/reports/filters/{reportFilterId} | Save the report filter



## deleteReportFilter

> deleteReportFilter(storeId, reportFilterId)

Delete the report filter

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsReportsApi();
let storeId = "storeId_example"; // String | Your store identifier
let reportFilterId = "reportFilterId_example"; // String | Your report filter identifier
apiInstance.deleteReportFilter(storeId, reportFilterId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **reportFilterId** | **String**| Your report filter identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportFilter

> ReportFilter getReportFilter(storeId, reportFilterId)

Get the report filter description

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsReportsApi();
let storeId = "storeId_example"; // String | Your store identifier
let reportFilterId = "reportFilterId_example"; // String | Your report filter identifier
apiInstance.getReportFilter(storeId, reportFilterId, (error, data, response) => {
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
 **reportFilterId** | **String**| Your report filter identifier | 

### Return type

[**ReportFilter**](ReportFilter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportFilters

> ReportFilterList getReportFilters(storeId)

Get report filter list for the given store

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsReportsApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.getReportFilters(storeId, (error, data, response) => {
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

[**ReportFilterList**](ReportFilterList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveReportFilter

> saveReportFilter(storeId, reportFilterId, saveReportFilterRequest)

Save the report filter

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsReportsApi();
let storeId = "storeId_example"; // String | Your store identifier
let reportFilterId = "reportFilterId_example"; // String | Your report filter identifier
let saveReportFilterRequest = new BeezUpMerchantApi.SaveReportFilterRequest(); // SaveReportFilterRequest | 
apiInstance.saveReportFilter(storeId, reportFilterId, saveReportFilterRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **reportFilterId** | **String**| Your report filter identifier | 
 **saveReportFilterRequest** | [**SaveReportFilterRequest**](SaveReportFilterRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

