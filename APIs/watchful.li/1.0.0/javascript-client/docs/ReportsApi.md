# WatchfulLi.ReportsApi

All URIs are relative to *https://watchful.li/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsSitesIdGet**](ReportsApi.md#reportsSitesIdGet) | **GET** /reports/sites/{id} | Returns a PDF report for a specific site
[**reportsTagsIdGet**](ReportsApi.md#reportsTagsIdGet) | **GET** /reports/tags/{id} | Find sites by ID



## reportsSitesIdGet

> Object reportsSitesIdGet(id, opts)

Returns a PDF report for a specific site

Returns a PDF report based on a site ID

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.ReportsApi();
let id = 789; // Number | ID that needs to be fetched
let opts = {
  'from': "from_example", // String | Start of the report, format YYYY-MM-DD, default today-30day 
  'to': "to_example", // String | End of the report, format YYYY-MM-DD, default today
  'reports': "reports_example", // String | Type of reports separate by comas: Ga,Logs,Uptime
  'logType': "logType_example", // String | Type of the log to show in the report
  'compare': 56 // Number | Define if you want show previous values in Google Analytics graph
};
apiInstance.reportsSitesIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID that needs to be fetched | 
 **from** | **String**| Start of the report, format YYYY-MM-DD, default today-30day  | [optional] 
 **to** | **String**| End of the report, format YYYY-MM-DD, default today | [optional] 
 **reports** | **String**| Type of reports separate by comas: Ga,Logs,Uptime | [optional] 
 **logType** | **String**| Type of the log to show in the report | [optional] 
 **compare** | **Number**| Define if you want show previous values in Google Analytics graph | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf


## reportsTagsIdGet

> Object reportsTagsIdGet(id, opts)

Find sites by ID

Returns a report based on a site ID

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.ReportsApi();
let id = 789; // Number | ID that needs to be fetched
let opts = {
  'from': "from_example", // String | Start of the report, format YYYY-MM-DD, default today-30day 
  'to': "to_example", // String | End of the report, format YYYY-MM-DD, default today
  'reports': "reports_example", // String | Type of reports separate by comas: Ga,Logs,Uptime
  'logType': "logType_example", // String | Type of the log to show in the report
  'compare': 56 // Number | Define if you want show previous values in Google Analytics graph
};
apiInstance.reportsTagsIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID that needs to be fetched | 
 **from** | **String**| Start of the report, format YYYY-MM-DD, default today-30day  | [optional] 
 **to** | **String**| End of the report, format YYYY-MM-DD, default today | [optional] 
 **reports** | **String**| Type of reports separate by comas: Ga,Logs,Uptime | [optional] 
 **logType** | **String**| Type of the log to show in the report | [optional] 
 **compare** | **Number**| Define if you want show previous values in Google Analytics graph | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf

