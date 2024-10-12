# NativeAdsPublisherApi.ReportsApi

All URIs are relative to *https://api.nativeads.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publisherReportsDailyGet**](ReportsApi.md#publisherReportsDailyGet) | **GET** /publisher/reports/daily | 
[**publisherReportsWebsiteGet**](ReportsApi.md#publisherReportsWebsiteGet) | **GET** /publisher/reports/website | 
[**publisherReportsWidgetGet**](ReportsApi.md#publisherReportsWidgetGet) | **GET** /publisher/reports/widget | 



## publisherReportsDailyGet

> ReportsDailyResponse publisherReportsDailyGet(token, startDate, endDate, limit, page)



Returns publisher statistics split by date

### Example

```javascript
import NativeAdsPublisherApi from 'native_ads_publisher_api';

let apiInstance = new NativeAdsPublisherApi.ReportsApi();
let token = "token_example"; // String | Native Ads Publisher API authentication token
let startDate = new Date("2013-10-20"); // Date | start date in format YYYY-MM-DD
let endDate = new Date("2013-10-20"); // Date | end date in format YYYY-MM-DD
let limit = 100; // Number | maximum number of results per page
let page = 1; // Number | page number
apiInstance.publisherReportsDailyGet(token, startDate, endDate, limit, page, (error, data, response) => {
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
 **token** | **String**| Native Ads Publisher API authentication token | 
 **startDate** | **Date**| start date in format YYYY-MM-DD | 
 **endDate** | **Date**| end date in format YYYY-MM-DD | 
 **limit** | **Number**| maximum number of results per page | [default to 100]
 **page** | **Number**| page number | [default to 1]

### Return type

[**ReportsDailyResponse**](ReportsDailyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publisherReportsWebsiteGet

> ReportsWebsiteResponse publisherReportsWebsiteGet(token, startDate, endDate, limit, page)



Returns publisher statistics split by website

### Example

```javascript
import NativeAdsPublisherApi from 'native_ads_publisher_api';

let apiInstance = new NativeAdsPublisherApi.ReportsApi();
let token = "token_example"; // String | Native Ads Publisher API authentication token
let startDate = new Date("2013-10-20"); // Date | start date in format YYYY-MM-DD
let endDate = new Date("2013-10-20"); // Date | end date in format YYYY-MM-DD
let limit = 100; // Number | maximum number of results per page
let page = 1; // Number | page number
apiInstance.publisherReportsWebsiteGet(token, startDate, endDate, limit, page, (error, data, response) => {
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
 **token** | **String**| Native Ads Publisher API authentication token | 
 **startDate** | **Date**| start date in format YYYY-MM-DD | 
 **endDate** | **Date**| end date in format YYYY-MM-DD | 
 **limit** | **Number**| maximum number of results per page | [default to 100]
 **page** | **Number**| page number | [default to 1]

### Return type

[**ReportsWebsiteResponse**](ReportsWebsiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publisherReportsWidgetGet

> ReportsWidgetResponse publisherReportsWidgetGet(token, startDate, endDate, limit, page)



Returns publisher statistics split by widget

### Example

```javascript
import NativeAdsPublisherApi from 'native_ads_publisher_api';

let apiInstance = new NativeAdsPublisherApi.ReportsApi();
let token = "token_example"; // String | Native Ads Publisher API authentication token
let startDate = new Date("2013-10-20"); // Date | start date in format YYYY-MM-DD
let endDate = new Date("2013-10-20"); // Date | end date in format YYYY-MM-DD
let limit = 100; // Number | maximum number of results per page
let page = 1; // Number | page number
apiInstance.publisherReportsWidgetGet(token, startDate, endDate, limit, page, (error, data, response) => {
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
 **token** | **String**| Native Ads Publisher API authentication token | 
 **startDate** | **Date**| start date in format YYYY-MM-DD | 
 **endDate** | **Date**| end date in format YYYY-MM-DD | 
 **limit** | **Number**| maximum number of results per page | [default to 100]
 **page** | **Number**| page number | [default to 1]

### Return type

[**ReportsWidgetResponse**](ReportsWidgetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

