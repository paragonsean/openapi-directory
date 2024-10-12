# HighwaysEnglandApi.ReportsApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsIndex**](ReportsApi.md#reportsIndex) | **GET** /v{version}/reports/{report_type} | Gets the daily report.
[**vversionReportsStartDateToEndDateReportTypeGet**](ReportsApi.md#vversionReportsStartDateToEndDateReportTypeGet) | **GET** /v{version}/reports/{start_date}/to/{end_date}/{report_type} | Gets the daily report.



## reportsIndex

> Object reportsIndex(reportType, sites, startDate, endDate, page, pageSize, version, opts)

Gets the daily report.

Get&#39;s the report.

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.ReportsApi();
let reportType = "reportType_example"; // String | Report Type Id (i.e Daily, Monthly, Annual)
let sites = "sites_example"; // String | Comma separated list of site Ids.
let startDate = "startDate_example"; // String | The start date of the report in the format ddmmyyyy (i.e 31012016)
let endDate = "endDate_example"; // String | The end date of the report in the format ddmmyyyy (i.e 31012016)
let page = 56; // Number | The page offset to return.
let pageSize = 56; // Number | The number of rows to return.
let version = "version_example"; // String | 
let opts = {
  'reportSubTypeId': 56 // Number | 
};
apiInstance.reportsIndex(reportType, sites, startDate, endDate, page, pageSize, version, opts, (error, data, response) => {
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
 **reportType** | **String**| Report Type Id (i.e Daily, Monthly, Annual) | 
 **sites** | **String**| Comma separated list of site Ids. | 
 **startDate** | **String**| The start date of the report in the format ddmmyyyy (i.e 31012016) | 
 **endDate** | **String**| The end date of the report in the format ddmmyyyy (i.e 31012016) | 
 **page** | **Number**| The page offset to return. | 
 **pageSize** | **Number**| The number of rows to return. | 
 **version** | **String**|  | 
 **reportSubTypeId** | **Number**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vversionReportsStartDateToEndDateReportTypeGet

> Object vversionReportsStartDateToEndDateReportTypeGet(reportType, sites, startDate, endDate, page, pageSize, version, opts)

Gets the daily report.

Get&#39;s the report.

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.ReportsApi();
let reportType = "reportType_example"; // String | Report Type Id (i.e Daily, Monthly, Annual)
let sites = "sites_example"; // String | Comma separated list of site Ids.
let startDate = "startDate_example"; // String | The start date of the report in the format ddmmyyyy (i.e 31012016)
let endDate = "endDate_example"; // String | The end date of the report in the format ddmmyyyy (i.e 31012016)
let page = 56; // Number | The page offset to return.
let pageSize = 56; // Number | The number of rows to return.
let version = "version_example"; // String | 
let opts = {
  'reportSubTypeId': 56 // Number | 
};
apiInstance.vversionReportsStartDateToEndDateReportTypeGet(reportType, sites, startDate, endDate, page, pageSize, version, opts, (error, data, response) => {
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
 **reportType** | **String**| Report Type Id (i.e Daily, Monthly, Annual) | 
 **sites** | **String**| Comma separated list of site Ids. | 
 **startDate** | **String**| The start date of the report in the format ddmmyyyy (i.e 31012016) | 
 **endDate** | **String**| The end date of the report in the format ddmmyyyy (i.e 31012016) | 
 **page** | **Number**| The page offset to return. | 
 **pageSize** | **Number**| The number of rows to return. | 
 **version** | **String**|  | 
 **reportSubTypeId** | **Number**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

