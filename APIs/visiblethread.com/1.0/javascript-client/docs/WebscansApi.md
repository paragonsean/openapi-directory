# VisibleThreadApi.WebscansApi

All URIs are relative to *https://api.visiblethread.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getScanById**](WebscansApi.md#getScanById) | **GET** /webscans/{scanId} | Get data from a previously run scan
[**getScanUrlById**](WebscansApi.md#getScanUrlById) | **GET** /webscans/{scanId}/webUrls/{urlId} | Gets data for a particular scan/webUrl
[**runScan**](WebscansApi.md#runScan) | **POST** /webscans | Run a new scan
[**webscansGet**](WebscansApi.md#webscansGet) | **GET** /webscans | Get your list of scans



## getScanById

> ScanResponseDetailed getScanById(scanId)

Get data from a previously run scan

Get data from a previously run scan, identified by **scanId**

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.WebscansApi();
let scanId = 789; // Number | Id of scan to fetch
apiInstance.getScanById(scanId, (error, data, response) => {
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
 **scanId** | **Number**| Id of scan to fetch | 

### Return type

[**ScanResponseDetailed**](ScanResponseDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScanUrlById

> WebUrlDetail getScanUrlById(scanId, urlId)

Gets data for a particular scan/webUrl

Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** &amp; **urlId**

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.WebscansApi();
let scanId = 789; // Number | Id of scan
let urlId = 789; // Number | Id of url to fetch
apiInstance.getScanUrlById(scanId, urlId, (error, data, response) => {
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
 **scanId** | **Number**| Id of scan | 
 **urlId** | **Number**| Id of url to fetch | 

### Return type

[**WebUrlDetail**](WebUrlDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runScan

> NewScanResponse runScan(body)

Run a new scan

The scan runs in the background but returns immediately with a JSON response containing an \&quot;id\&quot; that represents your scan.         You can use this id in other requests to retrieve your scan result.   Also, an \&quot;id\&quot; is returned for each url which can be used to retrieve detailed results for individual scan urls. 

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.WebscansApi();
let body = new VisibleThreadApi.NewScan(); // NewScan | Scan title and webUrls to analyze
apiInstance.runScan(body, (error, data, response) => {
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
 **body** | [**NewScan**](NewScan.md)| Scan title and webUrls to analyze | 

### Return type

[**NewScanResponse**](NewScanResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webscansGet

> [ScanResponseSummary] webscansGet()

Get your list of scans

Get your list of scans

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.WebscansApi();
apiInstance.webscansGet((error, data, response) => {
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

[**[ScanResponseSummary]**](ScanResponseSummary.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

