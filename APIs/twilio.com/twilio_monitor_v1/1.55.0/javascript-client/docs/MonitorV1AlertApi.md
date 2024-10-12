# TwilioMonitor.MonitorV1AlertApi

All URIs are relative to *https://monitor.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAlert**](MonitorV1AlertApi.md#fetchAlert) | **GET** /v1/Alerts/{Sid} | 
[**listAlert**](MonitorV1AlertApi.md#listAlert) | **GET** /v1/Alerts | 



## fetchAlert

> MonitorV1AlertInstance fetchAlert(sid)





### Example

```javascript
import TwilioMonitor from 'twilio_monitor';
let defaultClient = TwilioMonitor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMonitor.MonitorV1AlertApi();
let sid = "sid_example"; // String | The SID of the Alert resource to fetch.
apiInstance.fetchAlert(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Alert resource to fetch. | 

### Return type

[**MonitorV1AlertInstance**](MonitorV1AlertInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAlert

> ListAlertResponse listAlert(opts)





### Example

```javascript
import TwilioMonitor from 'twilio_monitor';
let defaultClient = TwilioMonitor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMonitor.MonitorV1AlertApi();
let opts = {
  'logLevel': "logLevel_example", // String | Only show alerts for this log-level.  Can be: `error`, `warning`, `notice`, or `debug`.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAlert(opts, (error, data, response) => {
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
 **logLevel** | **String**| Only show alerts for this log-level.  Can be: &#x60;error&#x60;, &#x60;warning&#x60;, &#x60;notice&#x60;, or &#x60;debug&#x60;. | [optional] 
 **startDate** | **Date**| Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as &#x60;YYYY-MM-DD&#x60; or &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;. Queries for alerts older than 30 days are not supported. | [optional] 
 **endDate** | **Date**| Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as &#x60;YYYY-MM-DD&#x60; or &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;. Queries for alerts older than 30 days are not supported. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListAlertResponse**](ListAlertResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

