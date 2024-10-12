# ApiDocsLogoraisrCom.ReportsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsCreate**](ReportsApi.md#reportsCreate) | **POST** /reports/ | Create a new report.
[**reportsList**](ReportsApi.md#reportsList) | **GET** /reports/ | Get user report list.
[**reportsRead**](ReportsApi.md#reportsRead) | **GET** /reports/{report_number}/ | Get report details.



## reportsCreate

> ReportResponse reportsCreate(reportRequest)

Create a new report.

This POST-Method creates a new report.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.ReportsApi();
let reportRequest = new ApiDocsLogoraisrCom.ReportRequest(); // ReportRequest | 
apiInstance.reportsCreate(reportRequest, (error, data, response) => {
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
 **reportRequest** | [**ReportRequest**](ReportRequest.md)|  | 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportsList

> Report reportsList()

Get user report list.

This GET method lists the user&#39;s reports.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.ReportsApi();
apiInstance.reportsList((error, data, response) => {
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

[**Report**](Report.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsRead

> Report reportsRead(reportNumber)

Get report details.

This GET-Method returns the details of a specific report.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.ReportsApi();
let reportNumber = "reportNumber_example"; // String | 
apiInstance.reportsRead(reportNumber, (error, data, response) => {
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
 **reportNumber** | **String**|  | 

### Return type

[**Report**](Report.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

