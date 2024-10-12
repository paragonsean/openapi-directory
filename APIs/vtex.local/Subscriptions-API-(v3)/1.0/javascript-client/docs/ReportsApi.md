# SubscriptionsApiV3.ReportsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRnsPvtReportsGet**](ReportsApi.md#apiRnsPvtReportsGet) | **GET** /api/rns/pvt/reports | List report templates
[**apiRnsPvtReportsReportNameDocumentsDocumentIdGet**](ReportsApi.md#apiRnsPvtReportsReportNameDocumentsDocumentIdGet) | **GET** /api/rns/pvt/reports/{reportName}/documents/{documentId} | Get report document details
[**apiRnsPvtReportsReportNameDocumentsPost**](ReportsApi.md#apiRnsPvtReportsReportNameDocumentsPost) | **POST** /api/rns/pvt/reports/{reportName}/documents | Generate report



## apiRnsPvtReportsGet

> [SubscriptionReport] apiRnsPvtReportsGet(contentType, accept)

List report templates

List all report templates available.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.ReportsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPvtReportsGet(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

[**[SubscriptionReport]**](SubscriptionReport.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiRnsPvtReportsReportNameDocumentsDocumentIdGet

> ReportResponse apiRnsPvtReportsReportNameDocumentsDocumentIdGet(reportName, documentId, contentType, accept)

Get report document details

Retrieve a specific report document by its Id.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.ReportsApi();
let reportName = "reportName_example"; // String | Name of the report
let documentId = "documentId_example"; // String | Id from the desired report document
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPvtReportsReportNameDocumentsDocumentIdGet(reportName, documentId, contentType, accept, (error, data, response) => {
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
 **reportName** | **String**| Name of the report | 
 **documentId** | **String**| Id from the desired report document | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiRnsPvtReportsReportNameDocumentsPost

> ReportResponse apiRnsPvtReportsReportNameDocumentsPost(reportName, contentType, accept, opts)

Generate report

This endpoint creates a new report in the format of a CSV file and sends it via email. You can generate one of the following reports:    - subscriptionsWithStatus    - subscriptionsScheduledBetweenDate    - subscriptionsUpdatedBetweenDate    - subscriptionsCreatedBetweenDate    - executionsBetweenDate

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.ReportsApi();
let reportName = "reportName_example"; // String | Name of the type of report in wish to generate. The following values are accepted:    - `subscriptionsWithStatus`    - `subscriptionsScheduledBetweenDate`    - `subscriptionsUpdatedBetweenDate`    - `subscriptionsCreatedBetweenDate`    - `executionsBetweenDate`
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'email': "'receiver@email.com'", // String | The report is sent to the email in this field.
  'beginDate': "'2022-09-01'", // String | Start date of the report with the format `yyyy-mm-dd`. This field is required for any type of report.
  'endDate': "'2022-10-01'" // String | End date of the report with the format `yyyy-mm-dd`. This field is required for any type of report.
};
apiInstance.apiRnsPvtReportsReportNameDocumentsPost(reportName, contentType, accept, opts, (error, data, response) => {
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
 **reportName** | **String**| Name of the type of report in wish to generate. The following values are accepted:    - &#x60;subscriptionsWithStatus&#x60;    - &#x60;subscriptionsScheduledBetweenDate&#x60;    - &#x60;subscriptionsUpdatedBetweenDate&#x60;    - &#x60;subscriptionsCreatedBetweenDate&#x60;    - &#x60;executionsBetweenDate&#x60; | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **email** | **String**| The report is sent to the email in this field. | [optional] [default to &#39;receiver@email.com&#39;]
 **beginDate** | **String**| Start date of the report with the format &#x60;yyyy-mm-dd&#x60;. This field is required for any type of report. | [optional] [default to &#39;2022-09-01&#39;]
 **endDate** | **String**| End date of the report with the format &#x60;yyyy-mm-dd&#x60;. This field is required for any type of report. | [optional] [default to &#39;2022-10-01&#39;]

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

