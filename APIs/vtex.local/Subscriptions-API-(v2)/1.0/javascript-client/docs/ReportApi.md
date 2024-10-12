# SubscriptionsApiV2Deprecated.ReportApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getreportstatusbyID**](ReportApi.md#getreportstatusbyID) | **GET** /report/reportStatus/{reportId} | Get report status by ID
[**requestreportbyStatus**](ReportApi.md#requestreportbyStatus) | **GET** /report/subscriptionsByStatus | Retrieve Subscription report by Status
[**requestreportbydate**](ReportApi.md#requestreportbydate) | **GET** /report/subscriptionsByDate | Retrieve Subscription report by date
[**requestreportbyorderdate**](ReportApi.md#requestreportbyorderdate) | **GET** /report/subscriptionsOrderByDate | Retrieve Subscription report by order date
[**requestreportbyschedule**](ReportApi.md#requestreportbyschedule) | **GET** /report/subscriptionsScheduled | Retrieve Subscription report by schedule
[**requestreportbyupdate**](ReportApi.md#requestreportbyupdate) | **GET** /report/subscriptionsUpdated | Request report by update



## getreportstatusbyID

> getreportstatusbyID(contentType, accept, reportId)

Get report status by ID

Retrieves the Subscription&#39;s report status, filtering by its reportId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.ReportApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let reportId = "reportId_example"; // String | Report ID.
apiInstance.getreportstatusbyID(contentType, accept, reportId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **reportId** | **String**| Report ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## requestreportbyStatus

> requestreportbyStatus(requesterEmail, status, contentType, accept)

Retrieve Subscription report by Status

Retrieves Subscriptions&#39; reports, filtering by status. The report will be sent by email, to the address inserted in the API&#39;s path.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.ReportApi();
let requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
let status = 1; // Number | Binary OR of the following status: 1 - ACTIVE; 2 - PAUSED; 4 - CANCELED; 8 - EXPIRED
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.requestreportbyStatus(requesterEmail, status, contentType, accept, (error, data, response) => {
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
 **requesterEmail** | **String**| Email that the report will be sent to | 
 **status** | **Number**| Binary OR of the following status: 1 - ACTIVE; 2 - PAUSED; 4 - CANCELED; 8 - EXPIRED | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## requestreportbydate

> requestreportbydate(requesterEmail, beginDate, endDate, contentType, accept)

Retrieve Subscription report by date

Retrieves a report with the subscriptions created at the date interval requested

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.ReportApi();
let requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
let beginDate = 20190101; // Number | begin date of report interval, use format yyyyMMdd
let endDate = 20190701; // Number | end date of report interval, use format yyyyMMdd
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.requestreportbydate(requesterEmail, beginDate, endDate, contentType, accept, (error, data, response) => {
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
 **requesterEmail** | **String**| Email that the report will be sent to | 
 **beginDate** | **Number**| begin date of report interval, use format yyyyMMdd | 
 **endDate** | **Number**| end date of report interval, use format yyyyMMdd | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## requestreportbyorderdate

> requestreportbyorderdate(requesterEmail, beginDate, endDate, contentType, accept)

Retrieve Subscription report by order date

Retrieves a report regarding the Subscriptions created during the date interval of orders.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.ReportApi();
let requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
let beginDate = 20190101; // Number | begin date of report interval, use format yyyyMMdd
let endDate = 20190701; // Number | end date of report interval, use format yyyyMMdd
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.requestreportbyorderdate(requesterEmail, beginDate, endDate, contentType, accept, (error, data, response) => {
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
 **requesterEmail** | **String**| Email that the report will be sent to | 
 **beginDate** | **Number**| begin date of report interval, use format yyyyMMdd | 
 **endDate** | **Number**| end date of report interval, use format yyyyMMdd | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## requestreportbyschedule

> requestreportbyschedule(requesterEmail, beginDate, endDate, contentType, accept)

Retrieve Subscription report by schedule

Retrieves a report regarding the Subscriptions scheduled to execute at the date interval requested

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.ReportApi();
let requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
let beginDate = 20190101; // Number | begin date of report interval, use format yyyyMMdd
let endDate = 20190701; // Number | end date of report interval, use format yyyyMMdd
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.requestreportbyschedule(requesterEmail, beginDate, endDate, contentType, accept, (error, data, response) => {
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
 **requesterEmail** | **String**| Email that the report will be sent to | 
 **beginDate** | **Number**| begin date of report interval, use format yyyyMMdd | 
 **endDate** | **Number**| end date of report interval, use format yyyyMMdd | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## requestreportbyupdate

> requestreportbyupdate(requesterEmail, beginDate, endDate, contentType, accept)

Request report by update

Retrieves a report regarding Subscriptions updated in the date interval chosen. The report will be sent by email, to the address inserted in the API&#39;s path.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.ReportApi();
let requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
let beginDate = 20190101; // Number | begin date of report interval, use format yyyyMMdd
let endDate = 20190701; // Number | end date of report interval, use format yyyyMMdd
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.requestreportbyupdate(requesterEmail, beginDate, endDate, contentType, accept, (error, data, response) => {
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
 **requesterEmail** | **String**| Email that the report will be sent to | 
 **beginDate** | **Number**| begin date of report interval, use format yyyyMMdd | 
 **endDate** | **Number**| end date of report interval, use format yyyyMMdd | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

