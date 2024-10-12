# ChecksApi.ReportsApi

All URIs are relative to *https://api.truora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchUpload**](ReportsApi.md#batchUpload) | **POST** /v1/reports/{report_id}/upload | Batch Upload
[**createReport**](ReportsApi.md#createReport) | **POST** /v1/reports | Create Report
[**getReport**](ReportsApi.md#getReport) | **GET** /v1/reports/{report_id} | Get Report
[**listReports**](ReportsApi.md#listReports) | **GET** /v1/reports | List Reports



## batchUpload

> ReportOutput batchUpload(reportId, file)

Batch Upload

Upload multiple checks and associate them to the report. The inputs for these checks must be sent in an xlsx file, please use the following templates:  **Person:** [Chile](https://app.truora.com/files/person/person-input-cl.xlsx), [Colombia](https://app.truora.com/files/person/person-input-co.xlsx), [Mexico](https://app.truora.com/files/person/person-input-mx.xlsx), [Peru](https://app.truora.com/files/person/person-input-pe.xlsx), [Costa Rica](https://app.truora.com/files/person/person-input-cr.xlsx), [Brazil](https://app.truora.com/files/person/person-input-br.xlsx)  **Vehicle:** [Chile](https://app.truora.com/files/vehicle/vehicle-input-cl.xlsx), [Colombia](https://app.truora.com/files/vehicle/vehicle-input-co.xlsx), [Mexico](https://app.truora.com/files/vehicle/vehicle-input-mx.xlsx), [Peru](https://app.truora.com/files/vehicle/vehicle-input-pe.xlsx)  **Company** [Colombia](https://app.truora.com/files/company/company-input-co.xlsx), [Mexico](https://app.truora.com/files/company/company-input-mx.xlsx), [Brazil](https://app.truora.com/files/company/company-input-br.xlsx)  Keep in mind that we currently do not support batch uploads for custom check types. Background checks created by batch upload are processed with low priority.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ReportsApi();
let reportId = "reportId_example"; // String | The ID of the Report
let file = ["null"]; // [File] | Uploaded file name
apiInstance.batchUpload(reportId, file, (error, data, response) => {
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
 **reportId** | **String**| The ID of the Report | 
 **file** | **[File]**| Uploaded file name | 

### Return type

[**ReportOutput**](ReportOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## createReport

> ReportOutput createReport(name)

Create Report

Creates a Report to which it is possible to associate multiple Checks.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ReportsApi();
let name = "name_example"; // String | Report name
apiInstance.createReport(name, (error, data, response) => {
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
 **name** | **String**| Report name | 

### Return type

[**ReportOutput**](ReportOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getReport

> ReportOutput getReport(reportId)

Get Report

Returns a report with the given ID.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ReportsApi();
let reportId = "reportId_example"; // String | The ID of the Report
apiInstance.getReport(reportId, (error, data, response) => {
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
 **reportId** | **String**| The ID of the Report | 

### Return type

[**ReportOutput**](ReportOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listReports

> ReportsOutput listReports(opts)

List Reports

Lists all reports asociated with the client or user requesting.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ReportsApi();
let opts = {
  'startKey': "startKey_example", // String | Start value for pagination.
  'username': "username_example" // String | filter reports created by the specified username
};
apiInstance.listReports(opts, (error, data, response) => {
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
 **startKey** | **String**| Start value for pagination. | [optional] 
 **username** | **String**| filter reports created by the specified username | [optional] 

### Return type

[**ReportsOutput**](ReportsOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

