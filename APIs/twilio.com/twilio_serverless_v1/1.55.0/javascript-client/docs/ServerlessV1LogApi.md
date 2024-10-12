# TwilioServerless.ServerlessV1LogApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchLog**](ServerlessV1LogApi.md#fetchLog) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Logs/{Sid} | 
[**listLog**](ServerlessV1LogApi.md#listLog) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Logs | 



## fetchLog

> ServerlessV1ServiceEnvironmentLog fetchLog(serviceSid, environmentSid, sid)



Retrieve a specific log.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1LogApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Log resource from.
let environmentSid = "environmentSid_example"; // String | The SID of the environment with the Log resource to fetch.
let sid = "sid_example"; // String | The SID of the Log resource to fetch.
apiInstance.fetchLog(serviceSid, environmentSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Log resource from. | 
 **environmentSid** | **String**| The SID of the environment with the Log resource to fetch. | 
 **sid** | **String**| The SID of the Log resource to fetch. | 

### Return type

[**ServerlessV1ServiceEnvironmentLog**](ServerlessV1ServiceEnvironmentLog.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLog

> ListLogResponse listLog(serviceSid, environmentSid, opts)



Retrieve a list of all logs.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1LogApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Log resource from.
let environmentSid = "environmentSid_example"; // String | The SID of the environment with the Log resources to read.
let opts = {
  'functionSid': "functionSid_example", // String | The SID of the function whose invocation produced the Log resources to read.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The date/time (in GMT, ISO 8601) after which the Log resources must have been created. Defaults to 1 day prior to current date/time.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The date/time (in GMT, ISO 8601) before which the Log resources must have been created. Defaults to current date/time.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listLog(serviceSid, environmentSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Log resource from. | 
 **environmentSid** | **String**| The SID of the environment with the Log resources to read. | 
 **functionSid** | **String**| The SID of the function whose invocation produced the Log resources to read. | [optional] 
 **startDate** | **Date**| The date/time (in GMT, ISO 8601) after which the Log resources must have been created. Defaults to 1 day prior to current date/time. | [optional] 
 **endDate** | **Date**| The date/time (in GMT, ISO 8601) before which the Log resources must have been created. Defaults to current date/time. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListLogResponse**](ListLogResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

