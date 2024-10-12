# TwilioServerless.ServerlessV1FunctionVersionApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchFunctionVersion**](ServerlessV1FunctionVersionApi.md#fetchFunctionVersion) | **GET** /v1/Services/{ServiceSid}/Functions/{FunctionSid}/Versions/{Sid} | 
[**listFunctionVersion**](ServerlessV1FunctionVersionApi.md#listFunctionVersion) | **GET** /v1/Services/{ServiceSid}/Functions/{FunctionSid}/Versions | 



## fetchFunctionVersion

> ServerlessV1ServiceFunctionFunctionVersion fetchFunctionVersion(serviceSid, functionSid, sid)



Retrieve a specific Function Version resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1FunctionVersionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Function Version resource from.
let functionSid = "functionSid_example"; // String | The SID of the function that is the parent of the Function Version resource to fetch.
let sid = "sid_example"; // String | The SID of the Function Version resource to fetch.
apiInstance.fetchFunctionVersion(serviceSid, functionSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Function Version resource from. | 
 **functionSid** | **String**| The SID of the function that is the parent of the Function Version resource to fetch. | 
 **sid** | **String**| The SID of the Function Version resource to fetch. | 

### Return type

[**ServerlessV1ServiceFunctionFunctionVersion**](ServerlessV1ServiceFunctionFunctionVersion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFunctionVersion

> ListFunctionVersionResponse listFunctionVersion(serviceSid, functionSid, opts)



Retrieve a list of all Function Version resources.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1FunctionVersionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Function Version resources from.
let functionSid = "functionSid_example"; // String | The SID of the function that is the parent of the Function Version resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listFunctionVersion(serviceSid, functionSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Function Version resources from. | 
 **functionSid** | **String**| The SID of the function that is the parent of the Function Version resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListFunctionVersionResponse**](ListFunctionVersionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

