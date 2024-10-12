# TwilioServerless.ServerlessV1FunctionVersionContentApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchFunctionVersionContent**](ServerlessV1FunctionVersionContentApi.md#fetchFunctionVersionContent) | **GET** /v1/Services/{ServiceSid}/Functions/{FunctionSid}/Versions/{Sid}/Content | 



## fetchFunctionVersionContent

> ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent fetchFunctionVersionContent(serviceSid, functionSid, sid)



Retrieve a the content of a specific Function Version resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1FunctionVersionContentApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Function Version content from.
let functionSid = "functionSid_example"; // String | The SID of the Function that is the parent of the Function Version content to fetch.
let sid = "sid_example"; // String | The SID of the Function Version content to fetch.
apiInstance.fetchFunctionVersionContent(serviceSid, functionSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Function Version content from. | 
 **functionSid** | **String**| The SID of the Function that is the parent of the Function Version content to fetch. | 
 **sid** | **String**| The SID of the Function Version content to fetch. | 

### Return type

[**ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent**](ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

