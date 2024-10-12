# MessagingApiV3X.ReportsApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReport**](ReportsApi.md#getReport) | **GET** /reports/{reportId} | fetch a specific report
[**getReports**](ReportsApi.md#getReports) | **GET** /reports | fetch all reports
[**messagesReport**](ReportsApi.md#messagesReport) | **POST** /reports/messages | submit a request for a messages report



## getReport

> GetReport200Response getReport(contentLanguage, authorization, accept, acceptCharset, contentType, reportId, opts)

fetch a specific report

Fetch a download link for a report generated with POST /reports/{reportId} using the **reportId** returned in the response. Once ready, your report will be available for download for one week. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.ReportsApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let reportId = "reportId_example"; // String | Use the reportId returned in the POST /reports/{reportType} response. 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.getReport(contentLanguage, authorization, accept, acceptCharset, contentType, reportId, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **reportId** | **String**| Use the reportId returned in the POST /reports/{reportType} response.  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**GetReport200Response**](GetReport200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReports

> GetReports200Response getReports(contentLanguage, authorization, accept, acceptCharset, contentType, opts)

fetch all reports

Fetch details of all reports recently generated for your account. Use it to check the status of a report, plus fetch the report ID, status, report type and expiry date. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.ReportsApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.getReports(contentLanguage, authorization, accept, acceptCharset, contentType, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**GetReports200Response**](GetReports200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesReport

> MessagesReport201Response messagesReport(contentLanguage, authorization, accept, acceptCharset, contentType, messagesReportRequest, opts)

submit a request for a messages report

Request a CSV report of messages (both incoming and outgoing) that have been sent to/from your account within the last three months. You can request details for a specific timeframe, and filter your messages by tags, recipient number or Virtual Number.  A 201 Created means your report has been queued for generation. Make a note of the reportId returned in the response. You&#39;ll need this to check the status of your report and fetch your download link with GET reports/{reportId}. If you supplied a reportCallbackUrl in the request we&#39;ll also notify it when your report is ready for download.  Once your report is generated, it will be available for download for one week. The expiry date is returned in the response. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.ReportsApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let messagesReportRequest = new MessagingApiV3X.MessagesReportRequest(); // MessagesReportRequest | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.messagesReport(contentLanguage, authorization, accept, acceptCharset, contentType, messagesReportRequest, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **messagesReportRequest** | [**MessagesReportRequest**](MessagesReportRequest.md)|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**MessagesReport201Response**](MessagesReport201Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

