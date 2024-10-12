# ReportsApi.DefaultApi

All URIs are relative to *https://api.nexmo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelReport**](DefaultApi.md#cancelReport) | **DELETE** /v2/reports/{report_id} | Cancel the execution of a report
[**createAsyncReport**](DefaultApi.md#createAsyncReport) | **POST** /v2/reports | Create an asynchronous report
[**downloadReport**](DefaultApi.md#downloadReport) | **GET** /v3/media/{file_id} | Get report data
[**getRecords**](DefaultApi.md#getRecords) | **GET** /v2/reports/records | Load records synchronously
[**getReport**](DefaultApi.md#getReport) | **GET** /v2/reports/{report_id} | Get status of report
[**listReports**](DefaultApi.md#listReports) | **GET** /v2/reports | List reports



## cancelReport

> GetReport200Response cancelReport(reportId)

Cancel the execution of a report

Cancel the execution of a pending or processing report.

### Example

```javascript
import ReportsApi from 'reports_api';
let defaultClient = ReportsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ReportsApi.DefaultApi();
let reportId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | UUID of the report
apiInstance.cancelReport(reportId, (error, data, response) => {
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
 **reportId** | **String**| UUID of the report | 

### Return type

[**GetReport200Response**](GetReport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createAsyncReport

> CreateAsyncReport200Response createAsyncReport(opts)

Create an asynchronous report

Request a report on your account activity

### Example

```javascript
import ReportsApi from 'reports_api';
let defaultClient = ReportsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ReportsApi.DefaultApi();
let opts = {
  'createAsyncReportRequest': new ReportsApi.CreateAsyncReportRequest() // CreateAsyncReportRequest | The parameters of the JSON body will be used to create and filter the report.<br> The value of the `product` field will define which product the report will be created for and which parameters are accepted. 
};
apiInstance.createAsyncReport(opts, (error, data, response) => {
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
 **createAsyncReportRequest** | [**CreateAsyncReportRequest**](CreateAsyncReportRequest.md)| The parameters of the JSON body will be used to create and filter the report.&lt;br&gt; The value of the &#x60;product&#x60; field will define which product the report will be created for and which parameters are accepted.  | [optional] 

### Return type

[**CreateAsyncReport200Response**](CreateAsyncReport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## downloadReport

> DownloadReport200Response downloadReport(fileId)

Get report data

Download a zipped archive of the rendered report. The file is available for download for 72 hours.&lt;br&gt; The zip file will be named &#x60;&lt;PRODUCT&gt;_&lt;REPORT_ID&gt;.zip&#x60;&lt;br&gt; The csv file in the zip archive will be named as &#x60;report_&lt;PRODUCT&gt;_&lt;ACCOUNT_ID&gt;_&lt;DATE&gt;.csv&#x60; the date will be formatted as &#x60;yyyyMMdd&#x60;. 

### Example

```javascript
import ReportsApi from 'reports_api';
let defaultClient = ReportsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ReportsApi.DefaultApi();
let fileId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | UUID of the file.
apiInstance.downloadReport(fileId, (error, data, response) => {
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
 **fileId** | **String**| UUID of the file. | 

### Return type

[**DownloadReport200Response**](DownloadReport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## getRecords

> GetRecords200Response getRecords(accountId, product, opts)

Load records synchronously

Fetch usage data synchronously

### Example

```javascript
import ReportsApi from 'reports_api';
let defaultClient = ReportsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ReportsApi.DefaultApi();
let accountId = "abcd1234"; // String | The account for which the list of reports will be queried.
let product = "SMS"; // String | The product to return records for
let opts = {
  'direction': "inbound", // String | Direction of the communication, either `inbound` (received by our services), or `outbound` (originated from our services). Required for products `SMS` and `MESSAGES`. Optional for `VOICE-CALL`. Invalid for `IN-APP-VOICE`, `CONVERSATIONS`, `NUMBER-INSIGHT`, `VERIFY-API`.
  'id': "aaaaaaaa-bbbb-cccc-dddd-0123456789ab", // String | The UUID of the message or call to be searched for. You can specify a comma-separated list of UUIDs. If UUIDs are not found they are listed in the response in the `ids_not_found` field.  If you specify `id`, you must not specify `status`, `date_start` or `date_end`. 
  'dateStart': new Date("2017-12-01T00:00:00+0000"), // Date | ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format `yyyy-mm-ddThh:mm:ss[.sss]±hh:mm` or `yyyy-mm-ddThh:mm:ss[.sss]Z`) for when reports should begin.   It filters on the time the API call was received by Vonage and corresponds to the field `date_received` (`date_start` for Voice) in the report file. It is inclusive, i.e. the provided value is less than or equal to the value in the field `date_received` (`date_start` for Voice) in the CDR.  If you provide this, you must provide `date_end` and must not provide `id`. 
  'dateEnd': new Date("2018-01-01T00:00:00+0000"), // Date | **Must be no more than 24 hours later than `date_start`**  ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format `yyyy-mm-ddThh:mm:ss[.sss]±hh:mm` or `yyyy-mm-ddThh:mm:ss[.sss]Z`) for when report should end.  It is exclusive, i.e. the provided value is strictly greater than the value in the field `date_received` in the CDR.  If you provide this, you must provide `date_start` and must not provide `id`. 
  'includeMessage': true, // Boolean | Include the message contents in the records. Only applicable for use with products `SMS` and `MESSAGES`, where it is optional.
  'showConcatenated': false, // Boolean | Indicates whether the SMS was split up into multiple parts (due to its length).
  'status': "delivered" // String | The SMS status to search for. Optional where product is `SMS`.
};
apiInstance.getRecords(accountId, product, opts, (error, data, response) => {
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
 **accountId** | **String**| The account for which the list of reports will be queried. | 
 **product** | **String**| The product to return records for | 
 **direction** | **String**| Direction of the communication, either &#x60;inbound&#x60; (received by our services), or &#x60;outbound&#x60; (originated from our services). Required for products &#x60;SMS&#x60; and &#x60;MESSAGES&#x60;. Optional for &#x60;VOICE-CALL&#x60;. Invalid for &#x60;IN-APP-VOICE&#x60;, &#x60;CONVERSATIONS&#x60;, &#x60;NUMBER-INSIGHT&#x60;, &#x60;VERIFY-API&#x60;. | [optional] 
 **id** | **String**| The UUID of the message or call to be searched for. You can specify a comma-separated list of UUIDs. If UUIDs are not found they are listed in the response in the &#x60;ids_not_found&#x60; field.  If you specify &#x60;id&#x60;, you must not specify &#x60;status&#x60;, &#x60;date_start&#x60; or &#x60;date_end&#x60;.  | [optional] 
 **dateStart** | **Date**| ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;) for when reports should begin.   It filters on the time the API call was received by Vonage and corresponds to the field &#x60;date_received&#x60; (&#x60;date_start&#x60; for Voice) in the report file. It is inclusive, i.e. the provided value is less than or equal to the value in the field &#x60;date_received&#x60; (&#x60;date_start&#x60; for Voice) in the CDR.  If you provide this, you must provide &#x60;date_end&#x60; and must not provide &#x60;id&#x60;.  | [optional] 
 **dateEnd** | **Date**| **Must be no more than 24 hours later than &#x60;date_start&#x60;**  ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;) for when report should end.  It is exclusive, i.e. the provided value is strictly greater than the value in the field &#x60;date_received&#x60; in the CDR.  If you provide this, you must provide &#x60;date_start&#x60; and must not provide &#x60;id&#x60;.  | [optional] 
 **includeMessage** | **Boolean**| Include the message contents in the records. Only applicable for use with products &#x60;SMS&#x60; and &#x60;MESSAGES&#x60;, where it is optional. | [optional] [default to false]
 **showConcatenated** | **Boolean**| Indicates whether the SMS was split up into multiple parts (due to its length). | [optional] [default to false]
 **status** | **String**| The SMS status to search for. Optional where product is &#x60;SMS&#x60;. | [optional] [default to &#39;none&#39;]

### Return type

[**GetRecords200Response**](GetRecords200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReport

> GetReport200Response getReport(reportId)

Get status of report

Retrieve status and metadata about a requested report.

### Example

```javascript
import ReportsApi from 'reports_api';
let defaultClient = ReportsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ReportsApi.DefaultApi();
let reportId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | UUID of the report request (`request_id` in response).
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
 **reportId** | **String**| UUID of the report request (&#x60;request_id&#x60; in response). | 

### Return type

[**GetReport200Response**](GetReport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listReports

> ListReports200Response listReports(accountId, status, opts)

List reports

List reports created by the specified account based on filtered provided.

### Example

```javascript
import ReportsApi from 'reports_api';
let defaultClient = ReportsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ReportsApi.DefaultApi();
let accountId = "abcd1234"; // String | The account for which the list of reports will be queried.
let status = "SUCCESS, FAILED"; // String | A comma-separated list of report status values. Reports with any of the statuses specified are returned. The values in the comma-seperated list specified for `status` can be any of `PENDING`, `PROCESSING`, `SUCCESS`, `ABORTED`, `FAILED`, `TRUNCATED`.
let opts = {
  'dateFrom': new Date("2019-06-28T00:00:00-00:00"), // Date | ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date from which the list of reports will be queried. Format `yyyy-mm-ddThh:mm:ss[.sss]±hh:mm` or `yyyy-mm-ddThh:mm:ss[.sss]Z`.
  'dateTo': new Date("2019-06-28T23:59:59-00:00") // Date | ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date until which the list of reports will be queried. Format `yyyy-mm-ddThh:mm:ss[.sss]±hh:mm` or `yyyy-mm-ddThh:mm:ss[.sss]Z`.
};
apiInstance.listReports(accountId, status, opts, (error, data, response) => {
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
 **accountId** | **String**| The account for which the list of reports will be queried. | 
 **status** | **String**| A comma-separated list of report status values. Reports with any of the statuses specified are returned. The values in the comma-seperated list specified for &#x60;status&#x60; can be any of &#x60;PENDING&#x60;, &#x60;PROCESSING&#x60;, &#x60;SUCCESS&#x60;, &#x60;ABORTED&#x60;, &#x60;FAILED&#x60;, &#x60;TRUNCATED&#x60;. | 
 **dateFrom** | **Date**| ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date from which the list of reports will be queried. Format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;. | [optional] 
 **dateTo** | **Date**| ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date until which the list of reports will be queried. Format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;. | [optional] 

### Return type

[**ListReports200Response**](ListReports200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

