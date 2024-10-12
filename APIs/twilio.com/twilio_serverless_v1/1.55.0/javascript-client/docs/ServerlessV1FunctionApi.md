# TwilioServerless.ServerlessV1FunctionApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFunction**](ServerlessV1FunctionApi.md#createFunction) | **POST** /v1/Services/{ServiceSid}/Functions | 
[**deleteFunction**](ServerlessV1FunctionApi.md#deleteFunction) | **DELETE** /v1/Services/{ServiceSid}/Functions/{Sid} | 
[**fetchFunction**](ServerlessV1FunctionApi.md#fetchFunction) | **GET** /v1/Services/{ServiceSid}/Functions/{Sid} | 
[**listFunction**](ServerlessV1FunctionApi.md#listFunction) | **GET** /v1/Services/{ServiceSid}/Functions | 
[**updateFunction**](ServerlessV1FunctionApi.md#updateFunction) | **POST** /v1/Services/{ServiceSid}/Functions/{Sid} | 



## createFunction

> ServerlessV1ServiceFunction createFunction(serviceSid, friendlyName)



Create a new Function resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1FunctionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Function resource under.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.
apiInstance.createFunction(serviceSid, friendlyName, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to create the Function resource under. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters. | 

### Return type

[**ServerlessV1ServiceFunction**](ServerlessV1ServiceFunction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteFunction

> deleteFunction(serviceSid, sid)



Delete a Function resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1FunctionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Function resource from.
let sid = "sid_example"; // String | The SID of the Function resource to delete.
apiInstance.deleteFunction(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to delete the Function resource from. | 
 **sid** | **String**| The SID of the Function resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchFunction

> ServerlessV1ServiceFunction fetchFunction(serviceSid, sid)



Retrieve a specific Function resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1FunctionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Function resource from.
let sid = "sid_example"; // String | The SID of the Function resource to fetch.
apiInstance.fetchFunction(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Function resource from. | 
 **sid** | **String**| The SID of the Function resource to fetch. | 

### Return type

[**ServerlessV1ServiceFunction**](ServerlessV1ServiceFunction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFunction

> ListFunctionResponse listFunction(serviceSid, opts)



Retrieve a list of all Functions.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1FunctionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Function resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listFunction(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Function resources from. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListFunctionResponse**](ListFunctionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFunction

> ServerlessV1ServiceFunction updateFunction(serviceSid, sid, friendlyName)



Update a specific Function resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1FunctionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to update the Function resource from.
let sid = "sid_example"; // String | The SID of the Function resource to update.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.
apiInstance.updateFunction(serviceSid, sid, friendlyName, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to update the Function resource from. | 
 **sid** | **String**| The SID of the Function resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters. | 

### Return type

[**ServerlessV1ServiceFunction**](ServerlessV1ServiceFunction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

