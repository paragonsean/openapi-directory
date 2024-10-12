# TwilioServerless.ServerlessV1BuildStatusApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchBuildStatus**](ServerlessV1BuildStatusApi.md#fetchBuildStatus) | **GET** /v1/Services/{ServiceSid}/Builds/{Sid}/Status | 



## fetchBuildStatus

> ServerlessV1ServiceBuildBuildStatus fetchBuildStatus(serviceSid, sid)



Retrieve a specific Build resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1BuildStatusApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Build resource from.
let sid = "sid_example"; // String | The SID of the Build resource to fetch.
apiInstance.fetchBuildStatus(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Build resource from. | 
 **sid** | **String**| The SID of the Build resource to fetch. | 

### Return type

[**ServerlessV1ServiceBuildBuildStatus**](ServerlessV1ServiceBuildBuildStatus.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

