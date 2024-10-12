# TwilioServerless.ServerlessV1VariableApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVariable**](ServerlessV1VariableApi.md#createVariable) | **POST** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables | 
[**deleteVariable**](ServerlessV1VariableApi.md#deleteVariable) | **DELETE** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables/{Sid} | 
[**fetchVariable**](ServerlessV1VariableApi.md#fetchVariable) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables/{Sid} | 
[**listVariable**](ServerlessV1VariableApi.md#listVariable) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables | 
[**updateVariable**](ServerlessV1VariableApi.md#updateVariable) | **POST** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables/{Sid} | 



## createVariable

> ServerlessV1ServiceEnvironmentVariable createVariable(serviceSid, environmentSid, key, value)



Create a new Variable.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1VariableApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Variable resource under.
let environmentSid = "environmentSid_example"; // String | The SID of the Environment in which the Variable resource exists.
let key = "key_example"; // String | A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
let value = "value_example"; // String | A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.
apiInstance.createVariable(serviceSid, environmentSid, key, value, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to create the Variable resource under. | 
 **environmentSid** | **String**| The SID of the Environment in which the Variable resource exists. | 
 **key** | **String**| A string by which the Variable resource can be referenced. It can be a maximum of 128 characters. | 
 **value** | **String**| A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size. | 

### Return type

[**ServerlessV1ServiceEnvironmentVariable**](ServerlessV1ServiceEnvironmentVariable.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteVariable

> deleteVariable(serviceSid, environmentSid, sid)



Delete a specific Variable.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1VariableApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Variable resource from.
let environmentSid = "environmentSid_example"; // String | The SID of the Environment with the Variables to delete.
let sid = "sid_example"; // String | The SID of the Variable resource to delete.
apiInstance.deleteVariable(serviceSid, environmentSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to delete the Variable resource from. | 
 **environmentSid** | **String**| The SID of the Environment with the Variables to delete. | 
 **sid** | **String**| The SID of the Variable resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchVariable

> ServerlessV1ServiceEnvironmentVariable fetchVariable(serviceSid, environmentSid, sid)



Retrieve a specific Variable.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1VariableApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Variable resource from.
let environmentSid = "environmentSid_example"; // String | The SID of the Environment with the Variable resource to fetch.
let sid = "sid_example"; // String | The SID of the Variable resource to fetch.
apiInstance.fetchVariable(serviceSid, environmentSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Variable resource from. | 
 **environmentSid** | **String**| The SID of the Environment with the Variable resource to fetch. | 
 **sid** | **String**| The SID of the Variable resource to fetch. | 

### Return type

[**ServerlessV1ServiceEnvironmentVariable**](ServerlessV1ServiceEnvironmentVariable.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVariable

> ListVariableResponse listVariable(serviceSid, environmentSid, opts)



Retrieve a list of all Variables.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1VariableApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Variable resources from.
let environmentSid = "environmentSid_example"; // String | The SID of the Environment with the Variable resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listVariable(serviceSid, environmentSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Variable resources from. | 
 **environmentSid** | **String**| The SID of the Environment with the Variable resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListVariableResponse**](ListVariableResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateVariable

> ServerlessV1ServiceEnvironmentVariable updateVariable(serviceSid, environmentSid, sid, opts)



Update a specific Variable.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1VariableApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to update the Variable resource under.
let environmentSid = "environmentSid_example"; // String | The SID of the Environment with the Variable resource to update.
let sid = "sid_example"; // String | The SID of the Variable resource to update.
let opts = {
  'key': "key_example", // String | A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
  'value': "value_example" // String | A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.
};
apiInstance.updateVariable(serviceSid, environmentSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to update the Variable resource under. | 
 **environmentSid** | **String**| The SID of the Environment with the Variable resource to update. | 
 **sid** | **String**| The SID of the Variable resource to update. | 
 **key** | **String**| A string by which the Variable resource can be referenced. It can be a maximum of 128 characters. | [optional] 
 **value** | **String**| A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size. | [optional] 

### Return type

[**ServerlessV1ServiceEnvironmentVariable**](ServerlessV1ServiceEnvironmentVariable.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

