# XtrfHomePortalApi.ReportsApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete11**](ReportsApi.md#delete11) | **DELETE** /reports/{reportId} | Removes a report.
[**duplicate1**](ReportsApi.md#duplicate1) | **POST** /reports/{reportId}/duplicate | Duplicates a report.
[**exportToXML**](ReportsApi.md#exportToXML) | **POST** /reports/export/xml | Exports reports definition to XML.
[**generateCSV**](ReportsApi.md#generateCSV) | **GET** /reports/{reportId}/result/csv | Generates CSV content for a report.
[**generatePrinterFriendly**](ReportsApi.md#generatePrinterFriendly) | **GET** /reports/{reportId}/result/printerFriendly | Generates printer friendly content for a report.
[**importFromXML**](ReportsApi.md#importFromXML) | **POST** /reports/import/xml | Imports reports definition from XML.
[**setPreferred**](ReportsApi.md#setPreferred) | **PUT** /reports/{reportId}/preferred | Marks report as preferred or not.



## delete11

> delete11(reportId)

Removes a report.

Removes a report.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ReportsApi();
let reportId = 789; // Number | report's internal identifier
apiInstance.delete11(reportId, (error, data, response) => {
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
 **reportId** | **Number**| report&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## duplicate1

> duplicate1(reportId)

Duplicates a report.

Duplicates a report.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ReportsApi();
let reportId = 789; // Number | report's internal identifier
apiInstance.duplicate1(reportId, (error, data, response) => {
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
 **reportId** | **Number**| report&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportToXML

> ReportResultDTO exportToXML(exportRequestDTO)

Exports reports definition to XML.

Exports reports definition to XML.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ReportsApi();
let exportRequestDTO = /home-api/assets/examples/reports/exportToXML.json#requestBody; // ExportRequestDTO | Exported reports definition to XML.
apiInstance.exportToXML(exportRequestDTO, (error, data, response) => {
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
 **exportRequestDTO** | [**ExportRequestDTO**](ExportRequestDTO.md)| Exported reports definition to XML. | 

### Return type

[**ReportResultDTO**](ReportResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## generateCSV

> ReportResultDTO generateCSV(reportId)

Generates CSV content for a report.

Generates CSV content for a report.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ReportsApi();
let reportId = 789; // Number | report's internal identifier
apiInstance.generateCSV(reportId, (error, data, response) => {
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
 **reportId** | **Number**| report&#39;s internal identifier | 

### Return type

[**ReportResultDTO**](ReportResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## generatePrinterFriendly

> ReportResultDTO generatePrinterFriendly(reportId)

Generates printer friendly content for a report.

Generates printer friendly content for a report.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ReportsApi();
let reportId = 789; // Number | report's internal identifier
apiInstance.generatePrinterFriendly(reportId, (error, data, response) => {
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
 **reportId** | **Number**| report&#39;s internal identifier | 

### Return type

[**ReportResultDTO**](ReportResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## importFromXML

> ImportResultDTO importFromXML(importRequestDTO)

Imports reports definition from XML.

Imports a report definition from an XML using a file token. To obtain the token, you first need to upload a temporary XML file, as specified in the Files section. Note that the name of the imported report must be unique.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ReportsApi();
let importRequestDTO = /home-api/assets/examples/reports/importFromXML.json#requestBody; // ImportRequestDTO | Imported reports definition from XML.
apiInstance.importFromXML(importRequestDTO, (error, data, response) => {
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
 **importRequestDTO** | [**ImportRequestDTO**](ImportRequestDTO.md)| Imported reports definition from XML. | 

### Return type

[**ImportResultDTO**](ImportResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## setPreferred

> setPreferred(reportId, preferredRequestDTO)

Marks report as preferred or not.

Marks report as preferred or not.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ReportsApi();
let reportId = 789; // Number | report's internal identifier
let preferredRequestDTO = new XtrfHomePortalApi.PreferredRequestDTO(); // PreferredRequestDTO | Marked report as preferred or not.
apiInstance.setPreferred(reportId, preferredRequestDTO, (error, data, response) => {
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
 **reportId** | **Number**| report&#39;s internal identifier | 
 **preferredRequestDTO** | [**PreferredRequestDTO**](PreferredRequestDTO.md)| Marked report as preferred or not. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: Not defined

